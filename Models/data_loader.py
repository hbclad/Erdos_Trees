import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def data_load_and_split(big_data=pd.read_csv('../Data/final_big_data.csv'), 
                        trimmed_data= pd.read_csv('../Data/trimmed_data.csv'), 
                        test_size = 0.2, 
                        random_state = 216
                        ):

    """
    Loads our data frames (both large and trimmed), performs a train-test split on both, and returns the splits.
    
    Parameters:
    - big_data: larger data frame
    - trimmed_data: trimmed data frame
    - test_size: Proportion of the data to be used for testing (default 0.2)
    - random_state: Seed for reproducibility 
    
    Returns:
    - X_train, X_test, y_train, y_test: Split data (X and y)

    """
    #Separate each dataset into the first and second measurements
    big_data_firstMeas = big_data[pd.isna(big_data['PREV_TRE_CN'])]
    big_data_secondMeas = big_data[~pd.isna(big_data['PREV_TRE_CN'])]
    trimmed_data_firstMeas = trimmed_data[pd.isna(trimmed_data['PREV_TRE_CN'])]
    trimmed_data_secondMeas = trimmed_data[~pd.isna(trimmed_data['PREV_TRE_CN'])]
    #Perform the train_test_split on the first measurements 
    big_firstMeas_train, big_firstMeas_test = train_test_split(big_data_firstMeas, test_size=test_size,
                                                               random_state=random_state, shuffle=True)
    trimmed_firstMeas_train, trimmed_firstMeas_test = train_test_split(trimmed_data_firstMeas, test_size=test_size,
                                                               random_state=random_state, shuffle=True)
    #Now we should match up second measurements so that they are in the same train/test set as the
    #first measurement on the same tree-- Need to add PREV_TRE_CN back into the trimmed dataset..
    big_secondMeas_train = big_data_secondMeas[big_data_secondMeas['PREV_TRE_CN'].isin(big_firstMeas_train['CN'])]
    big_secondMeas_test = big_data_secondMeas[big_data_secondMeas['PREV_TRE_CN'].isin(big_firstMeas_test['CN'])]
    trimmed_secondMeas_train = trimmed_data_secondMeas[trimmed_data_secondMeas['PREV_TRE_CN'].isin(trimmed_firstMeas_train['CN'])]
    trimmed_secondMeas_test = trimmed_data_secondMeas[trimmed_data_secondMeas['PREV_TRE_CN'].isin(trimmed_firstMeas_test['CN'])]

    return (big_firstMeas_train, big_secondMeas_train, big_firstMeas_test, big_secondMeas_test, 
            trimmed_firstMeas_train, trimmed_secondMeas_train, trimmed_firstMeas_test, trimmed_secondMeas_test)



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
    
    meta_features = ["CN"]
    outcome_features = ["ALIVE_post_burn", "CULL_post_burn"] 
    mini_combined = combined[meta_features + indicator_features + outcome_features]

    if return_mini:
        return mini_combined
    else:
        return combined