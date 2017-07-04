## DOTA 2 match outcome prediction

This project attempts to predict the outcome of Defense of the Ancients 2 using match specific statistics.
The performance of each team as a whole was evaluated and then the differences between team performances were assessed.
This difference was used accross 9 different features to predict which team would win. A model was created for every combination
of these 9 features to compare predictive power of different feature combinations. Total gold spent and percent of gold spent
had the highest predictive power with score of approximately 98% accuracy when a Random Forest Classifier (RFC) was fit over a
training set with just these features. An interactive dashboard was created to allow users to explore the predictive
power of RFCs fit over every feature combination. This dashboard allows to select on and off individual features. For 
consistency and interpretability a single model classifier type was used throughout when ended up being 511 different 
feature combinations. To account for the diversity in feature spaces accross combinations Random Forest Classifier was 
chosen for all models. This allowed for a balance of interpretability, accuracy, and speed over a diverse set of combinations each with unique model requirements.  

## Preliminary EDA

Prior to running the final models, it was important to assess if there were any advantages provided by hero selection in DOTA 2.
It was predicted that a model using only team make up would have little predictive power, assuming that the game was well balanced. 
A Random Forest Classifier was fit over a dataframe of 50,000 matches looking only at which team won and which heroes were on each team.
The model demonstrated no predictive power, prefering a max depth of 1 and predicting the same team slot would be victorious for every case. 

## DATA

The data used for this project can be found [here](https://www.kaggle.com/devinanzelmo/dota-2-matches, "kaggle dota2") on kaggle. 
The match, teamfight_players, and players csvs were used with information on 50,000 DotA 2 matches. Of these 50,000 just over 40,000 were used;
 games in which a player left early/disconnected and unranked games were dropped for consistency's sake.  The features used for modeling were: 
 kills, environmental Deaths (Deaths - opposing team's kills), gold spent, percent of total gold spent, teamfight participation, 
 healing, experience earn rate, end level, assist rate.

## Model

511 different models were created using a gridsearchcv with a 5x stratified shuffle split, a max depth range of 5, 10, 15, and 20,
a number of estimators range of 50, 100, 500, and 1000. Best parameters were then stored in a local file for future reference and 
accuracy, recall, precision, and f1 scores were stored for visualiaztion.

## Visualization

The visualization dashboard consists of a horizontal bar chart which generates the score associated with the currently selected features, 
a clickable series of 10 buttons, one for each feature and a select all button. This allows users to investigate the performance of specific 
features combinations. This type of visual representation can be useful for exploring options when it is costly to acquire certain features. 
This way clients/employers could look at the difference between multiple combinations without having to change pages and without 
having to look at a predetermined list of combinations. Underneath this part of the visualization is a vertical bar chart with the model 
performance scores for models that only used a single feature for prediction. These features are in the same order as their selectable 
checkboxes in the former part of the visualization. Color coding for each scoring type is consitent for easy readability.  
## IPython Notebooks

The Main Ipython notebook for this file is DOTA_2_Modelling.ipynb, the hero selection inspection can be found in Preliminary_eda.ipynb and the visualizations can be found in the viz folder. The Kills_and_Victor ipython notebook has secondary eda and confusion matrix plotting for kills and environmental deaths mapped to victory.
