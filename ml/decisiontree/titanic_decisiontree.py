"""
Let's create the gender-based model on the Titanic training set using decision
trees in Python. First we'll load some libraries and preprocess the Titanic data:
"""
import numpy as np
import pandas as pd
import graphviz

# Load and prepare Titanic data
titanic_train = pd.read_csv("D:\\prodapt2026MarApril\\ml\\decisiontree\\archive\\titanic.csv")    # Read the data
print(titanic_train.info())
# Impute median Age for NA Age values
new_age_var = np.where(titanic_train["Age"].isnull(), # Logical check
                       28,                       # Value if check is true
                       titanic_train["Age"])     # Value if check is false
#print(new_age_var)

titanic_train["Age"] = new_age_var

"""
Next, we need to load and initialize scikit-learn's the decision tree model 
and then train the model using the sex variable:
"""
from sklearn import tree
from sklearn import preprocessing

# Initialize label encoder
label_encoder = preprocessing.LabelEncoder()

# Convert Sex variable to numeric
encoded_sex = label_encoder.fit_transform(titanic_train["Sex"])
#print(encoded_sex)
# Initialize model
tree_model = tree.DecisionTreeClassifier(max_depth=3)

# Train the model
tree_model.fit(X = pd.DataFrame(encoded_sex), 
               y = titanic_train["Survived"])

"""
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=None,
            max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, presort=False, random_state=None,
            splitter='best')
"""
"""
Note the list of default arguments included in the model above. 

Now let's view a visualization of the tree the model created. 
"""
import matplotlib.pyplot as plt

# Save tree
tree.plot_tree(tree_model,filled=True)
#plt.show()
"""
The tree's graph show us that it consists of only one decision node that 
splits the data on the variable sex (the first variable, X[0]). 
All 314 females end up in one leaf node and all 577 males end up in a 
different leaf node.

Let's make predictions with this tree and view a table of the results:
"""
# Get survival probability
preds = tree_model.predict_proba(X = pd.DataFrame(encoded_sex))
print(preds)
print(pd.crosstab(preds[:,0], titanic_train["Sex"]))
"""
The table shows that the decision tree managed to create the simple 
gender-based model where all females survive and all males perish.

Let's create a new decision tree that adds the passenger class variable and 
see how it changes the resulting predictions:
"""
# Make data frame of predictors
predictors = pd.DataFrame([encoded_sex, titanic_train["Pclass"]]).T

# Train the model
tree_model.fit(X = predictors, 
               y = titanic_train["Survived"])
"""
Now let's look at the graph of the new decision tree model:
"""
# Save tree
#tree.plot_tree(tree_model,filled=True)
#plt.show()
 # Save tree as dot file
dot_data = tree.export_graphviz(tree_model, out_file=None) 
graph = graphviz.Source(dot_data)  
graph.render('Source2.gv', view=True) 

"""
Notice that by adding one more variable, the tree is considerably more complex.
It now has 6 decision nodes, 6 leaf nodes and a maximum depth of 3.
Let's make predictions and view a table of the results:
"""    
# Get survival probability
preds = tree_model.predict_proba(X = predictors)

# Create a table of predictions by sex and class
print(pd.crosstab(preds[:,0], columns = [titanic_train["Pclass"], 
                                   titanic_train["Sex"]]))

"""
Notice that the more complex model still predicts a higher survival rate for 
women than men, but women in third class only have a 50% predicted death 
probability while women in first class are predicted to die less than 5% of 
the time.

The more variables you add to a decision tree, the more yes/no decisions it 
can make, resulting in a deeper, more complex tree. Adding too much complexity
to a decision tree, however, makes it prone to overfitting the training data, 
which can lead to poor generalization to unseen data. Let's investigate by 
creating a larger tree with a few more variables:
"""    

predictors = pd.DataFrame([encoded_sex,
                           titanic_train["Pclass"],
                           titanic_train["Age"],
                           titanic_train["Fare"]]).T

# Initialize model with maximum tree depth set to 8
tree_model = tree.DecisionTreeClassifier(max_depth = 8)

tree_model.fit(X = predictors, 
               y = titanic_train["Survived"])

# Save tree
#tree.plot_tree(tree_model,filled=True)
#plt.show()
# Save tree as dot file
dot_data = tree.export_graphviz(tree_model, out_file=None) 
graph = graphviz.Source(dot_data)  
graph.render('Source3.gv', view=True)

"""
The image above illustrates how complex decision trees can become when you 
start adding more explanatory variables. You can control the complexity of 
the tree by altering some of the decision tree function's default parameters. 
For example, when we made the tree above, we set max_depth = 8, which limited 
the tree to a depth of 8 (if we hadn't done this the tree would have been much 
larger!).

For interest's sake, let's check the accuracy of this decision tree model on 
the training data:
"""
scores=tree_model.score(X = predictors, 
                 y = titanic_train["Survived"])
print(scores)
"""
The model is almost 89% accurate on the training data, but how does it do on 
unseen data?
"""



"""
You can create a holdout validation set using the train_test_split() 
in sklearn's cross_validation library:

"""
print("HOLD OUT VALIDATION EXAMPLE OUTPUT")
from sklearn.model_selection import train_test_split
v_train, v_test = train_test_split(titanic_train,     # Data set to split
                                   test_size = 0.25,  # Split ratio
                                   random_state=1,    # Set random seed
                                   stratify = titanic_train["Survived"]) #*

# Training set size for validation
print(v_train.shape)
# Test set size for validation
print(v_test.shape)

"""
Note: When performing classification, it is desirable for each class in the 
target variable to have roughly the same proportion across each split of the 
data. The stratify argument lets you specify a target variable to spread 
evenly across the train and test splits.

The output above shows that we successfully created a new training set with 
roughly 75% of the original data and a validation test set with 25% of the 
data. We could proceed by building models with this new training set and 
making predictions on the validation set to assess the models.
"""
"""
CROSS VALIDATION
You can create K cross validation splits of the data using the Kfold() 
function in sklearn's model_selection library:
"""
print("CROSS VALIDATION EXAMPLE OUTPUT")
from sklearn.model_selection import KFold

kf = KFold(n_splits=10, random_state=12,shuffle=True)
print(kf.get_n_splits(titanic_train))

"""
After creating a cross validation object, you can loop over each fold and 
train and evaluate a your model on each one:
"""
fold_accuracy = []

titanic_train["Sex"] = encoded_sex

for train_fold, valid_fold in kf.split(titanic_train):
    train = titanic_train.loc[train_fold] # Extract train data with cv indices
    valid = titanic_train.loc[valid_fold] # Extract valid data with cv indices
    
    model = tree_model.fit(X = train[["Sex","Pclass","Age","Fare"]], 
                           y = train["Survived"])
    valid_acc = model.score(X = valid[["Sex","Pclass","Age","Fare"]], 
                            y = valid["Survived"])
    fold_accuracy.append(valid_acc)    

print("Accuracy per fold: ", fold_accuracy, "\n")
print("Average accuracy: ", sum(fold_accuracy)/len(fold_accuracy))


"""
Model accuracy can vary significantly from one fold to the next, especially 
with small data sets, but the average accuracy across the folds gives you an 
idea of how the model might perform on unseen data.

As with holdout validation, we'd like the target variable's classes to have 
roughly the same proportion across each fold when performing cross validation 
for a classification problem. To perform stratified cross validation, use the 
StratifiedKFold() function instead of KFold().

You use can score a model with stratified cross validation with a single 
function call with the cross_val_score() function:
"""

print("**************CROSS VAL SCORE OUTPUT***************")
from sklearn.model_selection import cross_val_score
scores = cross_val_score(estimator= tree_model,     # Model to test
                X= titanic_train[["Sex","Pclass",   # Train Data
                                  "Age","Fare"]],  
                y = titanic_train["Survived"],      # Target variable
                scoring = "accuracy",               # Scoring metric    
                cv=10)                              # Cross validation folds

print("Accuracy per fold: ")
print(scores)
print("Average accuracy: ", scores.mean())

"""
Notice that the average accuracy across each fold is higher than the 
non-stratified K-fold example. The cross_val_score function is useful for 
testing models and tuning model parameters (finding optimal values for 
arguments like maximum tree depth that affect model performance).
"""