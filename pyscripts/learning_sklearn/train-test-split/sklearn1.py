#!/usr/bin/env python3
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np

x = [[1], [2], [3], [4], [5]]
y = [20, 30, 40, 50, 60]
y = np.array(y).reshape(-1, 1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=69)

scaler = StandardScaler()

x_train = scaler.fit_transform(x_train)
y_train = scaler.fit_transform(y_train)
x_test = scaler.transform(x_test)
y_test = scaler.transform(y_test)

print("x_train: ", x_train, "\ny_train: ", y_train, "\nx_test: ", x_test, "\ny_test: ", y_test)


