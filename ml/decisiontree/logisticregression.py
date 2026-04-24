import pandas as pd
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings("ignore")

# Sample dataset
df = pd.DataFrame({
    'age': [22, 25, 47, 52],
    'salary': [20000, 25000, 50000, 60000],
    'churn': [0, 0, 1, 1]
})

X = df[['age', 'salary']]
y = df['churn']

model = LogisticRegression()
model.fit(X, y)

print(model.predict([[30, 30000]]))
print(model.predict([[45, 45000]]))
print(model.predict([[45, 10000]]))

X_test =X
predictions = model.predict(X_test)
from sklearn.metrics import classification_report, f1_score
y_test=[0,0,1,1]

# Evaluate the model and print the results
print(classification_report(y_test, predictions))
print('Predicted labels: ', predictions)
print('F1-score: ', f1_score(y_test, predictions))