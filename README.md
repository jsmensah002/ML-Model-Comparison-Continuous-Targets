Project Goal:
- Compare the performance of three machine learning models: Linear Regression (LR), Support Vector Regression (SVR), and Random Regressor (RFR) for predicting a continuous outcome. The dataset used focuses on profitability prediction.

Method:
- Built and trained three separate models (LR, SVR, RFR) to predict profitability.
- Compared model performance using relevant metrics, highlighting accuracy, stability, and suitability for the dataset.

Linear Regression Results (with a balanced class weight):
- R^2 (full dataset) = 0.6372
- R^2 (Trained 80% of the dataset) = 0.6388
- R^2 (Tested 20% of the dataset) = 0.6312
- Profit prediction = 43,139.58

Support Vector Regression Results:
- R^2 (full dataset) = -0.1233
- R^2 (Trained 80% of the dataset) = -0.1210
- R^2 (Tested 20% of the dataset) = -0.1328
- Profit prediction = 9,242.26

Random Forest Regressor Results:
- R^2 (full dataset) = 0.9843
- R^2 (Trained 80% of the dataset) = 0.9934
- R^2 (Tested 20% of the dataset) = 0.9539
- Profit prediction = 63,006.07

Key Insight:
- Based on the test performance, the Random Forest Regressor model achieved the highest test score AND showed no signs of overfitting, making it the most reliable model for this dataset. 

Conclusion:
- There is no universally preferred machine learning model. Model performance is data-dependent, and the most suitable model is determined by the characteristics of the dataset.
- The best model for a dataset is the one that achieves the highest test score while showing no signs of overfitting.
