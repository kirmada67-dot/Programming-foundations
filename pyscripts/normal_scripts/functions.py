#!/usr/bin/env python3
import sys
def boss_fight(*allies, **boss):
	print("Allies: ")
	for ally in allies:
		print(f"- {ally}")
	print("\nBOSS: ")
	for key, value in boss.items():
		print(f"- {key}: {value}")
boss_fight("morgot", "Godfrey", "Malenia", name="Elden Beast", hp=600, damage=300)
