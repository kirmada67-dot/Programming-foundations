#!/usr/bin/env python3
import pandas as pn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
#from sklearn.metrics import mean_squared_error, r2_score

x = [[500], [800], [1200], [1500]]
y = [10000, 15000, 25000, 30000]

#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=69)

model = DecisionTreeRegressor()

model.fit(x, y)

pred = model.predict([[1100]])

#print("x_test: ", x_test)
print("prediction: ", pred)
