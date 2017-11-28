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