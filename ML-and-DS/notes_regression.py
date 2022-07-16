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
