#!/usr/bin/env python3
import numpy as np
import pandas as pn
import os
#pan = pn.Series([1, 3, 4])
#print(pan)

#data = {"sr.no.": [1, 2, 3], "age": [19, 21, 25], "salary": [200, 2000, 4000]}

#df = pn.DataFrame(data)

#df = pn.read_csv("test.csv")
#fullmarks = 100
#print(df)
#df["age score ratio"] = df["age"] / df["score"]
#print(df)
#print(df["score"] >= 95)
#print(df.isna().sum())
#print(df)

#print(os.getcwd())

#print(df)
#print(df["name"])

df = pn.read_csv("test.csv")
#print(df[["name", "age"]])
#print(df.iloc[:2])
#print(df[df["age"] > 19])
#print(df["score"].sum())
#print(df.isna().sum())
#df["name"].fillna(df["name"].mode()[0], inplace=True)
#df["age"].fillna(df["age"].mean(), inplace=True)
#df["score"].fillna(df["score"].mean(), inplace=True)
#df.dropna(inplace=True)
#print(df.isna().sum())
#df["grade"] = np.where(df["score"] >= 95, "A", "B")
#print(df[["name", "score"]])
#print(df["name"].mode())
#df["grade"] = np.where(df["score"] >= 90, "A", "B")
#print(df.groupby("grade")["name"].count())
#print(df)


print(df.iloc[:5])
print(df.info)
print(df.isna().sum())
df["age"].fillna(df["age"].mean(), inplace=True)
df["name"].fillna(df["name"].mode()[0], inplace=True)
df["score"].fillna(df["score"].mean(), inplace=True)
print(df.isna().sum())
df["passed"] = df["score"] >= 80
df["grade"] = np.where(df["score"] >= 90, "A", "B")
print(df[df["score"] >= 85])

print(df.groupby("age")["score"].mean())
print(df.groupby("grade")["name"].count())
#print(df)
