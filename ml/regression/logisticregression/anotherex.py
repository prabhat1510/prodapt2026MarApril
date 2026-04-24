import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import train_test_split
import warnings
warnings.filterwarnings("ignore")

# Sample dataset
# df = pd.DataFrame({
#     'age': [22, 25, 47, 52],
#     'salary': [20000, 25000, 50000, 60000],
#     'churn': [0, 0, 1, 1]
# })

df =pd.read_csv('churn_data.csv')
'''
X = df[['age', 'salary']]
y = df['churn']

model = LogisticRegression()
model.fit(X, y)
'''
#print(model.predict([[30, 30000]]))
#print(model.predict([[45, 45000]]))
#print(model.predict([[45, 10000]]))

X = df[['age', 'salary']]
y = df['churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)


# Evaluate the model and print the results
print(classification_report(y_test, predictions))
print('Predicted labels: ', predictions)
print('F1-score: ', f1_score(y_test, predictions))
print("********************************************")
print('Model score: ', model.score(X_test, y_test))

print("*********************************************")
print(model.predict([[30, 30000]]))
print(model.predict([[45, 45000]]))
print(model.predict([[25, 10000]]))
print("*********************************************")
print(df.corr())
print("*********************************************")
print(model.coef_)
print("*********************************************")

