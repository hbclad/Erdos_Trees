import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, StratifiedKFold 


def data_merge(pre_burn, post_burn,
               indicator_features = ["ALIVE_pre_burn", "CULL_pre_burn", "DIA_pre_burn", "HT_pre_burn", "DRYBIO_AG_pre_burn", "ELEV", "SOFTWOOD", "YRS_SINCE_BURN", "NUM_BURNS", "BURN_AREA_TOTAL"],
               show_counts_after_burn = False,
               return_mini = True):
    '''
    This function takes two datasets corresponding to the first and second measurements
    of the same set of trees. It returns a single smaller dataframe with only the specified indicator
    features (also CN for reference, and our outcome features ALIVE_post_burn and CULL_post_burn). 
    If show_counts is set to True, it will also print (but NOT return) the counts of status codes
    after burn for all previously living trees. If return_mini is changed to False, it will return the
    entire combined dataframe.
    
    After running data_load_and_split(), I suggest running 
    data_merge(trimmed_firstMeas_train, trimmed_secondMeas_train), and the same for the test data.

    This is the exact same function that appears in data_loader.py.
    '''
    pre_burn_no_mystery_col = pre_burn.drop("Unnamed: 0", axis = 1)
    post_burn_no_mystery_col = post_burn.drop("Unnamed: 0", axis = 1)

    combined = pre_burn_no_mystery_col.merge(post_burn_no_mystery_col, left_on = "CN", right_on = "PREV_TRE_CN", suffixes = ("_pre_burn", "_post_burn"))
    combined.dropna(axis = 1, how = "all", inplace = True)

    # Checking the merge and removing redundant identifiers
    assert((combined["CN_pre_burn"] == combined["PREV_TRE_CN_post_burn"]).all())
    combined.drop("PREV_TRE_CN_post_burn", axis = 1, inplace = True)
    combined.rename(columns={"CN_pre_burn": "CN"}, inplace = True)
    
    if (combined["CONDID_pre_burn"] == combined["PREVCOND_post_burn"]).all():
        combined.drop("PREVCOND_post_burn", axis = 1, inplace = True)
    else: print("CONDID inconsistent; column will not be merged.")
    
    # Cleaning up redundant columns
    stable_features = ["PLOT", "LAT", "LON", "ELEV", "COUNTYCD", "UNITCD", "TREE", "SUBP", "UNIQUE_PLOT_ID", "SPCD", "SPGRPCD"]
    for col in stable_features:
        if (combined[col + "_pre_burn"] == combined[col + "_post_burn"]).all():
            combined.drop(col+"_post_burn", axis = 1, inplace = True)
            combined.rename(columns={col+"_pre_burn": col}, inplace = True)
        else: 
            print(f"{col} inconsistent; column will not be merged.")
    
    # Simplifying fire column names
    for num in ["1","2","3"]:
        for col in ["INCIDENT", "FIREYEAR", "AREA", "PERIM"]:
            combined.rename(columns={col+num+"_post_burn": col+num}, inplace = True)

    # Manipulating burn data to use as features
    for i in ["1","2","3"]:
        combined[f"YRS_SINCE_BURN{i}"] = combined["MEASYEAR_post_burn"] - combined[f"FIREYEAR{i}"]
    
    combined["YRS_SINCE_BURN"] = combined[["YRS_SINCE_BURN1","YRS_SINCE_BURN2","YRS_SINCE_BURN3"]].min(axis = 1)
    combined["NUM_BURNS"] = combined[["FIREYEAR1","FIREYEAR2","FIREYEAR3"]].notna().sum(axis=1)
    combined["BURN_AREA_TOTAL"] = combined[["AREA1","AREA2","AREA3"]].sum(axis=1)
    
    # Manipulating species codes to use as a feature
    combined["SOFTWOOD"] = 1*(combined["SPGRPCD_pre_burn"].between(0,24, inclusive = "both") & combined["SPGRPCD_post_burn"].between(0,24, inclusive = "both"))
    combined["HARDWOOD"] = 1*(combined["SPGRPCD_pre_burn"].between(25,48, inclusive = "both") & combined["SPGRPCD_post_burn"].between(25,48, inclusive = "both"))
    # I wrote these this way because some SPGRPCD were inconsistent between first and second observation.
    # SOFTWOOD and HARDWOOD should partition the dataset, which is why only SOFTWOOD is in the list of
    # features to retain.
    
    combined["ALIVE_pre_burn"] = 1*(combined["STATUSCD_pre_burn"] == 1)
    combined["ALIVE_post_burn"] = 1*(combined["STATUSCD_post_burn"] == 1)
    
    # Removing trees which were already dead
    combined = combined[~(combined['STATUSCD_pre_burn'] == 2)]
    if show_counts_after_burn:
        print("",
              combined["STATUSCD_post_burn"].value_counts(),
              "\n0 = couldn't resample, 1 = alive, 2 = dead, 3 = removed by humans")
    
    # Removing trees that were removed or nonsampled after burn
    combined = combined[~((combined['STATUSCD_post_burn'] == 3) | (combined['STATUSCD_post_burn'] == 0))]
    
    meta_features = ["CN","PLOT"]
    outcome_features = ["ALIVE_post_burn", "CULL_post_burn"] 
    mini_combined = combined[meta_features + indicator_features + outcome_features]

    if return_mini:
        return mini_combined
    else:
        return combined




def plotwise_split(big_data_path = '../Data/final_big_data.csv', 
                   trimmed_data_path = '../Data/trimmed_data.csv',
                   trimmed = True,
                   test_size = 0.2, 
                   random_state = 216
                   ):
    """
    Loads data from our CSV files (the file with only relevant features by default,
    the one with all columns if 'trimmed' is set to False). Performs a train-test split,
    keeping trees from the same PLOT together in the split to avoid the generalization issues
    caused each PLOT having very consistent outcomes. This way, trees in the test set will 
    not have a 'sister' tree 10 feet away in the training set which the model can use to predict.
    Size of the test set will approximate the test_size, but may be less exact than the vanilla 
    sklearn function.
    
    Returns 4 dataframes in order: training trees first measurement, second measurement, then
    test trees first and second measurement. Run these pairs through data_merge to 
    collate properly.
    """

    # Selecting which dataset to use
    if trimmed:
        data = pd.read_csv(trimmed_data_path)
    else:
        data = pd.read_csv(big_data_path)
    
    # Separate the dataset into the first and second measurements
    first_meas = data[pd.isna(data['PREV_TRE_CN'])]
    second_meas = data[~pd.isna(data['PREV_TRE_CN'])]

    plot_counts = pd.DataFrame(first_meas["PLOT"].value_counts())
    # The above function sorts by the count, i.e. the number of trees in that plot that we have
    # records for. This sorting provides the logic for the splits below, where I put plots into
    # 'bins' to ensure that our final split has representative plots of all size categories.

    total_plots = len(plot_counts)
    plot_counts["new index"] = range(total_plots) # adds a column counting up from 0
    plot_counts["decile bin"] = np.floor((total_plots - plot_counts["new index"] - 1) * 10 / total_plots)

    # Split the plots, stratifying by decile to ensure approximately the desired split in number of trees
    train_plots, test_plots = train_test_split(plot_counts.index, # this is actually the PLOT column
                                   test_size = test_size,
                                   random_state = random_state,
                                   stratify = plot_counts["decile bin"])
    
    train_trees_1 = first_meas[first_meas['PLOT'].isin(train_plots)]
    train_trees_2 = second_meas[second_meas['PLOT'].isin(train_plots)]
    test_trees_1 = first_meas[first_meas['PLOT'].isin(test_plots)]
    test_trees_2 = second_meas[second_meas['PLOT'].isin(test_plots)]
    
    return train_trees_1, train_trees_2, test_trees_1, test_trees_2



def plotwise_kfold(train, n_splits=5, random_state=216, shuffle=True):
    '''
    For a merged set of tree data which includes a PLOT column, split into K folds of
    approximately equal size, keeping PLOTs separated as with plotwise_split. Returns
    a list of n_splits pairs of dataframes in the format (train, val). The three optional
    parameters are passed to the KFold object.

    THIS RETURNS DATAFRAMES. I could not figure out how to get it to do the indexes like KFold
    usually would. You will have to adjust your code slightly to use this one.
    '''

    plot_counts = pd.DataFrame(train["PLOT"].value_counts())

    total_plots = len(plot_counts)
    plot_counts["new index"] = range(total_plots) # adds a column counting up from 0
    plot_counts["decile bin"] = np.floor((total_plots - plot_counts["new index"] - 1) * 10 / total_plots)

    plot_kfold = StratifiedKFold(n_splits=n_splits, random_state=random_state, shuffle=shuffle)

    folds = []
    for train_index, test_index in plot_kfold.split(plot_counts, plot_counts['decile bin']):
        plot_tt = plot_counts.index[train_index] # recall that 'index' for the value_counts df
        plot_val = plot_counts.index[test_index] # is the column that was being counted
        
        tree_tt = train[train["PLOT"].isin(plot_tt)]
        tree_val = train[train["PLOT"].isin(plot_val)]
        folds.append((tree_tt,tree_val))
    
    return folds