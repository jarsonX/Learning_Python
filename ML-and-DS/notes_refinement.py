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

# See GRID SEARCH below for efficient method of doing so.

#-Making-prediction-using-ridge-regression-----------------------------------------------------------

from sklearn.linear_model import Ridge

RidgeModel = Ridge(alpha=0.1)
RidgeModel.fit(x_train, y_train)  # subsets need to be created with train_test_split() first
RidgeModel.score(x_test, y_test)  # calculate R^2

Yhat = RidgeModel.predict(X)

#_GRID_SEARCH_______________________________________________________________________________________

# A time-efficient tuning technique that exhaustively computes the optimum values of hyperparameters.

# 1. Split the dataset into thre parts:
#     - training set
#     - validation set
#     - test set
# 2. Train the model for different hyperparameters and different values.
# 3. Use MSE or R^2 for each model.
# 4. Select the hyperparameters that minimizes MSE or maximizes R^2 on the validation set.
# 5. Test model performance using the test data.

from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV

parameters = [{'alpha': [0.001, 0.1, 1, 10, 100, 1000]}, 'normalize'=[True, False]]

RR = Rdige()

Grid1 = GridSearchCV(RR, parameters, cv=4)  #cv is the number of folds; we use R^2 by default
Grid1.fit(x_data[['var_1', 'var_2', 'var_3', 'var_4']], y_data)
Grid1.best_estimator_

scores = Grid1.cv_results_
scores['mean_test_score']

for param, mean_val, mean_test in zip(scores['params'], scores['mean_test_score'], \
                                      scores['mean_train_score']):
  print(param, "R^2 on test data:", mean_val, "R^2 on train data:", mean_test)
