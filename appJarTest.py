from appJar import gui
import smtp2

#Initialize Vars for Later
first_name = ""
last_name = ""
email = ""
password = ""
re_password = ""

current_user = ""
user_logged_in = False

users = {}

inventory = {}

uppercase_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_alpha = "abcdefghijklmnopqrstuvwxtz"
num_sym = "`1234567890-=[]\;',./~!@#$%^&*()_+{}|:<>?"

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

def press_new_user(button):
	if button == "Create your Account": #Submit new Acccount
		"""Will test if account info is valid, but haven't written it yet"""
		if email.lower() in users.keys():
			app.errorBox("Already have Account", "You already have an existing Account.\nTaking you to User Login Page.", parent="New User")
			app.showSubWindow("User Login") #Bring to User Login Page
			app.hideSubWindow("New User")
		elif app.getRadioButton("Agree Terms") != "No":
			app.errorBox("Didn't Agree to Terms", "You did not agree to the terms and conditions\nYou must select 'yes' to create a Makolet Account®", parent="New User")
		elif password != re_password:
			app.errorBox("Passwords Not Matching", "Your password did not match your re-entry! Try again.", parent="New User")
		elif len(password) < 6:
			app.errorBox("Password Too Short", "Your password does not meet the length requirement. It must be at least 7 characters long.", parent="New User")
		else:
			app.infoBox("Created New Account", "Congratulations on Making a New Account!\nTaking you to the login page. Enter your new credentials there.", parent="New User")
			users[email] = {"first_name": first_name, "last_name": last_name, "password": password, "address": ['St', 'Apt', 'City', 'State', 'Zip'], "account_info": {"balance" : 0.00, "purchase_history" : {}}}
			print("<DEBUG>: Added Account to users dictionary/.json")
			app.showSubWindow("User Login")
			app.hideSubWindow("New User")
	elif button == "Back": #Go back to Welcome Page
		app.hideSubWindow("New User")
		print("Going back to Welcome Page")
	else:
		print("ERROR, NOT A VALID OPTION")

def press_welcome_button(button):
	if button == "Login":
		print("<DEBUG>: Going to User Login Sub Window")
		app.showSubWindow("User Login")
	elif button == "Create an Account":
		print("<DEBUG>: Going to New User Sub Window")
		app.showSubWindow("New User")
	else:
		print("Error!!!")

def press_view_terms(button):
	if button == "View Terms and Conditions":
		app.infoBox("terms", "You must agree to the follow terms and conditions to use Makolet®", parent = "New User")

def press_submit_user_login(button):
	if button == "Submit":
		if email in users.keys():
			if password == users[email]["password"]:
				current_user = email
				logged_in = True
				app.infoBox("Welcome Back", "Welcome Back, " + users[email]["first_name"] + "!", parent="User Login")
				print("<DEBUG>: Taking you to Inventory logged in as your account")
				app.showSubWindow("Inventory")
				app.hideSubWindow("User Login")
			else:
				print("<DEUBG>: Password incorrect")
				if app.yesNoBox("Password Incorrect", "The password you entered is incorrect.\nWould you like us to send you your password by email?", parent="User Login") == True:
					smtp2.password_recovery(email, users[email]["password"])
				else:
					print("<LOG>: Not sending Recovery Email")
		else:
			app.errorBox("User Not Found", "The Email you entered does not have an account.", parent="User Login")
			if app.yesNoBox("Go to New User Page", "Would you like to go to the Create Account page?", parent="User Login") == True:
				app.showSubWindow("New User")
				app.hideSubWindow("User Login")
			else:
				print("Staying on User Login Page")
	else:
		print("<DEBUG>: ERROR. INVALID CHOICE")

app = gui("Makolet®", "400x500")
app.setBg("white")
app.setFg("black")
app.setSticky("news")
app.setExpand("both")
app.setFont(14)

# TODO: Add New User SubWindow, called from the Welcome Main Window.
"""Begin New User Sub-Window"""
app.startSubWindow("New User", modal = True)#blocking=True)
app.setGeometry("400x500")
app.setStretch("both")
app.setSticky("news")
app.setFont(20)
app.startLabelFrame("Enter Account Details")
app.setFont(14)
app.addLabelEntry("Email Address")
app.setEntryDefault("Email Address", "Enter your Email")
app.addLabelEntry("First Name")
app.setEntryDefault("First Name", "Enter your First Name")
first_name = app.getEntry("First Name")
app.addLabelEntry("Last Name")
app.setEntryDefault("Last Name", "Enter your Last Name")
last_name = app.getEntry("Last Name")
app.addSecretLabelEntry("Password")
app.setEntryDefault("Password", "Enter a password")
password = app.getEntry("Password")
app.addLabelValidationEntry("Re-enter Password")
app.setEntryDefault("Re-enter Password", "Type your Password again")
re_password = app.getEntry("Re-enter Password")
#Following button opens a popup, which has the Terms and Conditions
app.addButton("View Terms and Conditions", press_view_terms)
app.addRadioButton("Agree Terms", "I agree to the Terms")
#app.addLabelEntry("Address")
app.addButtons(["Create your Account", "Back"], press_new_user)
app.stopLabelFrame()
app.stopSubWindow()
"""End New User Sub-Window"""

"""Begin User Login Sub Window"""
app.startSubWindow("User Login", modal = True)#blocking=True)
app.startLabelFrame("Login Details")
# these only affect the labelFrame
app.setSticky("ew")
app.setFont(20)
app.addLabel("l1", "Email: ", 0, 0)
app.addEntry("Your Email", 0, 1)
app.setDefaultEntry("Enter your Email", "Your Email")
email = app.getEntry("Your Email")
app.addLabel("l2", "Password: ", 1, 0)
app.addEntry("Your Password", 1, 1)
app.setDefaultEntry("Enter your Password", "Your Password")
password = app.getEntry("Your Password")
app.addButton("Submit", press_submit_user_login, 2, 0, 1)
app.addButton("Cancel", app.hideSubWindow("User Login"), 2, 1, 1)
app.stopLabelFrame()
app.stopSubWindow()
"""End of User Login Sub-Window"""

"""Begin Inventory Sub-Window"""
app.startSubWindow("Inventory", modal = True)# blocking=True)
# menu_options = ["Homepage"] + [category for category in inventory.keys()]
# app.addMenuList("Makolet®", menu_options, top_menu_press)
app.addLabel("logo", "Makolet®", 0, 0)
# app.addLabel("category", category, 0, 1)
app.addEmptyLabel("blank_1", 0, 2)  # (len(category) - 3))
app.addButton("My Account", button_press, 0, 3)  # (len(category) - 2))
app.addButton("Log Out", button_press, 0, 4)  # (len(category) - 1))
app.startTabbedFrame("Inventory_Tabs")  # Each category has a tab
item_acc = 0  # global
for category in inventory.keys():
	inv_cat = inventory[category]
	app.startTab("Tab_" + category)  #Add a new Tab, with category strign as text in tab
	app.setTabText(category, "Tab_" + category)
	
	app.startPagedWindow("Page_" + category)  # begin paged window
	if len(inv_cat) % 5 == 0:
		num_pages = (len(inv_cat) // 5) # Give num of pages needed to display items in groups of 5 items per page
		num_left_over_items = 0
	else:
		num_pages = (len(inv_cat) // 5) + 1
		num_leftover_items = len(inv_cat) % 5
	item_acc = 0
	for item in inv_cat:
		# TODO: FIGURE OUT HOW TO MAKE EVERY 5 ITEMS APPEAR ON A NEW PAGE, WITHIN A FOR LOOP
		app.startPage()
		item_acc += 1
		app.addImage(item, inv_cat[item]["image"], 1, item_acc)
		app.addLabel(inv_cat[item]["name"], inv_cat[item]["name"], 2, item_acc)
		app.addLabel(inv_cat[item]["name"] + "_price", "$" + str(inv_cat[item]["price"]).center(2), 3, item_acc)
		app.addButton("Buy Now" + "   '" + str(item_acc) + "'", buy_button_press, 4, item_acc)
		app.addLabel(inv_cat[item]["name"] + "_rating", str(inv_cat[item]["rating"]) + "/5 stars".center(2), 5,
		             item_acc)
		app.startToggleFrame("More Info" + "     " + str(item_acc), 6, item_acc)
		this_other_info = ""
		for info in inv_cat[item][
			"other_info"].keys():  # creates a string where each piece of information in other_info is printed, with newlines. This will fill the other_info Label.
			this_other_info += str(info) + " : " + str(inv_cat[item]["other_info"][info]) + "\n"
		app.addLabel(inv_cat[item]["name"] + "_other_info", this_other_info, 6, item_acc)
		app.stopToggleFrame()
		app.stopPage()
	app.stopPagedWindow()
	app.stopTab()
app.stopTabbedFrame()
app.stopSubWindow()
"""End Store Inventory Sub-Window"""

"""Welcome Main Page Goes Here"""
app.addLabel("welcome_label", "Welcome to Makolet®!", 0, 0)
app.addButtons(["Login", "Create an Account"], press_welcome_button)
app.go(startWindow = "User Login")
app.go(startWindow = "New User")

"""End of Welcome Main Page"""
app.go()