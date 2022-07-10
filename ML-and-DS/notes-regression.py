
#---------------------------------------------------------------------------Simple-linear-regression
#___________________________________________________________________________________________________

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
#___________________________________________________________________________________________________

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


#-------------------------------------------------------------------------Regression-plot-in-Seaborn
#___________________________________________________________________________________________________

import seaborn as sns

plt.figure(figsize = (12, 10))  #figsize = (width, height); optional line
sns.regplot(x = 'independent_variable', y = 'dependent_variable', data = <dataframe>)
plt.ylim(0,)

#---------------------------------------------------------------------------Residual-plot-in-Seaborn
#___________________________________________________________________________________________________

import seaborn as sns

sns.residplot(df['independent'], df['dependent'])

#-----------------------------------------------------------------------Distribution-plot-in-Seaborn
#___________________________________________________________________________________________________

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


