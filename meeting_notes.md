## 11/05/24 Meeting Notes

### Items Discussed:
+ Since indivdual tree data greatly reduces dataset size, consider predicting the density of trees using `TPA_UNADJ` feature (trees per acre, unadjusted).  
    + If the forest is healthy at some point then burns, so we can predict the return to that health statistic. 
    + Could look at maximum health density via the carrying capacity via trees that haven't burned. Can also apply a logistical model to make predictions on healthy forest continuation.  
+ Examine how long between forest burns, i.e time between burns and what health looks like in that time.  
+ With regard to carrying capacity as an idicator of health given the `TPA_UNADJ` feature, it can be valuable to have data that is several years apart that didn't burn as a control. This shows us how a healthly forest contiunes along.   
    + Would be useful to one-hot encode plots/time combonations that did or did not burn.  
        + This filtering could be VERY easy in SQL. Would be worth exploring in SQL and then saving as .csv and reading back into Python.  

### Tasks to be Done:
+ One hot encoding (as described above). Want to do this on plots and time, multiple alignments.  
+ Written model approach -- what are we looking at (carrying capacity as a function of density) and how are we attempting to model it?  
+ design preliminary models, a pipeline could be a great way of looking at multiple models quickly. *this falls to the bottom in regards to priority until we get data completely clean and pre-processed.*  
+ Find and describe Key Visuals (see Alec's message in Slack). This relates heavily to all the EDA we have already done.  
+ Clean up the EDA in the Github to 1-3 presentable .ipynbs.
+ Identify which attriubtes in the fires.csv we want to pull through into the data. Potentially the IRWIN #? What makes each unique other than a name.  

### Questions: 
**@ Henry:** In compiling the PLOT_FIRE_GIS dataset, why did you use incident name? Did you consider object ID or some other unique identifier? 



## 11/11/24 Meeting Notes

### Items Discussed:
+ *Best Features for Predicting:* diameter (at breast, which is at least 4ft off the ground), height, above ground biomass, cull & previous cull.
    + Would predict these features on indivdual trees rather than TPA since that seemed to just be a code rather than a value.
+ Trees measured more than once is ~12.6% of the whole dataset (assuming this is in fire-sandwhiches set).
    + Approx 20868 trees now compose working dataset.  
    + Approx 14% of trees in fires were only measured once. This is a consideration/statistic that should be addressed in a final report/presentation.
    + How many trees in this set have had > 2 measurements?
    + How many trees in this set are past due, it's been longer than 10 years since a last measurement, for a remeasurement.
+ Potnetial predictors: need to consider time since the fire --> time between fires and first measurement.
    + Should also consider how to handle plots that have burned multiple times between measurement years. It was suggested that we throw those out or classify them differently since it would greatly affect a predictor.
+ **Features also discussed to be used:** consider the time since a fire and then create a time that is measure_year1 - fire - measureyear2 to understand growing time of each tree after fire. Could serve as another feature column.
    + can also consider the condition of each plot before and after fire. This would also be a interesting thing to value like 1, 2, or 3 based on plot condition.
    + Water: seperate perm from temporary from no water on plot => affects plot condition and tree re-growth. This would also be affected by elevation.

### Tasks:
+ Select features to predict on from literature/documentation -- Christina.
+ Construct list of ML models to throw at the dataset -- Open/Ella.
+ Investigate the water data -- Ella.
+ Investigate which plots have been measured how many times -- Allie/Henry.  

### Goals for after future Meeting:
Next meeting is 11am CT on Weds November 13. *Goal is to have a complete .csv file that all have access to and can start throwing ML models at*. 
