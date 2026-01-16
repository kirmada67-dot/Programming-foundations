#!/usr/bin/env python3
class Banking():
	bal = 0
	def __init__(self, acc_no, bal):
		self.acc_no = acc_no
		self.bal = bal
	def check_bal(self):
		print(f"Rs.{self.bal}")
	def credit(self):
		while True:
			ammount = input("Enter ammount to be credited(enter stop to exit): ")
			if ammount.isdigit():
				num = int(ammount)
				self.bal += num
				print(f"{ammount}: ammount has been credited to your account")
				break
			elif ammount == "stop":
				print("Exiting...")
				break
			else:
				print("Invalid ammount.")

	def debit(self):
		if self.bal > 0:
			while True:
				ammount = input("Enter ammount to be debited(enter stop to exit): ")
				if ammount.isdigit():
					num = int(ammount)
					if num <= self.bal:
						self.bal -= num
						print(f"{ammount}: ammount has been debited from your account")
						break
					else:
						print("Insufficient funds in account.")
						print(f"available funds: {self.bal}")
				elif ammount == "stop":
					print("Exiting...")
					break
				else:
					print("Invalid input.")
		else:
			print("Insufficient funds in account.")




acc1 = Banking(1234, 1000)
acc1.check_bal()



