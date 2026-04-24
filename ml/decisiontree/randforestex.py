import numpy as np
import pandas as pd


# Load and prepare Titanic data
titanic_train = pd.read_csv("D:\\prodapt2026MarApril\\ml\\decisiontree\\train.csv")    # Read the data
print(titanic_train.info())

# Impute median Age for NA Age values
new_age_var = np.where(titanic_train["Age"].isnull(), # Logical check
                       28,                       # Value if check is true
                       titanic_train["Age"])     # Value if check is false

titanic_train["Age"] = new_age_var 


from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

# Set the seed
np.random.seed(12)

# Initialize label encoder
label_encoder = preprocessing.LabelEncoder()

# Convert some variables to numeric
titanic_train["Sex"] = label_encoder.fit_transform(titanic_train["Sex"])

# Initialize the model
rf_model = RandomForestClassifier(n_estimators=1000, # Number of trees
                                  max_features=2,    # Num features considered
                                  oob_score=True)    # Use OOB scoring*

features = ["Sex","Pclass","SibSp","Age","Fare"]

# Train the model
rf_model.fit(X=titanic_train[features],
             y=titanic_train["Survived"])

print("OOB accuracy: ")
print(rf_model.oob_score_)


"""
Since random forest models involve building trees from random subsets or 
"bags" of data, model performance can be estimated by making predictions 
on the out-of-bag (OOB) samples instead of using cross validation. 
You can use cross validation on random forests, but OOB validation 
already provides a good estimate of performance and building several 
random forest models to conduct K-fold cross validation with random forest 
models can be computationally expensive.
"""
"""
The random forest classifier assigns an importance value to each feature 
used in training. Features with higher importance were more influential 
in creating the model, indicating a stronger association with the response 
variable. Let's check the feature importance for our random forest model:
"""
for feature, imp in zip(features, rf_model.feature_importances_):
    print(feature, imp)

"""
Feature importance can help identify useful features and eliminate features that don't contribute 
much to the model.

As a final exercise, let's use the random forest model to make predictions 
on the titanic test set and submit them to Kaggle to see how our actual 
generalization performance compares to the OOB estimate:
"""

# Load and prepare Titanic test data
titanic_test = pd.read_csv("D:\\prodapt2026MarApril\\ml\\decisiontree\\test.csv")

# Impute median Age for NA Age values
new_age_var = np.where(titanic_test["Age"].isnull(), # Logical check
                       28,                       # Value if check is true
                       titanic_test["Age"])     # Value if check is false

titanic_test["Age"] = new_age_var 

# Convert Sex variable to numeric
titanic_test["Sex"] = label_encoder.fit_transform(titanic_test["Sex"])

# Make predictions on the test set
test_preds = rf_model.predict(X=titanic_test[features])

# Create a dataframe of the predictions
submission = pd.DataFrame({
        "PassengerId": titanic_test["PassengerId"],
        "Survived": test_preds
    })

# Save the predictions to a CSV file
submission.to_csv("submission.csv", index=False)
"""
Upon submission, the random forest model achieves  an accuracy 
score of 0.74641, which is actually worse than the decision tree model 
and even the simple gender-based model. What gives? Is the model 
overfitting the training data? Did we choose bad variables and model 
parameters? Or perhaps our simplistic imputation of filling in missing 
age data using median ages is hurting our accuracy. Data analyses and 
predictive models often don't turn out how you expect, but even a "bad" 
result can give you insight into your problem and help you improve your 
analysis or model in a future iteration.

"""
#Create a confusion matrix
from sklearn.metrics import confusion_matrix

# Get predictions on the training data
train_preds = rf_model.predict(X=titanic_train[features])

# Create a confusion matrix
conf_matrix = confusion_matrix(y_true=titanic_train["Survived"],
                               y_pred=train_preds)

print(conf_matrix)


"""
Confusion Matrix
[[542   7]
 [ 12 330]]

True Negatives (TN): 542 - These are the instances where the model correctly predicted that the passenger did not survive.
False Positives (FP): 7 - These are the instances where the model incorrectly predicted that the passenger survived, but they actually did not.
False Negatives (FN): 12 - These are the instances where the model incorrectly predicted that the passenger did not survive, but they actually did.
True Positives (TP): 330 - These are the instances where the model correctly predicted that the passenger survived.
"""
print("************************************************************")

import matplotlib.pyplot as plt

plt.bar(x=features, height=rf_model.feature_importances_)
plt.show()