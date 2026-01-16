#!/usr/bin/env python3
def training():
	xp = 0
	def defeating():
		nonlocal xp
		xp += 50
		print(f"inner xp:{xp}")
	defeating()
	defeating()
	defeating()
	print(f"outer xp:{xp}")
training()
