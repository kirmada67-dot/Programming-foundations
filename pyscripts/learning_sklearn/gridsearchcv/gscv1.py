#!/usr/bin/env python3
import pandas as pn
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline

df = pn.read_csv("../dummy_data/problem1.csv")
df["area_squared"] = df["area"] ** 2
x = df[["area", "rooms", "age", "area_squared"]]
y = df["rent"]

pipeline = Pipeline([("scaler", StandardScaler()), ("model", Lasso(max_iter=10000))])

param_grid = {"model__alpha": [0.001, 0.01, 0.1, 1, 10, 100]}

grid = GridSearchCV(pipeline, param_grid, cv=7)

grid.fit(x, y)

print("Best param: ", grid.best_params_)
print("Best score: ", grid.best_score_)

best_model = grid.best_estimator_
print("coef_: ", best_model.named_steps["model"].coef_)

