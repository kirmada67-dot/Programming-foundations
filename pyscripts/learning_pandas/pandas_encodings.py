#!/usr/bin/env python3
import pandas as pn
import numpy as np

df = pn.read_csv("test.csv")

df["grade"] = np.where(df["score"] >= 90, "A", "B")
df["grade_num"] = df["grade"].map({"A" : 1, "B" : 0})

dummies = pn.get_dummies(df, columns=["grade"])

print(dummies)

