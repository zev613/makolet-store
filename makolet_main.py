################################################################
#	makolet_main.py, part of Zev and Harry's Final Project
################################################################

import json
import sys
import passwd
from appJar import gui
import smtp2
from datetime import datetime

uppercase_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_alpha = "abcdefghijklmnopqrstuvwxtz"
num_sym = "`1234567890-=[]\;',./~!@#$%^&*()_+{}|:<>?"

users = {}
inventory = {} #Dictionary that represents the entire store's Inventory

global first_name
first_name = "John"
global last_name
last_name = "Smith"
global email
email = "jsmith@fandm.edu"
global password
password = "password"
global re_password
re_password = "password"
global current_user
current_user = "jsmith@fandm.edu"
user_logged_in = False

json_data = json.load(open('users.json')) #load user database from json file
users.update(json_data) #update empty user dictionary from the json file

inventory_data = json.load(open('inventory.json')) # load inventory json file
inventory.update(inventory_data)

def menu_button_press(button):
	if button == "My Account":
		print("This will take you to the My Account page")
		app.showSubWindow("My Account")
		app.hideSubWindow("Inventory")
	elif button == "Log Out":
		print("This will take you to the My Account page")
		user_logged_in = False
		current_user = ""
		app.hideSubWindow("Inventory")

def buy_button_press(button):
	item_name = button.replace("_Button", "")
	item_category = ""
	"""since the button function can't pass additional parameters, need to go through whole Inventory until find this item, and record what category it is in."""
	for category in inventory:
		for item in inventory[category]:
			if inventory[category][item]["name"] == item_name: #if name value is same as the first half of Button name
				item_category = category
				print("<LOG>: category", category)
	
	item_ref_dict = inventory[category][item_name]
	item_price = item_ref_dict["price"]
	item_quantity = item_ref_dict["quantity"]
	user_balance = users[current_user]["account_info"]["balance"]
	if item_quantity <= 0: #Store doesn't have any in stock
		print("<LOG>: Item Quantity is 0")
		app.errorBox("quantity_zero", "We do not have any of this item in stock currently. Check back later.", parent="Inventory")
	elif item_price > user_balance: #User doesn't have enough funds to pay for it
		print("<LOG>: User's balance is not enough to buy item.")
		app.errorBox("balance_too_low", "You do not have sufficient funds to pay for this item.\nPlease add more funds or select a different item.", parent="Inventory")
	else:
		"""Follow buys the item, subtracting price from the balance, subtracts 1 from quantity"""
		user_balance -= item_price #remove the funds necessary to buy this item from user's balance
		print("<LOG>: subtracted price from balance")
		item_quantity -= 1 #remove 1 quantity of the item from stock
		users[current_user]["account_info"]["purchase_history"][item_name] = {} #add empty dictionary with purchase_history, key is item_name
		if category == "Books":
			manufacturer = inventory[category][item_name]["other_info"]["publisher"]
		elif category == "Electronics":
			manufacturer = inventory[category][item_name]["other_info"]["manufacturer"]
		elif category == "Movies":
			manufacturer = inventory[category][item_name]["other_info"]["studio"]
		elif category == "Music":
			manufacturer = inventory[category][item_name]["other_info"]["artist"]
		else:
			print("<LOG>: Category not found??")
		users[current_user]["account_info"]["purchase_history"]["manufacturer"] = manufacturer
		users[current_user]["account_info"]["purchase_history"]["department"] = category
		users[current_user]["account_info"]["purchase_history"]["quantity"] += 1
		users[current_user]["account_info"]["purchase_history"]["cost"] = item_price
		users[current_user]["account_info"]["purchase_history"]["date_time_purchased"] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		#TODO: Implement date/time tracking -- records when a user bought an item, and stores that in the purchase_history dictionary.

#Check if user's Balance is enough to buy it.
	
	#TODO: This will check user's balance, if there is enough money, buys it after being pressed, and takes the user to the Shipping Page, has them confirm the info is correct, then will send a "order confirmation" email using smtp. Then will send them back to Homepage.

def press_my_account_menu(button):
	"""Controls the menu buttons for the 'My Account' sub-window"""
	if button == "Back to Store":
		app.showSubWindow("Inventory")
		print("<LOG>: Back to Inventory")
		app.hideSubWindow("My Account")
	elif button == "Sign Out":
		print("<LOG>: Logging out.")
		global user_logged_in #define global vars
		global current_user
		global email
		global first_name
		global last_name
		global password
		global re_password
		user_logged_in = False
		current_user = ""
		email = ""
		first_name = ""
		last_name = ""
		password = ""
		re_password = ""
		app.hideSubWindow("My_Account")
	else:
		print("<LOG>: Option not found.")

def press_new_user(button):
	if button == "Create your Account":  # Submit new Acccount
		if app.getEntry("Email Address") in users:
			app.errorBox("Already have Account",
			             "You already have an existing Account.\nTaking you to User Login Page.", parent="New User")
			app.showSubWindow("User Login")  # Bring to User Login Page
			app.hideSubWindow("New User")
		elif app.getCheckBox("I Agree to the Terms") == False:
			app.errorBox("Didn't Agree to Terms",
			             "You did not agree to the terms and conditions\nYou must select 'yes' to create a Makolet Account®",
			             parent="New User")
		elif app.getEntry("Password") != app.getEntry("Re-enter Password"):
			app.errorBox("Passwords Not Matching", "Your password did not match your re-entry! Try again.",
			             parent="New User")
		elif len(app.getEntry("Password")) < 6:
			app.errorBox("Password Too Short", "Your password does not meet the length requirement. It must be at least 7 characters long.",parent="New User")
		else:
			app.infoBox("Created New Account", "Congratulations on Making a New Account!\nTaking you to the login page. Enter your new credentials there.", parent="New User")
			users[app.getEntry("Email Address")] = {"first_name": app.getEntry("First Name"), "last_name": app.getEntry("Last Name"), "password": app.getEntry("Password"), "address": ['St', 'Apt', 'City', 'State', 'Zip'], "account_info": {"balance": 0.00, "purchase_history": {"default_item": ""}}}
			with open('users.json', 'w') as outfile:
				json.dump(users, outfile)
			print("<LOG>: Added Account to users dictionary/.json")
			app.showSubWindow("User Login")
			app.hideSubWindow("New User")
	elif button == "Back":  # Go back to Welcome Page
		app.hideSubWindow("New User")
		print("Going back to Welcome Page")
	else:
		print("ERROR, NOT A VALID OPTION")

def press_welcome_button(button):
	if button == "Login":
		print("<LOG>: Going to User Login Sub Window")
		app.showSubWindow("User Login")
	elif button == "Create an Account":
		print("<LOG>: Going to New User Sub Window")
		app.showSubWindow("New User")
	elif button == "Quit":
		if app.yesNoBox("Confirm Exit", "Are you sure you want to exit the application?") == True:
			print("<LOG>: Quitting program")
			app.stop()
		else:
			print("<LOG>: Not quitting")
	else:
		print("Error!!! Not an Option")

def press_view_terms(button):
	if button == "View Terms and Conditions":
		app.infoBox("terms", "You must agree to the follow terms and conditions to use Makolet®", parent="New User")

def cancel_user_login(button):
	if button == "Cancel":
		print("Going back to Main Menu")
		app.hideSubWindow("User Login")

def press_submit_user_login(button):
	if button == "Submit":
		global email
		email = app.getEntry("Your Email")
		#print('EMAIL:', email)
		global password
		password = app.getEntry("Your Password")
		#print('PASSWORD:', password)
		if email in users:
			if password == users[email]["password"]:
				current_user = email
				logged_in = True
				app.infoBox("Welcome Back", "Welcome Back, " + users[email]["first_name"] + "!", parent="User Login")
				print("<LOG>: Taking you to Inventory logged in as your account")
				app.showSubWindow("Inventory")
				app.hideSubWindow("User Login")
			else:
				print("<DEUBG>: Password incorrect")
				if app.yesNoBox("Password Incorrect", "The password you entered is incorrect.\nWould you like us to send you your password by email?", parent="User Login") == True:
					smtp2.password_recovery(email, users[email]["password"])
					app.infoBox("recovery_sent", "Your password has been sent to the email " + email + ".", parent="User Login")
				else:
					print("<LOG>: Not sending Recovery Email")
		else:
			app.errorBox("User Not Found", "The Email you entered does not have an account.", parent="User Login")
			if app.yesNoBox("Go to New User Page", "Would you like to go to the Create Account page?", parent="User Login") == True:
				app.showSubWindow("New User")
				app.hideSubWindow("User Login")
			else:
				print("Staying on User Login Page")
	elif button == "Cancel":
		print("Going back to Main Page")
		app.hideSubWindow("User Login")
	else:
		print("<LOG>: ERROR. INVALID CHOICE")

app = gui("Makolet®", "400x500")
app.setBg("white")
app.setFg("black")
app.setSticky("news")
app.setExpand("both")
app.setFont(14)

#TODO: Add New User SubWindow, called from the Welcome Main Window.
"""Begin New User Sub-Window"""
app.startSubWindow("New User", modal = True)  # blocking=True)
app.setGeometry("400x500")
app.setStretch("both")
app.setSticky("news")
app.setFont(20)
app.startLabelFrame("Enter Account Details")
app.setFont(14)
app.addLabelEntry("Email Address")#
app.setEntryDefault("Email Address", "Enter your Email")
app.addLabelEntry("First Name")
app.setEntryDefault("First Name", "Enter your First Name")
app.addLabelEntry("Last Name")
app.setEntryDefault("Last Name", "Enter your Last Name")
app.addSecretLabelEntry("Password")
app.setEntryDefault("Password", "Enter a password")
app.addLabelValidationEntry("Re-enter Password")
app.setEntryDefault("Re-enter Password", "Type your Password again")
# Following button opens a popup, which has the Terms and Conditions
app.addButton("View Terms and Conditions", press_view_terms)
app.addCheckBox("I Agree to the Terms")
	# app.addLabelEntry("Address")
app.addButtons(["Create your Account", "Back"], press_new_user)
app.stopLabelFrame()
app.stopSubWindow()
"""End New User Sub-Window"""

"""Begin User Login Sub Window"""
app.startSubWindow("User Login", modal = True)  # blocking=True)
app.startLabelFrame("Login Details")
# these only affect the labelFrame
app.setSticky("ew")
app.setFont(20)
app.addLabel("l1", "Email: ", 0, 0)
app.addEntry("Your Email", 0, 1)
app.setEntryDefault("Your Email", "Enter your Email")
app.addLabel("l2", "Password: ", 1, 0)
app.addSecretEntry("Your Password", 1, 1)
app.setEntryDefault("Your Password", "Enter your Password")
app.addButton("Submit", press_submit_user_login, 2, 0, 1)
app.addButton("Cancel", cancel_user_login, 2, 1, 1)
app.stopLabelFrame()
app.stopSubWindow()
"""End of User Login Sub-Window"""

"""Begin Inventory Sub-Window"""
app.startSubWindow("Inventory", modal = True)  # blocking=True)
app.addLabel("logo", "Makolet®", 0, 0)
#app.addEmptyLabel("blank_1", 0, 2)  # (len(category) - 3))
app.setStretch("column")
app.setSticky("new")
app.addButton("My Account", menu_button_press, 0, 3)  # (len(category) - 2))
app.addButton("Log Out", menu_button_press, 0, 4)  # (len(category) - 1))
app.setSticky("esw")
app.setStretch("both")
app.startTabbedFrame("Inventory_Tabs", column=0, colspan=5, rowspan=4)#, colspan=4)  # Each category has a tab
item_acc = 0  # global

for category in inventory.keys():
	inv_cat = inventory[category]
	app.startTab(category)  # Add a new Tab, with category strign as text in tab
	app.startPagedWindow(category)  # begin paged window
	if len(inv_cat) % 4 == 0:
		num_pages = (len(inv_cat) // 4)  # Give num of pages needed to display items in groups of 5 items per page
		num_left_over_items = 0
	else:
		num_pages = (len(inv_cat) // 4) + 1
		num_leftover_items = len(inv_cat) % 4
	category_items = [thing for thing in inv_cat]
	print('<LOG>: len(category_items', len(category_items))
	item_acc = 0
	for item in inv_cat:
		# TODO: FIGURE OUT HOW TO MAKE EVERY 5 ITEMS APPEAR ON A NEW PAGE, WITHIN A FOR LOOP
		app.startPage()
		item_acc += 1
		app.addImage(item, inv_cat[item]["image"], 1, item_acc)
		app.addLabel(inv_cat[item]["name"], inv_cat[item]["name"], 2, item_acc)
		app.addLabel(inv_cat[item]["name"] + "_price", "$" + str(inv_cat[item]["price"]).center(2), 3, item_acc)
		app.addNamedButton("Buy Now", inv_cat[item]["name"] + "_Button", buy_button_press, 4, item_acc)
		app.addLabel(inv_cat[item]["name"] + "_rating", str(inv_cat[item]["rating"]) + "/5 stars".center(2), 5, item_acc)
		app.startToggleFrame(inv_cat[item]["name"] + "_More_Info", 6, item_acc)
		app.setToggleFrameText(inv_cat[item]["name"] + "_More_Info", "More Info")
		this_other_info = ""
		for info in inv_cat[item]["other_info"].keys():  # creates a string where each piece of information in other_info is printed, with newlines. This will fill the other_info Label.
			this_other_info += str(info) + " : " + str(inv_cat[item]["other_info"][info]) + "\n"
		app.addLabel(inv_cat[item]["name"] + "_other_info", this_other_info, 6, item_acc)
		app.stopToggleFrame()
		app.stopPage()
	app.stopPagedWindow()
	app.stopTab()
app.stopTabbedFrame()
app.stopSubWindow()
"""End Store Inventory Sub-Window"""

"""Begin My Account Sub-Window"""
#TODO: Complete the My Account Sub Window, then enable it
#TODO: Need to figure out how to use the email variable within this scope

app.startSubWindow("My Account")
app.setGeometry("400x500")
app.setSticky("news")
app.setStretch("both")
print("current_user:", current_user)
print("email: ", email)
app.addButtons(['Back to Store', "Sign Out"], press_my_account_menu)
app.startLabelFrame("Welcome " + users[current_user]["first_name"] + "!", row=1, colspan=4)
app.addLabel("")
app.startToggleFrame("purchase_history_frame", 0, 0)
app.setToggleFrameText("purchase_history_frame", "Items Purchased")
purchased_items_acc = 0
user_purchases = users[current_user]["account_info"]["purchase_history"] #make code simpler
if len(user_purchases) < 1:
	app.addLabel("no_purchased_items", "No Purchased Items", 1, 0)
for item in user_purchases.keys():
	app.addLabel("purchases_label_" + purchased_items_acc + "_title", "Item: ", 2, 0)
	app.addLabel("purchases_" + item, item, 3, 0)
	purchased_items_acc += 1

app.stopToggleFrame()
app.stopLabelFrame()
app.stopSubWindow()

"""End My Account Sub-Window"""

"""Welcome Main Page Goes Here"""
app.addLabel("welcome_label", "Welcome to Makolet®!", 0, 0)
app.addButtons(["Login", "Create an Account", "Quit"], press_welcome_button)

"""End of Welcome Main Page"""
app.go()

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
		self.password = passwd.new_password(self.email) #calls new_password, which returns a valid password entered by user

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