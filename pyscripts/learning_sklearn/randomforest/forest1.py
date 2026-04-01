#!/usr/bin/env python3
import pandas as pn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

df = pn.read_csv("../dummy_data/problem1.csv")

x = df[["area", "rooms", "age"]]
y = df["rent"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=69)

model = RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42)
test_pred_data = x_train
test_result_data = y_train
model.fit(x_train, y_train)

pred = model.predict(test_pred_data)

print("Model: ", model)
if test_pred_data is x_train:
        print("Test based on: x_train")
else:
        print("Test based on: x_test")
print("prediction: ", pred)
print("MSE: ", mean_squared_error(test_result_data, pred))
print("r2_score: ", r2_score(test_result_data, pred))
