#!/usr/bin/env python3
import pandas as pn
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler

df = pn.read_csv("problem1.csv")
df["area_squared"] = df["area"] ** 2
x = df[["area", "rooms", "age", "area_squared"]]
y = df["rent"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,  random_state=42)
model = Lasso(alpha=1)
scaler = StandardScaler()

print(model)

print("x_test: ", x_test)

x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model.fit(x_train, y_train)

print("coef_:", model.coef_)
print("intercept_:", model.intercept_)

pred = model.predict(x_test)
print("Predictions: ", pred)

print("MSE: ", mean_squared_error(y_test, pred))
print("r2_score: ", r2_score(y_test, pred))
