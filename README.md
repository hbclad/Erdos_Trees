# Erdos_Trees
# Thrive or Survive: Predicting the Health of Trees following Forest Fires in Washington 
A project by Henry Cladouhos, Allie Cruikshank, Christina Duffield, & Ella Palacios

## Overview
#### Motivation:
The motivation behind this project is to build a model that can accurately predict the survival and health of trees 
following a forest fire, given previous health data. We picked the state of Washington to begin developing the model 
due to its diverse boreal & arboreal ecosystems at varying elevations that fall victim to yearly forest fires. Preserving 
Washington forests is a passion of ours. 

#### Question:
Can we predict tree survival and health following a fire, using data about the tree’s past health and the fire severity?

#### Stakeholders: 
- Disaster Mitigation Groups
- Commercial Logging
- Forestry Researchers

#### KPI:
Accuracy of tree survival predictions post-fire when compared with actual historic outcomes

## File Organization
This Github is divided into three folders. They are described below in the general logical order that you should access them
to understand the project.

#### Data
The Data folder contains...
- `WA_PLOT`, `WA_TREE`, and `wa_lrg_fires`, raw files downloaded from our data sources (FIA datamart and NIFC). Note that the
`WA_TREE` file is too large to be stored on Github in its unzipped form.
- `TREES_FOR_US`, which is the TREE dataset augmented by geographic and temporal data from PLOT.
- `PLOT_GIS` and `PLOT_FIRES_GIS`, which Henry used in QGIS to intersect the datasets.
- `WA_PLOT_FIRE_PAIRS` and `DISSOLVED_FIRE_PLOT_PAIRS`, which contains the TREE dataset after filtering, with additional 
columns pulled in from both PLOT and the fire dataset. The "dissolved" file is the result of removing duplicate fire incidents.
- `final_dataset_construction`, which was used to merge `WA_PLOT` and `WA_TREE` into the `final_big_data` and 
`trimmed_data` files.
- `FeaturesToKeep.md`, which lists features from the TREE dataset that were viable (i.e. not mostly NaN) and/or relevant, 
along with a short description of the feature based on the FIA user guide description. These features are the ones out of 
`final_big_data` which we carried over into `trimmed_data`, which is the dataset loaded in most of our Models.

#### Early Data Analysis
This folder contains...
- `DBFconvert.py`, used for transforming a dbf file in the Data folder into a CSV for further use.
- `Filtering_Trees`, which we used to pare down the tree dataset to only those which had a fire occur between observations.
- `Tree_Species` and `TREES_EDA` which contain some exploratory work to understand our dataset.
- The `figures` folder, which has a few geographical views of the data.

#### Models
This folder contains...
- `data_loader` and `plot_split_loader`, two files containing functions used in other notebooks to load and split our data 
in the same way each time they are called. `plot_split_loader` was made in response to a concern about data contamination, 
and separates the trees into train and test data so that entire plots are kept together. This avoids data contamination 
between train and test sets, which would otherwise have trees with similar geographic features and similar outcomes simply
because they are physically very close to each other.
- `SVC`, `KNN`, `RandomForest`, and `LogisticRegression` notebooks, which walk through applying the named models to the 
plot-split data. These are updated from their old versions, which had data contamination issues as described above.
- `knn_health_quality`, which contains the beginnings of a model to predict tree health (not just survival) after a fire. This 
is a new direction that we did not have time to fully explore during the boot camp, but hope to continue working with going 
forward.
