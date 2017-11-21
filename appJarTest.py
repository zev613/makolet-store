from appJar import gui

def press(button):
	if button == "Cancel":
		app.stop()
	else:
		usr = app.getEntry("Username")
		pwd = app.getEntry("Password")
		print("User:", usr, "Password:", pwd)
		
app = gui("Login Page", "400x200")
app.setBg("gray")
app.setFont(18)
app.addLabel("title", "welcome to Makolet")
app.setLabelBg("title", "red")

app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")

app.addButtons(["Submit", "Cancel"], press)

app.setFocus("Username")

app.go()
