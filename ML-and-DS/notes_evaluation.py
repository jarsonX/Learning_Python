#MODEL_EVALUATION_USING_VISUALIZATION_______________________________________________________________

#-Regression-plot-in-Seaborn------------------------------------------------------------------------

import seaborn as sns

plt.figure(figsize = (12, 10))  #figsize = (width, height); optional line
sns.regplot(x = 'independent_variable', y = 'dependent_variable', data = <dataframe>)
plt.ylim(0,)

#-Residual-plot-in-Seaborn--------------------------------------------------------------------------

import seaborn as sns

sns.residplot(df['independent'], df['dependent'])

#-Distribution-plot-in-Seaborn----------------------------------------------------------------------

import seaborn as sns

plt.figure(figsize = (width, height))
ax1 = sns.distplot(df['dependent'], hist=False, color='r', label='Actual values')
#ax2 = ... [optional]
sns.distplot(Yhat, hist=False, color='b', label='Fitted values', ax=ax1)
#of course Yhat needs to be created first

plt.title('title')
plt.xlabel('label')
plt.ylabel('label')

plt.show()
plt.close()

#-Polynomial-plot-----------------------------------------------------------------------------------

def PlotPolly(model, independent_variable, dependent_variabble, Name):
    x_new = np.linspace(15, 55, 100)
    y_new = model(x_new)

    plt.plot(independent_variable, dependent_variabble, '.', x_new, y_new, '-')
    plt.title('Polynomial Fit with Matplotlib for Price ~ Length')
    ax = plt.gca()
    ax.set_facecolor((0.898, 0.898, 0.898))
    fig = plt.gcf()
    plt.xlabel(Name)
    plt.ylabel('label')

    plt.show()
    plt.close()
 

#NUMERICAL_MODEL_EVALUATION_________________________________________________________________________

#-Generating-a-sequence-of-values-------------------------------------------------------------------

import numpy as np

new_input = np.arange(1, 101, 1).reshape(-1, 1)  #generating values for a model
yhat = lm.predict(new_input)

#-Mean-Square-Error---------------------------------------------------------------------------------

from sklearn.metrics import mean_squared_error
mean_squared_error(df['target'], Yhat)

#-R^2-----------------------------------------------------------------------------------------------

x = df[['predictor']]  #single predictor or multiple predictors
y = df['target']]

lm.fit(x, y)
lm.score(x, y)

#-R^2-and-polynomial-with-different-orders-----------------------------------------------------------

# Calculates R^2 for different orders allowing to choose the best fit.

Rsqu_test = []
order = [1, 2, 3, 4]

for n in order:
    pr = PolynomialFeatures(degree=n)
    
    # Transform training and testing data into polynomials
    x_train_pr = pr.fit_transform(x_train[['var_1']])
    x_test_pr = pr.fit_transform((x_test[['var_1']])
                                 
    lr.fit(x_train_pr, y_train)  # fit the regression model
    
    Rsqu_test.append(lr.score(x_test_pr, y_test))  # calculate R^2 and store it                             

# It is helpful to plot it:

plt.plot(order, Rsqu_test)
plt.xlabel('order')
plt.ylabel('R^2')
plt.title('R^2 using test data')
plt.text(3, 0.75, 'Maximum R^2')                                 

                                 
#_ADVANCED_MODEL_EVALUATION_________________________________________________________________________

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

scores = cross_val_score(lr, x_data, y_data, cv=3)  #'scoring' is optional (default R^2)

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




