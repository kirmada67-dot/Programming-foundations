#!/usr/bin/env python3
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

x = df[["area", "rooms"]]
y = df["rent"]

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=69)

model = LinearRegression(fit_intercept=False)

model.fit(x_train, y_train)

print(model.coef_)
print(model.intercept_)

y_pred = model.predict(x_test)

mse = mean_squared_error(y_test, y_pred)

print(y_pred)
print(y_test)
print(mse)
print(r2_score(y_test, y_pred))

