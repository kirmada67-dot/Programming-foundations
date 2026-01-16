#!/usr/bin/env python3
students = {"prem": 69, "harsh": 0, "Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 90, "Ethan": 88}
print(students)
students.update({"Mimi": 100})
print(students)
students.pop("Alice")
students.update({"Mimi": 1000})
print(students)
for name, marks in students.items():
	print(f"{name} scored {marks} in exam!")
if "Mimi" in students:
	print("Mimi exists is students and she is a topper! ")
if "lalit" in students:
	print("yes he does idk how")
else:
	print("no he doesnt")
print(students.get("Mimi"))
print(students.get("prem", "N/A"))
students.clear()
print(students)
