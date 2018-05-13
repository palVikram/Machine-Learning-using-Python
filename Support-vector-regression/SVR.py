# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('../Position_Salaries.csv')

X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)


from sklearn.svm import SVR
regressor=SVR(kernel='rbf')
regressor.fit(X,y)

#Predicting a new result with Polynomial resgression
y_predict=sc_y.inverse_transform(regressor.predict(sc_X.transform(np.array([[6.5]]))))



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
plt.plot(x_grid, regressor.predict((x_grid), color='blue'))
plt.title("Truth or Bluff (SVR Regression)")
plt.xlabel('Position level')
plt.ylabel("Salary")
plt.show()





