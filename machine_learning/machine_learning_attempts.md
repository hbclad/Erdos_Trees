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
- KNN predicting cull and alive status

## Ella
- Throwing linear models at it today to predict on cull w alive/dead. 

## Henry 
- I'm going to add the most recent fire year and size, along with the number of fires in between measurements as features to predict on. 
- Maybe use one binary model to choose between alive and dead, then another trained on alive trees to specify damages to the alive tree.  
- I'm going to look at CATBOOST, which is a decision tree boosting algorithm for datasets with a lot of categorical variables
- Seems like decision trees could be good in general, then bagging.  


