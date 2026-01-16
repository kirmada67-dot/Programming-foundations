#!/usr/bin/env python3
import sys
print("Welcome Master, input txt file to count unique words.")
def words_checker(a):
	data = {}
	try:
		with open(a, "r") as f:
			for line in f:
				words = line.split()
				for word in words:
					if word in data:
						data[word]+=1
					else:
						data[word] = 1
		for num, (word, count) in enumerate(data.items(), start=1):
			print(f"{num}. {word}: {count}")
	except FileNotFoundError:
		print(f"{filename} not found.")

while True:
	filename = input("Choose file (stop to exit): ")
	if filename == "stop":
		print("Exiting")
		sys.exit()
	else:
		words_checker(filename)
