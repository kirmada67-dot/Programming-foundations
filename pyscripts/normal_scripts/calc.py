#!/usr/bin/env python3
import sys
def calculate(num1, opr, num2):
	match opr:
		case "+":
			return num1+num2
		case "-":
			return num1-num2
		case "/":
			if num2 != 0:
				return num1/num2
			else:
				return "Invalid input, dividing by 0."
		case "*":
			return num1*num2
		case _:
			return "Invalid inputs."
while True:
	expression = input("Enter values (example: 1 + 2): ").strip()
	if expression == "stop":
		print("Exiting...")
		sys.exit()
	parts = expression.split()
	if len(parts) == 3:
		num1, opr, num2 = parts
		result = calculate(int(num1), opr, int(num2))
		print(f"Result: {result}")
	else:
		print("Invalid inputs.")
