import numpy as np
from sklearn.linear_model import LinearRegression

X = np.linspace(0, 10, 100)
y_true = 2 * X - 10 
y = y_true + 5 * np.random.randn(*X.shape)
X = X[:, np.newaxis]

regr = LinearRegression()
regr.fit(X, y)
y_pred = regr.predict(X)
