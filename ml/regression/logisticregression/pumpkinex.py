import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

full_pumpkins = pd.read_csv('US-pumpkins.csv')

#print(full_pumpkins.head())
#print(full_pumpkins.columns)
#print(full_pumpkins.info())

# Select the columns we want to use
columns_to_select = ['City Name','Package','Variety', 'Origin','Item Size', 'Color']
pumpkins = full_pumpkins.loc[:, columns_to_select]

# Drop rows with missing values
pumpkins.dropna(inplace=True)

print(pumpkins.head())


# Specify colors for each values of the hue variable
palette = {
    'ORANGE': 'orange',
    'WHITE': 'wheat',
}
# Plot a bar plot to visualize how many pumpkins of each variety are orange or white
sns.catplot(
    data=pumpkins, y="Variety", hue="Color", kind="count",
    palette=palette, 
)


#plt.show()
# Data pre-processing

#Let's encode features and labels to better plot the data and train the model
# Let's look at the different values of the 'Item Size' column
print(pumpkins['Item Size'].unique())
'''
OrdinalEncoder is a scikit-learn preprocessing tool that converts categorical text data into numerical 
integers (0, 1, 2, ...) based on a specific, ordered ranking. It is ideal for ordinal data—where categories 
have a natural order, such as "low," "medium," "high".
'''
from sklearn.preprocessing import OrdinalEncoder
# Encode the 'Item Size' column using ordinal encoding
item_size_categories = [['sml', 'med', 'med-lge', 'lge', 'xlge', 'jbo', 'exjbo']]
ordinal_features = ['Item Size']
ordinal_encoder = OrdinalEncoder(categories=item_size_categories)
print(ordinal_encoder.fit_transform(pumpkins[ordinal_features]))
print("*************************************************************************")
'''
OneHotEncoder is a crucial preprocessing tool in machine learning, available in scikit-learn and PySpark, 
that converts categorical text data into a numerical binary format (0s and 1s). It creates a separate 
column for each unique category, marking 1 for presence and 0 for absence, which prevents models from 
assuming incorrect ordinal relationships between categories.
'''
from sklearn.preprocessing import OneHotEncoder
# Encode all the other features using one-hot encoding
categorical_features = ['City Name', 'Package', 'Variety', 'Origin']
categorical_encoder = OneHotEncoder(sparse_output=False)
print(categorical_encoder.fit_transform(pumpkins[categorical_features]))
print("*************************************************************************")
#Transformer
'''
ColumnTransformer is a scikit-learn class that applies different preprocessing steps (scaling, encoding) 
to specific columns in a dataset simultaneously. It handles mixed data types (numerical and categorical) 
efficiently, allowing for customized transformations per column type before model training.
'''
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer(transformers=[
     ('ord', ordinal_encoder, ordinal_features),
     ('cat', categorical_encoder, categorical_features)
     ])
# Get the encoded features as a pandas DataFrame
ct.set_output(transform='pandas')
encoded_features = ct.fit_transform(pumpkins)
print(encoded_features.head())
print("*************************************************************************")
'''
LabelEncoder is a scikit-learn preprocessing tool that converts categorical text data into numerical 
integers (0 to (n-1) classes). It is primarily used to encode target labels (y) 
rather than input features (X), assigning unique integers to each category.
'''
from sklearn.preprocessing import LabelEncoder
# Encode the 'Color' column using label encoding
label_encoder = LabelEncoder()
encoded_label = label_encoder.fit_transform(pumpkins['Color'])
encoded_pumpkins = encoded_features.assign(Color=encoded_label)
print(encoded_pumpkins.head())

# Let's look at the mapping between the encoded values and the original values
print(list(label_encoder.inverse_transform([0, 1])))

print("*******************Analysing relationships between features and label**********************")
#Analysing relationships between features and label
palette = {
    'ORANGE': 'orange',
    'WHITE': 'wheat',
}
# We need the encoded Item Size column to use it as the x-axis values in the plot
pumpkins['Item Size'] = encoded_pumpkins['ord__Item Size']

g = sns.catplot(
    data=pumpkins,
    x="Item Size", y="Color", row='Variety',
    kind="box", orient="h",
    sharex=False, margin_titles=True,
    height=1.8, aspect=4, palette=palette,
)
# Defining axis labels 
g.set(xlabel="Item Size", ylabel="").set(xlim=(0,6))
g.set_titles(row_template="{row_name}")
#plt.show()

print("*******************Let's now focus on a specific relationship: Item Size and Color!**********************")
# Suppressing warning message claiming that a portion of points cannot be placed into the plot due to the high number of data points
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='seaborn')

palette = {
    0: 'orange',
    1: 'wheat'
}
sns.swarmplot(x="Color", y="ord__Item Size", hue="Color", data=encoded_pumpkins, palette=palette)
#plt.show()
#Build our model
from sklearn.model_selection import train_test_split
# X is the encoded features
X = encoded_pumpkins[encoded_pumpkins.columns.difference(['Color'])]
print("*********Value of X**********************")
print(X)
# y is the encoded label
y = encoded_pumpkins['Color']

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)


from sklearn.metrics import f1_score, classification_report 
from sklearn.linear_model import LogisticRegression

# Train a logistic regression model on the pumpkin dataset
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

# Evaluate the model and print the results
print(classification_report(y_test, predictions))
print('Predicted labels: ', predictions)
print('F1-score: ', f1_score(y_test, predictions))
'''
A confusion matrix is a performance evaluation table for machine learning classification models, 
comparing predicted classes against actual ground truth. It displays true positives (TP), 
true negatives (TN), false positives (FP), and false negatives (FN), allowing for detailed 
analysis of correct versus incorrect predictions.
Key Metrics Derived from Confusion Matrix
Accuracy: \(\frac{TP+TN}{Total}\), measures overall correctness.
Precision: \(\frac{TP}{TP+FP}\), measures accuracy of positive predictions.
Recall (Sensitivity): \(\frac{TP}{TP+FN}\), measures the ability to find all positive instances.
F1-Score: Harmonic mean of precision and recall.

'''
from sklearn.metrics import confusion_matrix
print("*********Confusion Matrix**********************")
print(confusion_matrix(y_test, predictions))

print("*********************ROC Curve***************************")
'''
 What is ROC ?
 ROC (Receiver Operating Characteristic) curve is a fundamental tool for 
 evaluating the performance of binary classification models (like your Logistic Regression model for pumpkins).
 It plots the True Positive Rate (TPR) against the False Positive Rate (FPR) at various probability thresholds.

'''
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline

y_scores = model.predict_proba(X_test)
# calculate ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_scores[:,1])

# plot ROC curve
fig = plt.figure(figsize=(6, 6))
# Plot the diagonal 50% line
plt.plot([0, 1], [0, 1], 'k--')
# Plot the FPR and TPR achieved by our model
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()
'''
What is AUC Score?
'''
print("*********************AUC Score***************************")
from sklearn.metrics import roc_auc_score
auc_score = roc_auc_score(y_test, y_scores[:,1])
print('AUC Score: ', auc_score)
