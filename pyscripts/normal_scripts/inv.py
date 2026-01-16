#!/usr/bin/env python3
inventory = [["moonveil", 1], ["runes", 500], ["flask", 7]]
backup = []
while True:
	print("\n*****************************")
	print("1.View inventory \n2.Add item \n3.Remove item \n4.Clear inventory \n5.Total amout of item \n6.Backup \n7.Exit ")
	choice = input("Choose: ").strip()
	match choice:
		case "1":
			inventory.sort()
			print("\nList of items: ")
			for num, (item, qty) in enumerate(inventory, start=1):
				print(f"{num}. {item} x{qty}")
			print(f"Total items: {len(inventory)}")
		case "2":
			item = input("Enter item: ").strip()
			amount = int(input("Enter amount: "))
			for i in inventory:
				if i[0] == item:
					i[1] += amount
					print(f"Added {item} x{amount}")
					break
			else:
				inventory.append([item, amount])
				print(f"Added {item} x{amount}")
		case "3":
			item = input("Enter item: ")
			for i in inventory:
				if i[0] == item:
					if i[1] > 1:
						amount = int(input("Enter amount: "))
						if amount < i[1]:
							i[1] -= amount
							print(f"removed {item} x{amount}. Remaining: {i[1]} ")
						elif i[1] == amount:
							inventory.remove(i)
							print(f"removed {item} x{amount}")
						else:
							print("invalid amount")
					else:
						inventory.remove(i)
						print(f"removed {item}")
					break
			else:
				print("item does not exist")
		case "4":
			inventory.clear()
			print("inventory cleared")
		case "5":
			item = input("Enter item: ")
			for i in inventory:
				if i[0] == item:
					print(f"{item} x", i[1])
					break
			else:
				print("item does not exist")
		case "6":
			print("\n1.Create backup \n2.restore backup")
			choose = input("\nchoose: ")
			if choose == "1":
				backup = inventory.copy()
				print("Backup created...")
			elif choose == "2":
				if backup:
					inventory = backup.copy()
					print("inventory restored...")
				else:
					print("No backup found")
			else:
				print("Invalid input")
		case "7":
			print("Exiting...")
			break
		case _:
			print("Invalid input")
