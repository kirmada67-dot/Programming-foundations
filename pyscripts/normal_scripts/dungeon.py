#!/usr/bin/env python3
import random
monsters = ['goblin', 'wolf', 'undead', 'tree gaurdian']
torches = 3
print("Young tarnished, you are lost in the dungeon")
while torches > 0:
	monster = random.choice(monsters)
	move = input("Choose where to go (forward/right/left/dark path/skull yard/near the door): ").lower().strip()
	if move == "right":
		print(f"You encountered a {monster} but slained it and got out of dungeon!")
		exit ()
	else:
		print(f"You encounteret a {monster} but slained it and moved deeper into the dungeon...")
	torches -= 1
	print(f"You have {torches} torches left.")
print(f"You moved deeper and deeper into dungeon as your torch fades darkness coveres your path...")
