import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, model_selection

'''
The built-in diabetes dataset includes 442 samples of data around diabetes, 
with 10 feature variables, some of which include:

age: age in years
bmi: body mass index
bp: average blood pressure
s1 tc: T-Cells (a type of white blood cells)

This dataset includes the concept of 'sex' as a feature variable important to 
research around diabetes. Many medical datasets include this type of binary 
classification. Think a bit about how categorizations such as this might exclude 
certain parts of a population from treatments.


'''
# Load the diabetes dataset
X, y = datasets.load_diabetes(return_X_y=True)
print(X.shape)
print(X[0])
'''
Think a bit about the relationship between the data and the regression target. 
Linear regression predicts relationships between feature X and target variable y. 
Can you find the target for the diabetes dataset in the documentation? 
What is this dataset demonstrating, given that target?
'''
'''
Next, select a portion of this dataset to plot by selecting the 3rd column of the dataset. 
You can do this by using the : operator to select all rows, and then selecting the 3rd column 
using the index (2). You can also reshape the data to be a 2D array - as required for plotting - 
by using reshape(n_rows, n_columns). If one of the parameter is -1, the corresponding dimension 
is calculated automatically.
'''
X = X[:, 2]
X = X.reshape((-1,1))
#At any time, print out the data to check its shape.

'''
Now that you have data ready to be plotted, you can see if a machine can help determine 
a logical split between the numbers in this dataset. To do this, you need to split both 
the data (X) and the target (y) into test and training sets. 
Scikit-learn has a straightforward way to do this; you can split your test data at 
a given point.
'''
# Split into training and testing sets
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.33)

'''
Now you are ready to train your model! Load up the linear regression model and 
train it with your X and y training sets using model.fit():
'''
# Create a linear regression model
model = linear_model.LinearRegression()

# Train the model
model.fit(X_train, y_train)#model.fit() is a function you'll see in many ML libraries such as TensorFlow

'''
Then, create a prediction using test data, using the function predict(). 
This will be used to draw the line between data groups
'''
# Make predictions
y_pred = model.predict(X_test)

'''
Now it's time to show the data in a plot. Matplotlib is a very useful tool for this task. 
Create a scatterplot of all the X and y test data, and use the prediction to draw a line 
in the most appropriate place, between the model's data groupings.
'''
# Plot the results
plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Scaled BMIs')
plt.ylabel('Disease Progression')
plt.title('A Graph Plot Showing Diabetes Progression Against BMI')
plt.show()
'''
Think a bit about what's going on here. A straight line is running through many small 
dots of data, but what is it doing exactly? Can you see how you should be able to 
use this line to predict where a new, unseen data point should fit in relationship 
to the plot's y axis? Try to put into words the practical use of this model.

'''

'''
Plot a different variable from this dataset. Hint: edit this line: X = X[:,2]. 
Given this dataset's target, what are you able to discover about the progression of 
diabetes as a disease?
'''
'''
How would you describe the relationship between BMI and diabetes progression in 
this dataset?
If you were a doctor, would you use this model to make treatment decisions? 
Why or why not?
What other features might improve this model?
'''