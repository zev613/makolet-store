from appJar import gui

def press(name):
	if name == "Exit":
		win.stop()
	elif name == "Google Pixel XL":
		win.addImage("Pixel XL", "images/google_pixel_xl.gif")
	elif name == "Harry Potter Book 1":
		win.addImage("Harry Potter", "images/harry_potter_book_1.gif")

win = gui("Login")
win.setBg("green")
win.setFg("white")
win.setFont(16)
win.addButton("Harry Potter Book 1", press)
win.addButton("Google Pixel XL", press)
win.addButton("Exit", press)
win.go()


"""This is from the main file, was used to test getting specific items from the dictionary"""
inventory = {}

print(inventory, "\n")
print("There are:", len(inventory), "Categories in the Inventory.")
for category in inventory.keys():
	print(category, "\n")
	for item in inventory[category].keys():
		print(item, "\n")
		if "subcategory" in inventory[category][item]:
			print(inventory[category][item]["subcategory"])
		print("Image: - ", inventory[category][item]["image"])
		print("Other Info:")
		for info in inventory[category][item]["other_info"].keys():
			print(info, inventory[category][item]["other_info"][info])
		print("\n\n")