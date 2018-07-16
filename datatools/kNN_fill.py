from sklearn.model_selection import train_test_split
import pandas as pd

def kNN_fill(X, y, dtype='categorical'):
    """Returns y with missing values filled based on kNN
    
    Arguments:
        X (dataframe)
        y (series)
        dtype (str): categorical or continuous
        
        Note: X and y must be equal in column length and rows must 
        
    Returns:
        y_filled (series)
    """
    
    if len(y[y.isnull()]) == 0:
        raise ValueError('No missing values in y provided')    
    
    M = pd.concat([X, y], axis=1)
    fortrain = M.dropna()
    forpredict = M[y.isnull()]
    
    X_ft = fortrain.iloc[:,:-1]
    y_ft = fortrain.iloc[:,-1]
    
    X_fp = forpredict.iloc[:,:-1]
    
    X_train, X_test, y_train, y_test = train_test_split(X_ft, y_ft, test_size=0.2)
    
    if dtype == 'categorical':
        kNC = KNeighborsClassifier()
        kNC.fit(X_train, y_train)
        score = kNC.score(X_test, y_test)
        y_fp = kNC.predict(X_fp)
    elif dtype == 'continuous':
        kNR = KNeighborsRegressor()
        kNR.fit(X_train, y_train)
        score = kNR.score(X_test, y_test)
        y_fp = kNR.predict(X_fp)
    else:
        raise ValueError('dtype must be categorical or continuous')
    
    print(score)
    print(y_fp)
    
    y[y.isnull()] = y_fp
    
    # no return statement
    # the series set to y will be modified in-place