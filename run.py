#testing

import datasets

X,Y = datasets.load_linear_example1()
"""
print(X)
print(X[0])
print(Y)
"""

# ver1

import regression

model = regression.LinearRegression()
"""
print(model.x)
"""

# ver2

import importlib

importlib.reload(regression)

"""
print(model.fit(X, Y))
print(model.theta)
"""

# ver3

"""
print (model.fit(X, Y))
print (model.predict(X))
"""

# ver4

print(model.fit(X, Y))
print(model.score(X, Y))
