#!/usr/bin/env python3
crusr = "prem"
crpass = "eldenlord"
attempts = 3
while attempts > 0:
	usr = input("Enter username: ")
	password = input("Enter password: ")
	if usr == crusr and password == crpass:
		print("Welcome, Eldenlord.")
		exit(1)
	else:
		print("Invalid credentials, try again.")
	attempts-=1
print("Access denied!")
