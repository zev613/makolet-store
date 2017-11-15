import json
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user_logged_in = False

user_quit = False
while user_quit == False:
	print("Welcome to Makolet®, the Text-Based Store™\n")
	print("Please select one of the following menu choices, using its corresponding keyword:\n")
	print(" * Login for Existing Users  -  to select type: 'login' or 'log in'")
	print(" * Create a New Account  -  to select type: 'create account' or 'create user'")
	print(" * Quit Menu  -  to select type: 'quit' or 'exit'")
	choice = input("Type your choice:\n")
	valid_choices = ['login', 'log in', 'create account', 'create user', 'quit', 'exit']
	while choice not in valid_choices:
		print("Your choice was not one of the options listed. Please try again.")
		choice = input("Type your choice:\n")
	if choice == 'login' or choice == 'log in':
		print("Go to Login Menu")
		#make login function, called from here.
	elif choice == 'create account' or 'create user':
		print("Go to Create Account Menu")
		#make new account function, called from here.
	elif choice == 'quit' or choice == 'exit':
		print("Sorry to see you leave. Thank you for shopping with Makolet®, the Text-Based Store™\nGoodbye")
		#Store User back into database
		user_quit = True
		sys.exit()

json_data = json.load(open('database.json'))
users.update(json_data)
