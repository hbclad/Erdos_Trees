## Survive or Thrive: Predicting Tree Health Following Forest Fires in Washington State:
### Research Question: 
Can we predict future forest long-term health following a fire given soil make-up/quality and historical forest health? Project Plan: We plan to investigate if we can can predict forest regeneration via overall tree health and soil-makeup data following a forest fire. We plan to investigate geographical areas in the United States where major fires are present, such as Washington, Oregon, & Idaho.

### Stakeholders:
Forestry service, disaster mitigation groups, commercial logging, environmentalists

### KPIs:
Comparing our predicted tree diameter/height/crown health vs actual historical data after fires


### Datasets:

FIA Datamart Washington data (maybe other states too?): https://research.fs.usda.gov/products/dataandtools/tools/fia-datamart

NOAA historical fire data: https://www.ncei.noaa.gov/products/paleoclimatology/fire-history

(If needed) NIFC historical fire data: https://data-nifc.opendata.arcgis.com/search?tags=historic_wildlandfire_opendata%2CCategory

USDA Research Data Archive - fire recovery study in Maine  

### Model Selection/Machine Learning Process:  
*What choice of model/regression type would we use to process this?* It's unlikely that a linear regression could be useful, but not fully accurate on predictive learning. Classification would be difficult unless we developed a ground truth classifcation for healthy, unhealthy, and in-between and classifed on a numerical or similar value. Given the nature of our data, a Time Series approach wouldn't be useful as our data isn't chaning in time.. UNLESS we determine some sort of function in time for regenration, then a time-series predeiction would be a useful metric. To fully establish our model selection and ML process we need to get the data hammered out and selected. Though my worries still stand that combining datasets can result in widly wrong/inaccurate data and thus the rest of our project.  
