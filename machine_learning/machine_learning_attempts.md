# Machine Learning Attempts Documentation
Here we can put which ideas and models we have tried along with their performance stats:
accuracy, precision, error rates, etc.  

In all models lets set random_state = 216 for reproducibility.  

## Allie
- Used Dummy Classifer with strategy: stratified and most frequent for baseline
  - Stratified: chooses from a probability distribution based on the proportion of each class in the training set
      - Gives Accuracy of 61%
  - Most: Frequent: classifies all as most frequent class in training
      - Gives Accuracy of 72%
- SVC : Predicting dead vs alive using STATUSCD .
   - Features I ended up using were "ELEV","HT_pre_burn","BURN_AREA_TOTAL"
      - I tried all combos of this including just using "ELEV", etc
      - I tried including CULL_pre_burn and this worsened accuracy
   - performed k fold cross validation with n=5 to find optimal C value and best kernel
   - Conclusion: Kernel RBF with C=70 gives accuracy of 75.8%

## Christina 
KNN classifying living/dead, best outcomes for specified feature sets:
- 78.9% with all indicator_features in the merged data and 4 neighbors
- 81.0% with ["CULL_pre_burn", "ELEV", "SOFTWOOD", "BURN_AREA_TOTAL"] and 8 neighbors
    - far worse with NUM_BURNS instead of BURN_AREA_TOTAL (low 70s)
- 81.5% with ["ELEV", "SOFTWOOD", "BURN_AREA_TOTAL"] and 8 neighbors
    - Adding YRS_SINCE_BURN helps by another % point, HOWEVER this is most likely due to data leakage;
    trees with a higher delay in measuring were probably more likely to have been removed, or impossible
    to locate when it was time to resample.

KNN regressing for CULL:
- Almost all scores I calculated were under 0.1. This indicates KNN may not be very effective method of predicting CULL. However, some models were consistently above 0, so they are still more accurate than a mean regressor.
- .083 using all features, 17 neighbors
- .082 using ["CULL_pre_burn", "ELEV", "SOFTWOOD", "YRS_SINCE_BURN", "BURN_AREA_TOTAL"], 17 neighbors
    - adding in DIA or HT made it worse
- .101 using ["CULL_pre_burn", "DRYBIO_AG_pre_burn", "ELEV", "SOFTWOOD", "YRS_SINCE_BURN", "BURN_AREA_TOTAL"] and 18 neighbors

## Ella
- Throwing linear models at it today to predict on cull w alive/dead (unsuccesful due to the data missing in the CULL values)  
- Built a "health" ```'TREECOND_pre_burn``` class based on the CR column. Health class will be extended upon after preliminary KNN investigation.
    - Using "health" based only on the CR value, baseline KNN (w/ choice features) accuracy score was 0.65 with k = 31 neighbors. Only searched up to 36 neighbors.  
        - Searching through at least 100 neighbors returned the accuracy & number of neighbors results.
        - Features: ```features = ['ELEV','TREECOND_pre_burn_encoded','DRYBIO_AG_pre_burn', 'DRYBIO_AG_post_burn', 'DIA_pre_burn', 'DIA_post_burn',
            'HT_pre_burn', 'HT_post_burn']```

## Henry 
- I'm going to add the most recent fire year and size, along with the number of fires in between measurements as features to predict on. 
- Maybe use one binary model to choose between alive and dead, then another trained on alive trees to specify damages to the alive tree.  
- I'm going to look at CATBOOST, which is a decision tree boosting algorithm for datasets with a lot of categorical variables
- Seems like decision trees could be good in general, then bagging.  


