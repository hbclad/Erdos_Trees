# Machine Learning Attempts Documentation
Here we can put which ideas and models we have tried along with their performance stats:
accuracy, precision, error rates, etc.  

In all models lets set random_state = 216 for reproducibility.  

## Allie
- Used Dummy Classifer with strategy: stratified for baseline
  - Accuracy: 58%
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
- Throwing linear models at it today to predict on cull w alive/dead. 

## Henry 
- Made a decision tree using RandomizedSearchCV, which does random parameter search for max_depth and num_estimators with a stratified 5 Kfold split.  The best tree found was (17,260) with a mean accuracy on the Kfolds of 82%.  Accuracy on testing set is 81%.  
- Feature importances show that ELEV, BURN_AREA, DRYBIO_AG, HT_pre_burn, DIA, YRS_since_burn are the most common features in the decision forest.  With num_burns and cull_pre_burn having much less importance.  
- Thinking about predicting DIA or HT post_burn and comparing to expected growth rates using a linear model. After adding tree species to the model.  
- Might add tree species to the model- seems like it would help.  



