import pandas as pd
import math , datetime
import numpy as np
from sklearn import preprocessing , svm 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

#loading the dataset
#url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ_19245678901234567890123456789012345678901234567890/pub?gid=0&single=true&output=csv"
df = pd.read_csv("GOOG.csv")
#print(df.head())
#Calculate the HC and % of Change for the stock prices - derived features 
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

df['HC_%'] = ((df['High'] - df['Close']) / df['Close']) *100 #average traded value
df['%_change'] = ((df['Close'] - df['Open']) / df['Open']) *100 
#print(df.head())

#drop the missing values
df.dropna(inplace=True)
#Schema of the Dataframe
#print(df.info())
print("****************Statistics of the dataframe******************************")
#Statistics of the dataframe
print(df.describe())
df = df[['Close' , 'HC_%' , '%_change' , 'Volume']]
print(df.head())
sns.pairplot(df)
plt.show()
#"Close" is the Stock price column to be forecasted !!!!!!
forecast_col = 'Close'
forecast_out = int(math.ceil(0.01 * len(df)))   
print("The total records in data frame to be shifted", forecast_out)
print("The total records in the data frame",len(df))

# shift all closing 49 days 
#Deriving a forecast Label
df['Price_label'] = df[forecast_col].shift(-forecast_out)
print(df.head(10))
print(df.isnull().sum())

# y is called Label
y = df['Price_label']
print(y)
# x are features
x = df.drop(['Price_label'] , axis=1)

print("************************************")
print(x)

# after dropping all null values  ( records)
df.dropna(axis=0,inplace=True)
y = df['Price_label']
x = df.drop(['Price_label'] , axis=1)

print("Features")
print(x)
print("Labels")
print(y)
print(len(x) , len(y))
#Building a Machine learning model
# Build / develop a model 
# pickle is to save my model
import pickle
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(x , y , test_size = 0.2)

clf = LinearRegression()
# feed the data for training 
clf.fit(X_train , y_train) # Training my model 
# equation is ready
accuracy_in_precicting_the_stock = clf.score(X_test , y_test)

print(accuracy_in_precicting_the_stock * 100)

# permanently storing model files ( LR)

with open('linearregression.pickle' , 'wb') as f:
    pickle.dump(clf , f)

pickle_in = open('linearregression.pickle' , 'rb')
clf = pickle.load(pickle_in)

#print(accuracy_in_precicting_the_stock * 100)
print(-forecast_out)
x_lately = x[-forecast_out:]
print(x_lately)
# later predictions
sample = pd.DataFrame(x_lately)
print(len(sample)) 
print(clf.intercept_)
print(clf.coef_)
coeff_df = pd.DataFrame(clf.coef_,x.columns,columns=['Coefficient'])

print(coeff_df)

print(x_lately) 
forecast_set = clf.predict(x_lately)            

print("Predicted Stock prices\n\n", forecast_set)
print ("\n\nAccuracy :", accuracy_in_precicting_the_stock *100)

colname =['49thdayprediction']
final_predictions = pd.DataFrame(forecast_set,columns=colname)
final_predictions
print(len(final_predictions))
x_lately.reset_index()
print(len(x_lately))
x_lately['49thdayprediction']=forecast_set
print("************************")
print(x_lately)
print(clf.coef_)

new_data =[3.414,96.12,96.58,268900140] # one date 
features = np.array(new_data)
print("****************************************************")
print(features)
features.resize(1,4)
Stock_price = clf.predict(features)
print("Predicted Stock price",Stock_price)
print("#############################################################################")
import pickle
with open('Stockprice_prediction.model','wb') as f:
    pickle.dump(clf,f) 

Stockprice_regressor =pickle.load(open('Stockprice_prediction.model','rb'))

data =[3.414,96.12,96.58,268900140]
features = np.array(data)
features.resize(1,4)
price =Stockprice_regressor.predict(features)
print(price)
'''
#prepare the data for machine learning
#create features and target variables
X = np.array(df.drop(['Close'],1))
y = np.array(df['Close'])

#split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#train the model
model = LinearRegression()
model.fit(X_train, y_train)

#make predictions
y_pred = model.predict(X_test)

#evaluate the model
print('Mean Absolute Error:', mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', mean_squared_error(y_test, y_pred))
print('R-squared:', r2_score(y_test, y_pred))
'''