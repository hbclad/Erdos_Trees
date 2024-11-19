import pandas as pd
from sklearn.model_selection import train_test_split

def data_load_and_split(big_data = pd.read_csv("../Data/final_big_data.csv"), 
                        trimmed_data = pd.read_csv('../Data/trimmed_data.csv'), 
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
    big_data_firstMeas = big_data[pd.isna(big_data['INCIDENT1'])]
    big_data_secondMeas = big_data[~pd.isna(big_data['INCIDENT1'])]
    trimmed_data_firstMeas = trimmed_data[pd.isna(trimmed_data['INCIDENT1'])]
    trimmed_data_secondMeas = trimmed_data[~pd.isna(trimmed_data['INCIDENT1'])]
    #Perform the train_test_split on the first measurements 
    big_firstMeas_train, big_firstMeas_test = train_test_split(big_data_firstMeas, test_size=test_size,
                                                               random_state=random_state, shuffle=True)
    trimmed_firstMeas_train, trimmed_firstMeas_test = train_test_split(trimmed_data_firstMeas, test_size=test_size,
                                                               random_state=random_state, shuffle=True)
    #Now we should match up second measurements so that they are in the same train/test set as the
    #first measurement on the same tree
    big_secondMeas_train = big_data_secondMeas[big_data_secondMeas['PREV_TRE_CN'].isin(big_firstMeas_train['CN'])]
    big_secondMeas_test = big_data_secondMeas[big_data_secondMeas['PREV_TRE_CN'].isin(big_firstMeas_test['CN'])]
    trimmed_secondMeas_train = trimmed_data_secondMeas[trimmed_data_secondMeas['PREV_TRE_CN'].isin(trimmed_firstMeas_train['CN'])]
    trimmed_secondMeas_test = trimmed_data_secondMeas[trimmed_data_secondMeas['PREV_TRE_CN'].isin(trimmed_firstMeas_test['CN'])]

    return (big_firstMeas_train, big_secondMeas_train, big_firstMeas_test, big_secondMeas_test, 
            trimmed_firstMeas_train, trimmed_secondMeas_train, trimmed_firstMeas_test, trimmed_secondMeas_test)
