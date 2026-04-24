'''
Take a look at the Linnerud dataset(https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_linnerud.html#sklearn.datasets.load_linnerud) in Scikit-learn. 

This dataset has multiple targets(https://scikit-learn.org/stable/datasets/toy_dataset.html#linnerrud-dataset): 
'It consists of three exercise (data) and three physiological (target) variables 
collected from twenty middle-aged men in a fitness club'.

In your own words, describe how to create a Regression model that would plot the 
relationship between the waistline and how many situps are accomplished. Do the same 
for the other datapoints in this dataset.

Rubric
Criteria	                    Exemplary	                            Adequate	                        Needs Improvement
Submit a descriptive paragraph	Well-written paragraph is submitted	    A few sentences are submitted	    No description is supplied
'''

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model, model_selection
from sklearn.datasets import load_linnerud
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

linnerud=load_linnerud()
X, y = linnerud.data, linnerud.target
feature_names = linnerud.feature_names
target_names = linnerud.target_names

#Features  ['Chins', 'Situps', 'Jumps']
print("Feature names:", feature_names)
print("Target names:", target_names)
print("X shape:", X.shape)
print("y shape:", y.shape)


# Initialize model
model = linear_model.LinearRegression()


# -------- Waist vs Situps --------
situps = X[:, 1].reshape(-1, 1)
waist = y[:, 1]

model.fit(situps, waist)
waist_pred = model.predict(situps)

# Metrics
rmse_waist = np.sqrt(mean_squared_error(waist, waist_pred))
mae_waist = mean_absolute_error(waist, waist_pred)
r2_waist = r2_score(waist, waist_pred)

print("\nWaist vs Situps Metrics")
print("RMSE:", rmse_waist)
print("MAE:", mae_waist)
print("R2:", r2_waist)

# Plot
plt.scatter(situps, waist, color="blue", label="Actual")
plt.plot(situps, waist_pred, color="red", label="Regression Line")
plt.xlabel("Situps")
plt.ylabel("Waist")
plt.title("Regression: Waist vs Situps")
plt.legend()
plt.show()


# -------- Weight vs Chins --------
chins = X[:, 0].reshape(-1, 1)
weight = y[:, 0]

model.fit(chins, weight)
weight_pred = model.predict(chins)

# Metrics
rmse_weight = np.sqrt(mean_squared_error(weight, weight_pred))
mae_weight = mean_absolute_error(weight, weight_pred)
r2_weight = r2_score(weight, weight_pred)

print("\nWeight vs Chins Metrics")
print("RMSE:", rmse_weight)
print("MAE:", mae_weight)
print("R2:", r2_weight)

# Plot
plt.scatter(chins, weight, color="blue", label="Actual")
plt.plot(chins, weight_pred, color="red", label="Regression Line")
plt.xlabel("Chins")
plt.ylabel("Weight")
plt.title("Regression: Weight vs Chins")
plt.legend()
plt.show()