#!/usr/bin/env python3
class Employee():
	def __init__(self, role, dept, sal):
		self.role = role
		self.dept = dept
		self.sal = sal
	def showDetails(self):
		print(f"""role = {self.role}
dept = {self.dept}
salary = {self.sal}""")

class Engineer(Employee):
	def __init__(self, name, age):
		self.name = name
		self.age = age
		super().__init__("Engineer", "IT", 75000)
	def persnolInfo(self):
		print(f"""name: {self.name}
age: {self.age}""")

prem = Employee("Senior Engineer", "Cloud computing", 200000)
prem.showDetails()
idk = Engineer("dumby", 19)
idk.showDetails()
idk.persnolInfo()
