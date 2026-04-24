#Predict if a person buys a product
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Features: Age
X = [[22], [25], [47], [52], [46], [56]]

# Target: 0 = No, 1 = Yes
y = [0, 0, 1, 1, 1, 1]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=0)

# Create model
model = DecisionTreeClassifier()

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict new data
print(model.predict([[30]]))
print(model.predict([[50]]))
print(model.predict([[36]]))

#Find Entropy, Gini and Information Gain of above code
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=3)
print("Cross-validation scores:", scores)





