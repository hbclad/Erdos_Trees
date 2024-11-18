import pandas as pd
from sklearn.model_selection import train_test_split

big_data = pd.read_csv("../Data/final_big_data.csv")
trimmed_data = pd.read_csv('../Data/trimmed_data.csv')

def data_load_and_splot(big_data, trimmed_data, test_size = 0.2, random_state = 216):
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
    trimmed_train, trimmed_test = train_test_split(trimmed_data, test_size=test_size, random_state=random_state, shuffle = True)
    big_train, big_test = train_test_split(big_data, test_size=test_size, random_state=random_state, shuffle = True)
    return trimmed_train, trimmed_test, big_train, big_test





