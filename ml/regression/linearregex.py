#Linear Regression
"""
Linear Regression
The foundation of every predictive model — understand it deeply

What it does
Finds the best-fit line (or hyperplane) through data by minimising the sum of squared residuals. 
The "best" line minimises prediction error across all training points.

The model: ŷ = β₀ + β₁x₁ + β₂x₂ + … + βₙxₙ

Where β values (coefficients) represent: "for a 1-unit increase in xᵢ, y changes by βᵢ — holding 
all else constant."

Key metrics
MSE — Mean Squared Error. Penalises large errors heavily. Not interpretable in original units.
RMSE — Root MSE. Same units as y. Most commonly reported.
MAE — Mean Absolute Error. Robust to outliers. Easier to interpret.
R² — Proportion of variance explained. 1.0 = perfect, 0 = predicts the mean, negative = worse than baseline.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler

# --- Load data ---
data = fetch_california_housing()
X, y = data.data, data.target
feature_names = data.feature_names
# print(X)
# print(feature_names)
# print(y)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- Fit Linear Regression ---
scaler = StandardScaler()#Explain What is StandardScaler? 
X_train_s = scaler.fit_transform(X_train)#Explain What is fit_transform?
X_test_s  = scaler.transform(X_test)#Explain What is transform?

lr = LinearRegression() #Explain What is LinearRegression?
lr.fit(X_train_s, y_train)#Explain What is fit?

# --- Evaluate ---
y_pred = lr.predict(X_test_s)#Explain What is predict?
rmse = np.sqrt(mean_squared_error(y_test, y_pred))#Explain What is mean_squared_error?
mae  = mean_absolute_error(y_test, y_pred)#Explain What is mean_absolute_error?
r2   = r2_score(y_test, y_pred)#Explain What is r2_score?

print(f"RMSE : {rmse:.3f}")
print(f"MAE  : {mae:.3f}")
print(f"R²   : {r2:.3f}")

# --- Interpret coefficients ---
coef_df = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': lr.coef_
}).sort_values('Coefficient', key=lambda x: x.abs(), ascending=False)
print(coef_df.to_string(index=False))

# --- Residual plot (must look random for good model) ---
print("*************y_test*****************")
print(y_test)
print("*************y_pred*****************")
print(y_pred)
print("*************residuals*****************")
residuals = y_test - y_pred #actual - predicted
print(residuals)
plt.figure(figsize=(8, 4))
plt.scatter(y_pred, residuals, alpha=0.3, s=10)
plt.axhline(0, color='red', linewidth=1)
plt.xlabel("Predicted"); plt.ylabel("Residual")
plt.title("Residual Plot — should be random scatter")
plt.tight_layout(); plt.show()

'''
Explain R² in one sentence to a non-technical person.
What does a coefficient of 0.5 on a scaled feature mean?
What pattern in a residual plot indicates the linear model is correct? 
What patterns indicate problems?
'''