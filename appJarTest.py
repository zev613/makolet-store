from appJar import gui

def press(button):
	if button == "Cancel":
		win.stop()
	elif button == "Clear":
		win.clearEntry("Username")
		win.clearEntry("Password")
		win.setFocus("Username")
	elif button == "Submit":
		username = win.getEntry("Username")
		password = win.getEntry("Password")
		
	if username == "zseltzer@fandm.edu" and password == "my_password":
		win.infoBox("Success", "Valid Password")
	else:
		win.errorBox("Error", "Invalid password")
		
win = gui("Login", "400x200")
win.setBg("green")
win.setFg("white")
win.setFont(16)
win.addLabel("title", "Login Window")
win.setLabelBg("title", "light_green")

win.addLabelEntry("Username")
win.addLabelSecretEntry("Password")

win.addButtons(["Submit", "Clear", "Cancel"], press)

win.setFocus("Username")

win.go()
