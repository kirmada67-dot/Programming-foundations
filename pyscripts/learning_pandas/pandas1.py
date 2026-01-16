#!/usr/bin/env python3
import pandas as pn
import os
#pan = pn.Series([1, 3, 4])
#print(pan)

#data = {"sr.no.": [1, 2, 3], "age": [19, 21, 25], "salary": [200, 2000, 4000]}

#df = pn.DataFrame(data)

df = pn.read_csv("test.csv")
fullmarks = 100
print(df)
print(df["score"] >= 100)
print(df.info())
#print(df)

#print(os.getcwd())

#print(df)
