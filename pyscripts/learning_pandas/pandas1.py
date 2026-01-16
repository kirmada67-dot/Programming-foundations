#!/usr/bin/env python3
import pandas as pn

#pan = pn.Series([1, 3, 4])
#print(pan)

data = {"age": [19, 21, 25], "salary": [200, 2000, 4000]}

df = pn.DataFrame(data)
print(df)
