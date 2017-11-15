################################################################
#	makolet_main.py, part of Zev and Harry's Final Project
################################################################

import json
import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

users = {} #probably to remove

user_logged_in = False
current_user = {}
user_quit = False #flag var for main while loop
while user_quit == False:
	print("Welcome to Makolet®, the Text-Based Store™\n")
	print("Please select one of the following menu choices, using its corresponding keyword:\n") #print menu choices
	print(" * Login for Existing Users  -  to select type: 'login' or 'log in'")
	print(" * Create a New Account  -  to select type: 'create account' or 'create user'")
	print(" * Quit Menu  -  to select type: 'quit' or 'exit'")
	choice = input("Type your choice:\n") #get user choice for menu
	valid_choices = ['login', 'log in', 'create account', 'create user', 'quit', 'exit'] #possible options to check if valid
	while choice not in valid_choices: #if choice not valid,
		print("Your choice was not one of the options listed. Please try again.") #have the user try again
		choice = input("Type your choice:\n") #get new value for choice
	if choice == 'login' or choice == 'log in': #if user picks 'login'
		print("Go to Login Menu") #TODO: create login function, and call it here.
		#THE LOOP WILL CONTINUE GOING UNTIL SOMETHING STOPS IT, SUCH AS INPUT. MAY NEED TO CHANGE THE LOGIC FLOW
		#make login function, called from here.
	elif choice == 'create account' or 'create user':
		print("Go to Create Account Menu")
		#make new account function, called from here.
	elif choice == 'quit' or choice == 'exit': #if user wants to quit
		print("Sorry to see you leave. Thank you for shopping with Makolet®, the Text-Based Store™\nGoodbye")
		#Store User back into database
		user_quit = True #set flag var for main loop
		sys.exit() #quit program

json_data = json.load(open('database.json')) #load user database from json file
users.update(json_data) #update empty user dictionary from the json file

class User():
	"""Makes a new user with the specified attributes"""
	def __init__(self, first_name, last_name, email, password):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
		#self.address = address
		#self.purchase_history = purchase_history
	
	def get_first_name(self):
		return self.first_name
	
	def get_last_name(self):
		return self.last_name
	
	def get_email(self):
		return self.email
	
	def get_password(self):
		return self.password
	
zseltzer = User('Zev', 'Seltzer', 'zev123@gmail.com', "Zev'sPassword123") #create a new user, Zev

print('zseltzer.get_first_name:', zseltzer.get_first_name())
	
	

def user_login(): #TODO: Complete this user_login function
	print('Welcome to the Login Page')