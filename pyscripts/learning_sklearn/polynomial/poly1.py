#!/usr/bin/env python3
import pandas as pn
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

df = pn.read_csv("../dummy_data/problem1.csv")
x = df[["area", "rooms", "age"]]
y = df["rent"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=6)

pipeline = Pipeline([("poly", PolynomialFeatures(degree=2, include_bias=False)), ("scaler", StandardScaler()), ("model", Lasso(alpha=1))])

pipeline.fit(x_train, y_train)

pred = pipeline.predict(x_test)

features = pipeline.named_steps["poly"].get_feature_names_out()
coef_ = pipeline.named_steps["model"].coef_

print("model: ", pipeline.named_steps["model"])
for a, b in zip(features, coef_):
	print(f"coef_{a}: {b}")
print("intercept_", pipeline.named_steps["model"].intercept_)
print("MSE: ", mean_squared_error(y_test, pred))
print("R2 score: ", r2_score(y_test, pred))
print("Predictions: ", pred)
print("y_test: ", y_test)

