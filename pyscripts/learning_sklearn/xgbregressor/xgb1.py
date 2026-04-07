#!/usr/bin/env python3
import pandas as pn
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score

df = pn.read_csv("../dummy_data/large.csv")
x = df[["area", "rooms", "age"]]
y = df["rent"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
#new_x_train, x_val, new_y_train, y_val = train_test_split(x_train, y_train, test_size=0.2, random_state=42)

model = XGBRegressor(n_estimators=1000, learning_rate=0.01, max_depth=3, subsample=0.7, random_state=69, colsample_bytree=0.5)


model.fit(x_train, y_train)
test_pred = model.predict(x_test)
train_pred = model.predict(x_train)

print("model: ", model)
#print("Best iteration: ", model.best_iteration)
print("\n")
print("Train_prediction: ", train_pred)
print("Train_MSE: ", mean_squared_error(y_train, train_pred))
print("Train_r2_score: ", r2_score(y_train, train_pred))
print("\n")
print("Test_prediction: ", test_pred)
print("Test_MSE: ", mean_squared_error(y_test, test_pred))
print("Test_r2_score: ", r2_score(y_test, test_pred))
