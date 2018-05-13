# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""



from sklearn.linear_model import LinearRegression

lin_reg=LinearRegression()

lin_reg.fit(X, y)


from sklearn.preprocessing import PolynomialFeatures
poly_reg= PolynomialFeatures(degree=4)
x_poly=poly_reg.fit_transform(X)
poly_reg.fit(x_poly, y)
lin_reg2=LinearRegression()
lin_reg2.fit(x_poly, y)

#visualising the linear regession result
plt.scatter(X,y, color='red')
plt.plot(X, lin_reg.predict(X), color="blue")
plt.title("Truth or Bluff (Linear Regression)")
plt.xlabel('Position level')
plt.ylabel("Salary")
plt.show()


#visualising the polynimal linear regession result
x_grid=np.arange(min(X), max(X),0.1)
x_grid=x_grid.reshape((len(x_grid),1))

plt.scatter(X,y, color='red')
plt.plot(x_grid, lin_reg2.predict(poly_reg.fit_transform(x_grid)), color='blue')
plt.title("Truth or Bluff (Polynomial Regression)")
plt.xlabel('Position level')
plt.ylabel("Salary")
plt.show()


# Predicting a new result with linear regression
lin_reg.predict(6.5)

#Predicting a new result with Polynomial resgression
lin_reg2.predict(poly_reg.fit_transform(6.5))


