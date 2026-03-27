#!/usr/bin/env python3
import pandas as pn
import numpy as np


df = pn.read_csv("data.csv")
df["age"].fillna(df["age"].mean(), inplace=True)
df["city"].fillna(df["city"].mode()[0], inplace=True)
df["passed"] = df["score"] >= 75
df["grade"] = np.where(df["score"] >= 85, "A", "B")
print(df.isna().sum())
print(df[df["city"] == "Pune"])
print(df.groupby(df["grade"])["name"].count())
df["grade_num"] = df["grade"].map({"A" : 1, "B" : 0})
print(df)

dummies = pn.get_dummies(df, columns=["city"])
print(dummies)

x = df.drop("score", axis=1)
y = df["score"]
print(x)
print(y)
