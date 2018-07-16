from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier

import numpy as np
import pandas as pd

def get_predictability(X, y, dtype='continuous'):
    """Returns scores for various models when given a dataframe and target set
    
    Arguments:
        X (dataframe)
        y (series)
        dtype (str): categorical or continuous
        
        Note: X and y must be equal in column length 
        
    Returns:
        None
    """   
    M = pd.concat([X, y], axis=1)
    fortrain = M.dropna()
    
    X_ft = fortrain.iloc[:,:-1]
    y_ft = fortrain.iloc[:,-1]
        
    X_train, X_test, y_train, y_test = train_test_split(X_ft, y_ft, test_size=0.1)
    
    # use mean as the prediction
    y_train_mean = y_train.mean()
    y_pred_mean = np.zeros(len(y_test))
    y_pred_mean.fill(y_train_mean)
    
    # use median as the prediction
    y_train_median = y_train.median()
    y_pred_median = np.zeros(len(y_test))
    y_pred_median.fill(y_train_median)

    # use mode as the prediction
    # zero index is required to return the first most common value
    y_train_mode = y_train.mode()[0]
    y_pred_mode = np.zeros(len(y_test))
    y_pred_mode.fill(y_train_mode)
    
    lm = LinearRegression()
    print("Fitting linear regression model")
    lm.fit(X_train, y_train)

    
    rf = RandomForestRegressor()
    print("Fitting random forest model")
    rf.fit(X_train, y_train)
    
    kN = KNeighborsRegressor()
    print("Fitting kNN model")
    kN.fit(X_train, y_train)
    
    mean_score = r2_score(y_test, y_pred_mean)
    median_score = r2_score(y_test, y_pred_median)
    mode_score = r2_score(y_test, y_pred_mode)
    
    lm_score = lm.score(X_test, y_test)
    rf_score = rf.score(X_test, y_test)
    kN_score = kN.score(X_test, y_test)
    
    names = ['mean', 'median', 'mode', 'LinearRegression', 'RandomForestRegressor', 'KNeighborsRegressor']
    scores = [mean_score, median_score, mode_score, lm_score, rf_score, kN_score]
    
    print([(names[idx], score) for idx, score in enumerate(scores)])