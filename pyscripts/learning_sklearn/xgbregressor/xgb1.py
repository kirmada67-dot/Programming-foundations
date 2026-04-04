#!/usr/bin/env python3
import pandas as pn
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score

df = pn.read_csv("../dummy_data/problem1.csv")
x = df[["area", "rooms", "age"]]
y = df["rent"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=69)

model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)

model.fit(x_train, y_train)
pred = model.predict(x_test)
print("model: ", model)
print("prediction: ", pred)
print("MSE: ", mean_squared_error(y_test, pred))
print("r2_score: ", r2_score(y_test, pred))
