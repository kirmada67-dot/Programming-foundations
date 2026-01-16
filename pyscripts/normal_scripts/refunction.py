#!/usr/bin/env python3
import sys
def get_credentials():
	usr = input("Enter username: ").lower().strip()
	pin =  input("Enter password: ")
	return usr, pin
def check_credentials(usr, pin):
	if usr == "prem" and pin == "eldenlord":
		return True
	else:
		return False
def gatekeeper():
	attempts = 3
	while attempts > 0:
		usr, pin = get_credentials()
		if check_credentials(usr, pin):
			print("Access granted.")
			sys.exit(0)
		else:
			print("Invalid credentials")
			attempts -= 1
			print(f"You have {attempts} attempts left.")
	print("Access denied.")
gatekeeper()
