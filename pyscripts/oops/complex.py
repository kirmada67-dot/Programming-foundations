#!/usr/bin/env python3
class Complex():
	def __init__(self, real, img):
		self.real = real
		self.img = img
	def shownum(self):
		print(self.real, "i +", self.img, "j")

	def __add__(self, secnum):
		return Complex((self.real + secnum.real), (self.img + secnum.img))
	def __sub__(self, secnum):
                return Complex((self.real - secnum.real), (self.img - secnum.img))



num1 = Complex(5, 8)
num1.shownum()
num2 = Complex(6, 2)
num2.shownum()
num3 = num1 + num2
num3.shownum()
num4 = num3 - num1
num4.shownum()
