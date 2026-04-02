#!/usr/bin/env python3
import pandas as pn
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import GradientBoostingRegressor

df = pn.read_csv("../dummy_data/problem1.csv")
x = df[["area", "rooms", "age"]]
y = df["rent"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=69)
model = GradientBoostingRegressor(n_estimators=1000, learning_rate=0.01, random_state=69)

model.fit(x_train, y_train)
pred_train = model.predict(x_train)
pred_test = model.predict(x_test)
print("Model: ", model)
print("\n")
print("Train predictions: ", pred_train)
print("Train MSE: ", mean_squared_error(y_train, pred_train))
print("Train r2_score: ", r2_score(y_train, pred_train))
print("\n")
print("Test predictions: ", pred_test)
print("Test MSE: ", mean_squared_error(y_test, pred_test))
print("Test r2_score: ", r2_score(y_test, pred_test))
