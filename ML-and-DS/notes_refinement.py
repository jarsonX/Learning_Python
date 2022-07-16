#_RIDGE_REGRESSION__________________________________________________________________________________

# A regression that is employed in a multiple regression model when multicollinearity occurs. Ridge
# regression can be used to regularize and reduce the standard errors to avoid over-fitting.

# It is very common with polynomial regression. For higher orders of polynomial, a magnitude tends
# to be very large. Ridge regression enables to control it by the usage of alpha hyper-parameter. 
# As alpha increases, the parameters get smaller. However, the main problem is to set the appropriate
# value for alpha.

#-Finding-alpha--------------------------------------------------------------------------------------

# 1. Split the dataset (train, predict).
# 2. Start with a small value of alpha.
# 3. Train the model.
# 4. Make a prediction.
# 5. Calculate R^2 and store the value. Note that other metrics can be used, e.g. MSE.
# REPEAT for a larger value of alpha.
# FINALLY select the value of alpha that maximizes R^2.

#-Making-prediction-using-ridge-regression-----------------------------------------------------------

from sklearn.linear_model import Ridge

RidgeModel = Ridge(alpha=0.1)
RidgeModel.fit(X, Y)

Yhat = RidgeModel.predict(X)

#_GRID_SEARCH_______________________________________________________________________________________
