#REGRESSION_________________________________________________________________________________________

#---------------------------------------------------------------------------Simple-linear-regression

# Refer to one independent variable to make a prediction.

# 1). Import linear model from scikit-learn
from sklearn.linear_model import LinearRegression

# 2). Create a linear regression object using the constructor
lm = LinearRegression()

# 3). Define variables: predictor (X) and target (Y)
X = df[['predictor']]
Y = df['target']

# 4). Train the mode to obtain parameters b0, b1
lm.fit(X, Y)

# 5). Obtain a prediction
Yhat = lm.predict(X)

# Other:
lm.intercept_  # view the intercept (b0)
lm.coef_  # view the slope (b1)


#-------------------------------------------------------------------------Multiple-linear-regression

# Refer to several independent variables to make a prediction.

# 1). Import linear model from scikit-learn
from sklearn.linear_model import LinearRegression

# 2). Create a linear regression object using the constructor
lm = LinearRegression()

# 3). Store predictor variables
X = df[['pred_01', 'pred_02', 'pred_03', 'pred_04']]
Y = df['target']

# 4). Train the mode to obtain parameters b0, b1
lm.fit(X, Y)

# 5). Obtain a prediction
Yhat = lm.predict(X)

# Other:
lm.intercept_  # view the intercept (b0)
lm.coef_  # view the coefficients (b1, b2, b3, b4)


#------------------------------------------------------------------------------Polynomial-regression

f = np.polyfit(x, y, 3)  #third order polynomial regression
p = np.poly1d(f)  #model base

#For PR with order higher than 3 we need to use scikit-learn's preprocessing library

from sklearn.preprocessing import PolynomialFeatures
pr = PolynomialFeatures(degree=2, include_bias=False)  #degree of 2 used for simplicity
x_polly = pr.fit_transform(x[['var1', 'var2']])

#Example
x1, x2 = 1, 2
pr = PolynomialFeatures(degree=2, include_bias=False)
pr.fit_transform([[x1, x2]])

#output: x1, x2, x1x2, x1^2, x2^2


#--------------------------------------------Normalize-using-preprocessing-library-from-scikit-learn

from sklearn.preprocessing import StandardScaler

SCALE = StandardScale()
SCALE.fit(x_data[['var1', 'var2']])

x_scale = SCALE.transform(x_data[['var_1', 'var_2']])  #transforms data into a new dataframe



#MODEL EVALUATION USING VISUALIZATION_______________________________________________________________

#-------------------------------------------------------------------------Regression-plot-in-Seaborn

import seaborn as sns

plt.figure(figsize = (12, 10))  #figsize = (width, height); optional line
sns.regplot(x = 'independent_variable', y = 'dependent_variable', data = <dataframe>)
plt.ylim(0,)


#---------------------------------------------------------------------------Residual-plot-in-Seaborn

import seaborn as sns

sns.residplot(df['independent'], df['dependent'])


#-----------------------------------------------------------------------Distribution-plot-in-Seaborn

import seaborn as sns

plt.figure(figsize = (width, height))
ax1 = sns.distplot(df['dependent'], hist=False, color='r', label='Actual values')
sns.distplot(Yhat, hist=False, color='b', label='Fitted values', ax=ax1)
#of course Yhat needs to be created first

plt.title('title')
plt.xlabel('label')
plt.ylabel('label')

plt.show()
plt.close()


#------------------------------------------------------------------------------------Polynomial-plot

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
    
    

#NUMERICAL MODEL EVALUATION_________________________________________________________________________

#--------------------------------------------------------------------Generating-a-sequence-of-values

import numpy as np

new_input = np.arange(1, 101, 1).reshape(-1, 1)  #generating values for a model
yhat = lm.predict(new_input)

#----------------------------------------------------------------------------------Mean-Square-Error

from sklearn.metrics import mean_squared_error
mean_squared_error(df['target'], Yhat)


#------------------------------------------------------------------------------------------------R^2

x = df[['predictor']]  #single predictor or multiple predictors
y = df['target']]

lm.fit(x, y)
lm.score(x, y)
