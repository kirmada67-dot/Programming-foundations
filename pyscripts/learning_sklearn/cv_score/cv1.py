#!/usr/bin/env python3
import pandas as pn
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

df = pn.read_csv("../dummy_data/problem1.csv")
model = Ridge()
scaler = StandardScaler()

x = df[["area", "rooms", "age"]]
y = df["rent"]

pipeline = Pipeline([("scaler", scaler), ("model", model)])

scores = cross_val_score(pipeline, x, y, cv=7)
print("Model: ", model)
print(scores)
print("Mean: ", scores.mean())
