from appJar import gui

def validateCredentials():
	""" Called when user presses submit button to log in to an existing account"""
	pass

def user_login(): #TODO: Complete this user_login function
	login = gui("Existing User Login Page")
	login.setGeometry("600x700")
	login.setResizable(False)
	login.setExpand("column")
	login.setLocation("CENTER")
	login.setTitle("Login Page")
	login.setStretch("column")
	login.setFont(30)
	login.addLabel("user_label", "Email:", 0, 0)
	login.addEntry("email", 0, 1)
	login.addLabel("password_label", "Password:", 1, 0)
	login.addEntry("password", 1, 1)
	login.setFocus("email")
	login.go()
	
user_login()