print("#############################################################################")
import pickle
import numpy as np
# with open('Stockprice_prediction.model','wb') as f:
#     pickle.dump(clf,f) 

Stockprice_regressor =pickle.load(open('Stockprice_prediction.model','rb'))

data =[3.414,96.12,96.58,268900140]
features = np.array(data)
features.resize(1,4)
price =Stockprice_regressor.predict(features)
print(price)