# Forest Fire and Bio-Diversity Project Notes:
**The purpose of this living document is to have a place to put all thoughts and outside research from each group member in one place.** 

### Information About Previous Related Projects:
The purpose of this section is to explore and summarize previous Erdös and Academic projects that may relate to our proposed research question.  

**Forest Fire Prediction** *Fall 2023, Team 36* Their project surrounds the data involved in what weather patterns cause forest fires and given a specific weather pattern can we predict if a fire could/will ignite. They used the natural factors such as rainfall, relative humidity, and temperature as primary indicators of if a fire will or will not ignite. 

**Predicting land cover using GEDI-L2A tree canopy data for New York State** *May-Summer 2024, Team 41*. The aim of this project was find a correlation between tree canopy cover and tree height -- which could indicate tree health. Only link to wildfires was where this project could be applicable, such as wildfire researchers could use this to understand tree health and where wildfires may or may not spread/ignite. (Fun Fact: Ella went to undergrad with one of the people that worked on this project). 

**Predicting Forest Cover Types and Visualizing Data** *Team 71, Fall 2023* The goal of this project was to, given a current map of forest data, can we predict future tree covers and what is the minimal amount of data we need to predict this. They used a topological based algorithm, which is actually really interesting.
Note: This project is likely most similar to what we could be doing, but I think we've veered in a slightly different direction. Please correct me (Ella) if I'm wrong. 

**Predicting Wildfire Spread** *Team 78, Fall 2022* The goal of this project was to predict where wildfires will spread once started using features like windspeed/wind direction/previous fire perimeter and minimum temperature. They used a convolutional neural network. 


### Our Project
**Research Question:** Can we predict how a forest regenerates following a fire given the soil make up and previous bio-diversity?   
*Edit: Can we predict future forest long-term health following a fire given soil make-up/quality and historical forest health?*
**Project Plan:** We plan to investigate if we can can predict forest regeneration via the bio-diversity data in trees (potentially also insects/birds but potentially trees might be enough -- OR if we could find some biodiversity index, mathematically?) follwoing a forest fire. We plan to investigate geographical areas in the United States where major fires are present, such as Washington, Oregon, & Idaho. 

**Links to Data Sets**:
"Mapping recovery in the Thomas Fire Scar": https://www.gbif.org/dataset/e09a772e-f755-4738-a2d4-f84db79971b2
This seems relevant, although it's highly specific.

Another potential dataset: Fire and tree mortality database https://www.fs.usda.gov/rds/archive/catalog/RDS-2020-0001-2

Highly specific to two regions in Washington but with alot of good data like density of different species X years after a fire.  https://www.fs.usda.gov/rds/archive/catalog/RDS-2020-0079


"Wildfire severity and postfire salvage harvest effects on long-term forest regeneration": Field attributes and satellite data for "How vegetation recovery and fuel conditions in past fires influences fuels and future fire management in five western U.S. ecosystems" (2nd Edition).  Looks at long term effects. https://www.fs.usda.gov/rds/archive/catalog/RDS-2019-0005-2

**General Observations/Notes**  
Everyone should give this a read and we may be able to use some the results for our project: https://www.mdpi.com/1999-4907/14/4/709.  
Here's what my thought had been, if we could find some sort of mathematical formula for an index of biodiversity in a given area, we could then compile data to understand that index and see how that index changes after a fire. This would encompass trees, wildlife, soil quality etc since the entire ecosystem relies on each of these things. The paper focuses primarily on forest ecosystems which would fit our project well.   

This (https://research.fs.usda.gov/sites/default/files/2024-07/wo-17827_forest_service_forest_ecosystem_health_indicators_508.pdf) is also worth a read from a stakeholders perspective in this project as well as forest health indicators. I think I've got an idea for our direction that I'll pitch in an edit to the research question/project plan section of this document. (-Ella)  
    Furthermore this document covers essantially what all of the data in the FIA Datamart is, where we're concerned is forest regenration following a fire, for which they don't have a ton of data. Much of the FIA project following regenration has been focused on the Midwest and Northeast regions of the United States where forest decimation has occured due to human and natural impacts, inlcuding but not limited to unsustainable mining and forestry practices, invasive species, human stated fires (mostly Midwest) etc (pages 20-21 cover this well). This can dictate where our project goes given that there is a TON of forestry data for WA and the PNW as well as soil data. Potentially building an indicator based on soil make up and forest health before a fire as a predictor of regenration after a fire could be interesting. With regard to soil, things such as dead fall (leaves, trees, other organic material) can affect the quality as organic matter adds nitrogen back into the soil, we can also look at water retention and the other variables they include in the FIA soil survey. I plan to also attempt to cross reference with USGS if I can find a similar range. While I think bio-diversity is an excellent indicator of forest health, it may be too broad and require too much data mining to be productive in this project.  
    More on FIA: https://research.fs.usda.gov/understory/forest-inventory-and-analysis-database-user-guide-nfi. This is the user guide to the dataset and should be used in conjunction with the dataset. It outlines the name and use of each varibale. It's also 1000+ pages. Whoop. This is a glossary for some of the terms used :https://research.fs.usda.gov/understory/forest-inventory-and-analysis-glossary-standard-terminology.

While the following dataset (linked below) could take our project in a totally different direction, it could be really interesting.  
*Abstract:* This data publication contains overstory tree measurements, regeneration data, and permanent sample plot location information collected between 1952 and 2014 under the study plan: FS-NRS-07-08-01 "Study Plan: Silvicultural effects on composition, structure and growth of northern conifers in the Acadian Forest Region: Revision of the Compartment Management Study on the Penobscot Experimental Forest" (see Methodology citation section). Data are available in six data sets. 1) Overstory tree measurement data include tree species, condition code (e.g., merchantability status and cause of mortality, if applicable), and diameter at breast height (dbh), 1952 to 2014. 2) Regeneration data include tree seedling species, presence, and count by height class, 1964 to 2014. 3) Spatial location data include location of a subsample of trees, 2000 to 2014. 4) Height and crown measurement data include tree height, height to crown base, and crown radii for a subsample of trees, 2000 to 2014. 5) Understory vegetation data include percent cover by substrate and non-tree vegetation categories, 2000 to 2014. 6) Permanent plot location data include the geospatial coordinates for permanent sample plots.  
*Link:* https://www.fs.usda.gov/rds/archive/catalog/RDS-2012-0008-2

**Work Done Thus Far**  
This section outlines work done this far by each group member with a summary.  
In the "Data Analysis" folder of this repo, Henry has a doc called "DA.ipynb" wherein he includes the "WA_PLOT" data from the FIA Datamart. The NB contains 3 figures from the "WA_PLOT" dataset. These figures depict where FIA Plots of studied land are. These plots are overlaid onto geographical maps of Washington and line up with the Cascade mountian and forest areas. They are given below, and would serve as our geographical area of interest. 
![alt text](https://github.com/hbclad/Erdos_trees/blob/main/figures/data_overlay1.png?raw=true)
This figure shows geographically on a rough outline of the west coast of the United States where the research plots that generate the data in "WA_PLOT" lie. 
![alt text](https://github.com/hbclad/Erdos_trees/blob/main/figures/data_overlay2.png?raw=true)
This figure shows geographically, where data was collected via remote sensing on a map of the state of WA. 
![alt text](https://github.com/hbclad/Erdos_trees/blob/main/figures/data_overlay3.png?raw=true)
This, while essantially the same as the previous, shows data where researchers collected plot data in the field. These are distinguhed via sampling method form in the dataset. 


Historical fire data here: https://www.ncei.noaa.gov/products/paleoclimatology/fire-history -- once they recover from the hurricane.

**FIA DataMart Abbreviation Helpful Names:**
+ CN == Sequence Number (reading number, each is unique to each table)  
+ PLOT == Plot # -- we could use this to link datasets together.  
+ PLT_CN == Plot Sequence # -- could maybe also be used to link data sets together.
+ RSCD == Region or Station code -- also useful in combining datasets and seeing if they're in the correct region.
+ SEVERITY1_CD_PNWRS == Severity of damage type 1 (there are also damage types 1, 1A, 1B, 2, 2A, 2B, & 3). We should find an understanding of what each of these damage types truly is. Could be a very useful metric.
+ SICOND == site index for condition.
+ SISP == site index species code.
+ SITETREE_TREE == site tree number, if we can link individual tree numbers this could be useful, but also take a TON of time and data processing. It may make more sense to consider the forest as a whole organism rather than individual trees.
+ SPCD == species code.
  













