import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, model_selection

'''
Load the diabetes dataset from scikit-learn.

Split the data into training and testing sets (70% train, 30% test).

Create a Linear Regression model.

Train the model using the training data.

Make predictions on the test data.

Plot the test data points (scatter plot).

Plot the regression line on the same graph.

Add appropriate labels and a title.

'''
data=datasets.load_diabetes(as_frame=True)
print(data.feature_names)
X,y=datasets.load_diabetes(return_X_y=True)
print(X.shape)
print(y.shape)
#print(X.feature_names)
print(X[0])
#print(y)

print("*************************************************")
X = X[:, 2]
#print(X)

print("*************************************************")
X = X.reshape((-1,1))
#print(X)
print("*************************************************")
# Split into training and testing sets
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.33)


# Create a linear regression model
model = linear_model.LinearRegression()

# Train the model
model.fit(X_train, y_train)#model.fit() is a function you'll see in many ML libraries such as TensorFlow


# Make predictions
y_pred = model.predict(X_test)


plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Scaled BMIs')
plt.ylabel('Disease Progression')
plt.title('A Graph Plot Showing Diabetes Progression Against BMI')
plt.show()