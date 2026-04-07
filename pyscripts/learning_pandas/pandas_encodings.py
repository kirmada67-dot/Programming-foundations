#!/usr/bin/env python3
import pandas as pn
import numpy as np

df = pn.read_csv("test.csv")

df["passed"] = df["score"] >= 80
df["grade"] = np.where(df["score"] >= 90, "A", "B")
df["grade_num"] = df["grade"].map({"A" : 1, "B" : 0})

city_dummies = pn.get_dummies(df, columns=["city"])

print(city_dummies)

