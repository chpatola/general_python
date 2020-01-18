import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

#Split X, y data in train, val and test & check number of instances in each group
def data_split3(X,y,x_percent=0.8):
    train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0,train_size=x_percent)
    val_X, test_X, val_y,test_y = train_test_split(val_X, val_y, random_state = 0,train_size=0.5)
    print("Train number of rows: %d"%(train_X.shape[0]))
    print("\nVal  number of rows: %d"%(val_X.shape[0]))
    print("\nTest  number of rows: %d"%(test_X.shape[0]))
    print("\n")

    return train_X, val_X, test_X, train_y, val_y, test_y

#Linear regression on X and y & info on result
def linreg_info(X,y):
    X2 = sm.add_constant(X)
    est = sm.OLS(y, X2)
    est2 = est.fit()
    print(est2.summary())
    return est2

#RandomforestRegressor on X, y & print mean absolute error
def forest_reg_eval(X,y):
    forest = RandomForestRegressor(random_state = 0)
    forest.fit(X,y)
    y_pred = forest.predict(X)
    print(mean_absolute_error(y, y_pred)) 
    return forest

#Use defined Grid model on X,y, split in train and validation & print best params + score (defined in grid model)
def grid_eval(X,y,gridmodel=LinearRegression(),test_size=0.3):
    train_Xgrid, val_Xgrid, train_ygrid, val_ygrid = train_test_split(
    X, y, test_size=test_size, random_state=1)

    gridmodel.fit(train_Xgrid, train_ygrid)
    print('Best params: ', gridmodel.best_params_)
    print('Score: ', (gridmodel.best_score_*-1))  


