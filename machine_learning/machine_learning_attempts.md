# Machine Learning Attempts Documentation
Here we can put which ideas and models we have tried along with their performance stats:
accuracy, precision, error rates, etc.  

In all models lets set random_state = 216 for reproducibility.  

## Allie
Predicting alive/dead
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
Predicting Diameter post/burn
- I used a mlr model and ridge model both with ["DIA_pre_burn","HT_pre_burn","DRYBIO_AG_pre_burn","BURN_AREA_TOTAL"] to predict DIA_post_burn.
    - R2 scores of .98 for both
 -Baseline model where just predict DIA_post_burn is same as DIA_pre_burn already works quite well with R2 score of .98 since diameter doesn't change much!
Predicting Height post/burn
- I used a mlr model and ridge model both with ["DIA_pre_burn","HT_pre_burn","DRYBIO_AG_pre_burn","BURN_AREA_TOTAL"] to predict DIA_post_burn.
    - R2 scores of .96 for both
 -Baseline model where just predict DIA_post_burn is same as DIA_pre_burn already works quite well with R2 score of .94 since diameter doesn't change much!
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
- Built a "health" ```'TREECOND_pre_burn``` class based on the CR column. Health class will be extended upon after preliminary KNN investigation. This works on post burn ALIVE trees only. I'm working on getting the dead ones factored in.  
    - Using "health" based only on the CR value, baseline KNN (w/ choice features) accuracy score was 65% with k = 31 neighbors. Only searched up to 36 neighbors.  
        - Searching through at least 100 neighbors returned the accuracy & number of neighbors results.
        - Features: ```features = ['ELEV','TREECOND_pre_burn_encoded','DRYBIO_AG_pre_burn', 'DRYBIO_AG_post_burn', 'DIA_pre_burn', 'DIA_post_burn',
            'HT_pre_burn', 'HT_post_burn']```
      - Using the same health indicator, but with all features we got an accuracy score of 69% with k = 1 neighbor.. certianly overfitting. Accuraccy declined rapidally to 0.64 after double digit neighbors.
      - Using a list of refined features, accuracy score increased to 80% with k = 6 neighbors, which is reasonable in my mind.
          - refined feature list can be found in my nb titled knnqualitystudy in the ML folder.
      - Attemped a PCA with 2 features to investigate if our data is PCA friendly -- it's not. The result is well presented in the previously refrenced nb in the ML folder.
      - Attempted LDA as a pre-processor, when plotting this seperated our data incredibly well. Then applying a KNN classifer I was able to get **97.2% accuracy with k = 37 neighbors**. This model, even with less than 10 neighbors still performs at nearly 95% accuracy. The LDA worked well on our data due to the strong linearity of our features.. Results presented in the previously refrenced nb in the ML folder. Yeet. 🥳

## Henry 
- Made a decision tree using RandomizedSearchCV, which does random parameter search for max_depth and num_estimators with a stratified 5 Kfold split.  The best tree found was (17,260) with a mean accuracy on the Kfolds of 82%.  Accuracy on testing set is 81%.  
- Feature importances show that ELEV, BURN_AREA, DRYBIO_AG, HT_pre_burn, DIA, YRS_since_burn are the most common features in the decision forest.  With num_burns and cull_pre_burn having much less importance.  
- Thinking about predicting DIA or HT post_burn and comparing to expected growth rates using a linear model. After adding tree species to the model.  
- Might add tree species to the model- seems like it would help.  



