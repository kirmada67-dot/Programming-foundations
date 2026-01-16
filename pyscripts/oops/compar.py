#!/usr/bin/env python3
class Order():
	def __init__(self, item, price):
		self.item = item
		self.price = price
	def showList(self):
		print(f"item = {self.item} \nprice = {self.price}")
	def __gt__(self, ord2):
		return self.price > ord2.price
	def __lt__(self, ord2):
		return self.price < ord2.price
ord1 = Order("snacks", 1)
ord2 = Order("pen", 10)
ord1.showList()
ord2.showList()
print(ord1 > ord2)
