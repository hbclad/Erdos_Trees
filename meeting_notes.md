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

