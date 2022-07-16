#--------------------------------------------------------------------Using-a-pipeline-in-scikit-learn

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

Input = [('scale', StandardScaler()), ('polynomial', PolynomialFeatures(degree=2, include_bias=False)) \
         ('mode', LinearRegression())]  #'name of the estimator model', model constructor

pipe = Pipeline(Input)
pipe.fit(df[['var1', 'var2', 'var3']], y)  #train the pipeline

yhat = pipe.predict(X[['var1', 'var2', 'var3']])  #produce a prediction
