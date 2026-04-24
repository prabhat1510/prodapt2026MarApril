import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from imblearn.over_sampling import SMOTE
import warnings
warnings.filterwarnings("ignore")

df  = pd.read_csv('cuisines.csv')
print(df.head())
print(df.info())
print(df['cuisine'].value_counts())
df.cuisine.value_counts().plot.barh()
#plt.show()


thai_df = df[(df.cuisine == "thai")]
japanese_df = df[(df.cuisine == "japanese")]
chinese_df = df[(df.cuisine == "chinese")]
indian_df = df[(df.cuisine == "indian")]
korean_df = df[(df.cuisine == "korean")]

print(f'thai df: {thai_df.shape}')
print(f'japanese df: {japanese_df.shape}')
print(f'chinese df: {chinese_df.shape}')
print(f'indian df: {indian_df.shape}')
print(f'korean df: {korean_df.shape}')

### What are the top ingredients by class

def create_ingredient_df(df):
    # transpose df, drop cuisine and unnamed rows, sum the row to get total for ingredient and add value header to new df
    ingredient_df = df.T.drop(['cuisine','Unnamed: 0']).sum(axis=1).to_frame('value')
    # drop ingredients that have a 0 sum
    ingredient_df = ingredient_df[(ingredient_df.T != 0).any()]
    # sort df
    ingredient_df = ingredient_df.sort_values(by='value', ascending=False, inplace=False)
    return ingredient_df

thai_ingredient_df = create_ingredient_df(thai_df)
thai_ingredient_df.head(10).plot.barh()
#plt.show()

japanese_ingredient_df = create_ingredient_df(japanese_df)
japanese_ingredient_df.head(10).plot.barh()
#plt.show()

chinese_ingredient_df = create_ingredient_df(chinese_df)
chinese_ingredient_df.head(10).plot.barh()
#plt.show()

indian_ingredient_df = create_ingredient_df(indian_df)
indian_ingredient_df.head(10).plot.barh()
#plt.show()

korean_ingredient_df = create_ingredient_df(korean_df)
korean_ingredient_df.head(10).plot.barh()
#plt.show()

#Drop very common ingredients (common to all cuisines)
feature_df= df.drop(['cuisine','Unnamed: 0','rice','garlic','ginger'], axis=1)
labels_df = df.cuisine #.unique()
print(feature_df.head())

'''
Balance data with SMOTE oversampling to the highest class. 
Read more here: https://imbalanced-learn.org/dev/references/generated/imblearn.over_sampling.SMOTE.html
'''
oversample = SMOTE()
transformed_feature_df, transformed_label_df = oversample.fit_resample(feature_df, labels_df)

print(f'new label count: {transformed_label_df.value_counts()}')
print(f'old label count: {df.cuisine.value_counts()}')

print(transformed_label_df.value_counts())


# export transformed data to new df for classification
transformed_df = pd.concat([transformed_label_df,transformed_feature_df],axis=1, join='outer')
print(transformed_df.head())
print(transformed_df.info())
transformed_df.to_csv("cleaned_cuisines.csv")


#Build Classification Model
cuisines_df = pd.read_csv("cleaned_cuisines.csv")
print(cuisines_df.head())

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score,precision_score,confusion_matrix,classification_report, precision_recall_curve
from sklearn.svm import SVC
import numpy as np


cuisines_label_df = cuisines_df['cuisine']
#cuisines_label_df.head()
cuisines_feature_df = cuisines_df.drop(['Unnamed: 0', 'cuisine'], axis=1)
#cuisines_feature_df.head()

X_train, X_test, y_train, y_test = train_test_split(cuisines_feature_df, cuisines_label_df, test_size=0.3)

#lr = LogisticRegression(multi_class='ovr',solver='liblinear')
lr = LogisticRegression(solver='lbfgs')
model = lr.fit(X_train, np.ravel(y_train))

accuracy = model.score(X_test, y_test)
print ("Accuracy is {}".format(accuracy))


# test an item
print(f'ingredients: {X_test.iloc[50][X_test.iloc[50]!=0].keys()}')
print(f'cuisine: {y_test.iloc[50]}')


#rehsape to 2d array and transpose
test= X_test.iloc[50].values.reshape(-1, 1).T
# predict with score
proba = model.predict_proba(test)
classes = model.classes_
# create df with classes and scores
resultdf = pd.DataFrame(data=proba, columns=classes)

# create df to show results
topPrediction = resultdf.T.sort_values(by=[0], ascending = [False])
#topPrediction.head()

y_pred = model.predict(X_test)
print(classification_report(y_test,y_pred))
