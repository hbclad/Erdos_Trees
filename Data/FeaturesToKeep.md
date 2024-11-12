## From TREE
#### Results we are predicting:
STATUSCD - nonmeasured, alive, dead, or removed by humans <br>
CULL - extent of damage/deformation

#### Main predictors:

DIA - diameter <br>
HT - height <br>
CULL - (existing) extent of damage/deformation <br>
DRYBIO_AG - oven-dry biomass aboveground <br>
CR - compacted crown ratio: percent of bole supporting healthy foliage <br>
CCLCD - crown class code: 1-5, where 1s are taller than all surroundings and get lots of light, and 5s are shorter than surroundings and get no direct light <br>
CDENCD - crown density code: percent of visibility blocked by foliage <br>
EPIPHYTE_PNWRS - extent of epiphytes (e.g. ivy?) on the tree, rated 0-6. Could make it more likely to burn?

#### Existing damage indicators:

DAMLOC1-3, DAMTYP1-3 - mostly about what part of the tree is damaged. 0 is none, 1-9 are specific parts in order from root to foliage. Type codes are pretty varied but no info on what caused the damage. <br>
DAMSEV1-3 - percentage of THAT PART OF THE TREE affected by associated damage. Can make null values into zeros to use this feature <br>
DAMAGE_AGENT_CD1-3 - not very full but can indicate fire-caused damage (code 30000) <br>
DMG_AGENT1_CD_PNWRS - and agent 2 and 3, same as above. Fire is code 92, and drought is 85 <br>
SEVERITY1_CD_PNWRS - and 2 and 3, severity of associated damage. (the A and B features are only about bugs). These are specific to each agent code and are not "balanced" between damage types. For both fire and drought, codes are 1 and 2, with 1 being less than 20% of crown damaged and 2 being more than 20% or any bole damage.

#### Checking if our results make sense:

AGENTCD - cause of death (for dead trees only), code 30 is fire <br>
MORTYR - year of death, estimated <br>
RECONCILECD - can contain reasons a tree was not remeasured


## From PLOT:

WATERCD - 59% full, numeric codes we would need to one-hot encode. permanent water vs temporary or no water <br>
ELEV - full


## Construct new columns:

Time since (most recent) fire <br>
Number of burns between observations <br>
