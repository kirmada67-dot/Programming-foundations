#!/usr/bin/env python3
import sys
class User():
	def __init__(self, name, phoneno, location):
		self.name = name
		self.phoneno = phoneno
		self.location = location
	def __str__(self):
		return f"User: {self.name}, Phone: {self.phoneno}, Location: {self.location}"

class Driver():
	def __init__(self, name, phoneno, location, vehicle, available):
		self.name = name
		self.phoneno = phoneno
		self.location = location
		self.vehicle = vehicle
		self.available = available
	def __str__(self):
                return f"Driver: {self.name}, Phone: {self.phoneno}, Location: {self.location}, Vehicle: {self.vehicle}"


class Ride():
	def __init__(self, usr, driver, distance, fare, vehicle):
		self.usr = usr
		self.driver = driver
		self.distance = distance
		self.fare = fare
		self.veh = vehicle
		driver.available = False
	def end_ride():
		self.driver.available = True
	def __str__(self):
		return f"User: {self.usr.name} with Driver: {self.driver.name}, Distance: {self.distance}km, Vehicle: {self.veh}, Fare:Rs.{self.fare}"

drv1 = Driver("Harsh", 101, "Satara", "bike", True)
drv2 = Driver("Babu", 180, "Pune", "bike", True)
drv3 = Driver("Pappu", 132, "Mumbai", "bike", True)
drv4 = Driver("Shubham", 690, "Latur", "car", True)

Drivers = [drv1, drv2, drv3, drv4]
Users = {}
Users["demo acc"] = User("prem", 100, "Satara")       #comment this out to disable demo account.

def createusr():
	global Users
	usrname = input("Enter Username: ")
	if usrname in Users:
		print(f"Username is not available: {usrname}")
	else:
		rlname = input("Enter your name: ")
		phonenum = input("Enter phone number: ")
		address = input("Enter Address: ")
		Users[usrname] = User(rlname, phonenum, address)
		print(f"\nUser Account added: {usrname}\n")

def showUsers():
	if len(Users) == 0:
		print("\nNo users available.\n")
	else:
		print("\nList of available users: ")
		for num, item in enumerate(Users, start=1):
			print(f"{num}. {item}")
		print("\n")

def callUber():
	if len(Users) != 0:
		while True:
			showUsers()
			curracc = input("Choose acc: ")
			if curracc in Users:
				veruser = curracc
				print("Selected User:",veruser)
				break
			else:
				print("Invalid user.")
				print("Try again.")
		while True:
			print("Choose vehicle preference: ")
			print("""1. Car
2. Bike
3.N/A""")
			choice = input("Choose: ").lower().strip()
			match choice:
				case "1":
					veh = "car"
					break
				case "2":
					veh = "bike"
					break
				case "3":
					veh = "N/A"
					break
				case _:
					print("Invalid input, try again.")

		while True:
			dist = input("Distance from location(km): ")
			if dist.isdigit():
				print(f"Distance set to: {dist}km")
				distance = int(dist)
				break
			else:
				print("Invalid input, try again.")
		for item in Drivers:
			if item.vehicle == veh and item.available == True:
				seldrv = item
				break
		else:
			print("No drivers currently available.")
			return
		if seldrv.vehicle == "car":
			rfare = distance * 20
		else:
			rfare = distance * 10
		r1 = Ride(Users[veruser], seldrv, dist, rfare, veh)
		print(r1)
		print("Driver will be soon at your location.")
	else:
		print("Create a user account first.")
		createusr()


print("Welcome to Prem's Uber!")
while True:
	print("""Services:
1.Create user account
2.Call Uber
3.All accounts
4.Exit """)
	choice = input("Choose: ").strip()
	match choice:
		case "1":
			createusr()
		case "2":
			callUber()
		case "3":
			showUsers()
		case "4":
			print("Exiting..")
			sys.exit()

