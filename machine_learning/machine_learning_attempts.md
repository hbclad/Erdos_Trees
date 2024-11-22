# Machine Learning Attempts Documentation
Here we can put which ideas and models we have tried along with their performance stats:
accuracy, precision, error rates, etc.  

In all models lets set random_state = 216 for reproducibility.  

## Allie
- SVC : Predicting dead vs alive using STATUSCD 
   - I first dropped all of the trees where the first measurement was dead and trees where second measurement was not recorded (code 0), or was recorded as removed by humans (code 3).
   - Then did pairplot to see which features I could use
      - Features I ended up using were "ELEV","YRS_SINCE_BURN","HT_pre_burn","Number_of_Fires","CULL_pre_burn"
   - performed k fold cross validation with n=5 to find optimal C value
   - Ended with mean CV accuracy of 75.1% with an optimal C value of 50 (higher C prioritizes correct classification with narrower margins)
   - Conclusion: This could be useful, but might be nice to do pca beforehand to see what that gives us next
## Christina 
- KNN predicting cull and alive status

## Ella

## Henry 
- I'm going to add the most recent fire year and size, along with the number of fires in between measurements as features to predict on. 
- Maybe use one binary model to choose between alive and dead, then another trained on alive trees to specify damages to the alive tree.  
- I'm going to look at CATBOOST, which is a decision tree boosting algorithm for datasets with a lot of categorical variables
- Seems like decision trees could be good in general, then bagging.  


