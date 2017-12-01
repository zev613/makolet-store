################################################################
#	makolet_main.py, part of Zev and Harry's Final Project
################################################################

import json
import sys
import password
from appJar import gui
#import smtplib
#from email.mime.multipart import MIMEMultipart
#from email.mime.text import MIMEText

users = {}

inventory = {} #Dictionary that represents the entire store's Inventory

user_logged_in = False
current_user = {}

json_data = json.load(open('users.json')) #load user database from json file
users.update(json_data) #update empty user dictionary from the json file

inventory_data = json.load(open('inventory.json')) # load inventory json file
inventory.update(inventory_data)

def button_press(button):
	if button == "My Account":
		print("This will take you to the My Account page")
		#TODO: make and then call the My Account GUI
	elif button == "Log Out":
		print("This will take you to the My Account page")
		#TODO: Make and then call Log Out GUI

def buy_button_press(button):
	if button == "Buy Now":
		print("This will let you buy the item as long as your account has enough of a Balance")
		#TODO: This will check user's balance, if there is enough money, buys it after being pressed, and takes the user to the Shipping Page, has them confirm the info is correct, then will send a "order confirmation" email using smtp. Then will send them back to Homepage.

def top_menu_press(menu_option):
	print("This will call the specific function for each category, depending on which one is clicked.")
	#TODO: Make functions that draw the GUI page for each category, then call from here.

def make_inventory_page(category):
	inv_cat = inventory[category]
	win_inv_1 = gui("Inventory Main", "600x800")
	win_inv_1.setBg("white")
	win_inv_1.setFg("black")
	win_inv_1.setSticky("news")
	win_inv_1.setExpand("both")
	win_inv_1.setFont(10)
	menu_options = ["Homepage"] + [category for category in inventory.keys()]
	win_inv_1.addMenuList("Makolet®", menu_options, top_menu_press)
	win_inv_1.addLabel("logo", "Makolet®", 0, 0)
	win_inv_1.addLabel("category", category, 0, 1)
	win_inv_1.addLabel("blank_label_1", "", 0, 2) #(len(inv_cat) - 3))
	win_inv_1.addButton("My Account", button_press, 0, 3)#(len(inv_cat) - 2))
	win_inv_1.addButton("Log Out", button_press, 0, 4)#(len(inv_cat) - 1))
	
	item_acc = 0
	num_page = len(inv_cat.keys()) % 5
	for item  in inv_cat.keys():
		item_acc += 1
		win_inv_1.addImage(item, inv_cat[item]["image"], 1, item_acc)
		win_inv_1.addLabel(inv_cat[item]["name"], inv_cat[item]["name"], 2, item_acc)
		win_inv_1.addLabel(inv_cat[item]["name"] + "_price", "$" + str(inv_cat[item]["price"]).center(2), 3, item_acc)
		win_inv_1.addButton("Buy Now" + "   '" + str(item_acc) + "'", buy_button_press, 4, item_acc)
		win_inv_1.addLabel(inv_cat[item]["name"] + "_rating", str(inv_cat[item]["rating"]) + "/5 stars".center(2), 5, item_acc)
		win_inv_1.startToggleFrame("More Info" + "     " + str(item_acc), 6, item_acc)
		this_other_info = ""
		for info in inv_cat[item]["other_info"].keys(): #creates a string where each piece of information in other_info is printed, with newlines. This will fill the other_info Label.
			this_other_info += str(info) + " : " + str(inv_cat[item]["other_info"][info]) + "\n"
		win_inv_1.addLabel(inv_cat[item]["name"] + "_other_info", this_other_info, 6, item_acc)
		win_inv_1.stopToggleFrame()
	win_inv_1.go()

#make_inventory_page("Books") #Create inventory page for "Books"

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
	make_inventory_page(category)

class User():
	'''Makes a new user with the specified attributes, then have user create a new password'''
	def __init__(self, first_name, last_name, email, address):
		'''I had to remove the password parameter for the constructor because
		we have them set their passwords below. Maybe we should make a subclass that refers to a new User, and add
		And then make this a separate class?'''
		
		#Reference Strings to compare for password requirements
		self.first_name = first_name
		self.last_name = last_name
		valid_email = False #flag var to check for valid email address
		while valid_email == False: #while email invalid
			if '@' and '.' not in email: #Email must have a '@' and a '.' in it.
				email = input("You entered an invalid email address, please type it again.") #if it does not, have re-enter their email address.
				continue
		self.email = email #set email to instance var.
		self.address = address
		#self.purchase_history = purchase_history

		#The folllowing is the code to create a new password
		self.password = password.new_password(self.email) #calls new_password, which returns a valid password entered by user

	def get_first_name(self):
		return self.first_name

	def get_last_name(self):
		return self.last_name

	def get_email(self):
		return self.email

	def get_password(self):
		return self.password
	
	def get_address(self):
		return self.address

zseltzer = User('Zev', 'Seltzer', 'zev123@gmail.com') #create a new user, Zev
want_recovery = input("Would you like to recover your password? Type yes or no").lower()
if want_recovery in ['yes', 'y']:
	password.password_recovery(zseltzer.get_email()) #call password_recovery function in password.py

#print('zseltzer.get_first_name:', zseltzer.get_first_name()) #test User object initiation

def user_login(): #TODO: Complete this user_login function
	print('Welcome to the Login Page')