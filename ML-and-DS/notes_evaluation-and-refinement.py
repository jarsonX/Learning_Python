#_MODEL_EVALUATION__________________________________________________________________________________

#-Training-testing-sets-----------------------------------------------------------------------------

# Splits data into random train and test subsets.

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test.split(x_data, y_data, test_size=0.3, random_state=0)

# x_data - features or independent variables,
# y_data - dataset target
# x_train, y_train - parts of available data as training set
# x_test, y_test - parts of available data as testing set
# test_size - percentage of the data for testing
# random_state - number generator used for random sampling

#-Cross-val-score-----------------------------------------------------------------------------------

# Using a lot of data for training gives us an accurate means of determining how well our model will
# perform in the real world. But the precision of the performance will be low, i.e. results from each
# experiment will be extremely different. On the other hand, if we use fewer data points to train the
# model, the accuracy of the generalization performance will be less, but the model will have good
# precision.

# Solution lies in cross-validation, one of the most common out-of-sample evaluation metrics. It
# enables more effective use of data. Each observaiton is used for both training and testing. The
# dataset is split into k equal groups called 'Folds'. Some are used for testing, some for training.
# This is repeated until each fold is used for both. At the end we use average results as the
# estimate of out-of-sample error. The evaluation metric depends on the model, e.g. R^2.

# cross_val_score() function performs multiple out-of-sample evaluations.

from sklearn.model_selection import cross_val_score

scores = cross_val_score(lr, x_data, y_data, cv=3)

# lr - the type of model we are using to do the cross validation (here: linear regression)
# x_data - the predictive variable
# y_data - the target variable
# cv - number of partitions

# The function returns an array of scores, one for each partition that was chosen as the testing set.
# The result can be averaged together to estimate out-of-sample R^2:

np.mean(scores)

#-Cross-val-predict---------------------------------------------------------------------------------

# Provides detailed information in respect of predicted values supplied by the model before R^2
# values are calculated.

from sklearn.model_selection import cross_val_predict
yhat = cross_val_predict(lr2e, x_data, y_data, cv=3)




