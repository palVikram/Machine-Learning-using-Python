# -*- coding: utf-8 -*-

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('../Position_Salaries.csv')

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(X,y)


#Predicting a new result with Polynomial resgression
y_predict=regressor.predict(6.5)

plt.scatter(X,y, color='red')
plt.plot(X, regressor.predict(X), color='blue')
plt.title("Truth or Bluff (Polynomial Regression)")
plt.xlabel('Position level')
plt.ylabel("Salary")
plt.show()


#visualising the polynimal linear regession result(smoother and bright result)
x_grid=np.arange(min(X), max(X),0.1)
x_grid=x_grid.reshape((len(x_grid),1))

plt.scatter(X,y, color='red')
plt.plot(X, regressor.predict(X), color='blue')
plt.title("Truth or Bluff (Decison Tree Regression)")
plt.xlabel('Position level')
plt.ylabel("Salary")
plt.show()





