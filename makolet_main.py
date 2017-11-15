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
	def __init__(self, first_name, last_name, email):
		#TODO: I had to remove the password parameter for the constructor, because
		#we have them set their passwords below. Maybe we should make a subclass that refers to a new User, and add
		#And then make this a separate class?
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		#self.password = password
		#self.address = address
		#self.purchase_history = purchase_history

		#The folllowing is the code to create a new password
		lowercase_letters = 'abcdefghijklmnopqrstuvwxyz' #reference to check if lowercase in password
		uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #reference to check if uppercase in password
		num_sym = "`1234567890-=[]\;',./~!@#$%^&*()_+{}|:<>?" #reference to check if nums or syms in password

	    #Loop that ensures user enters the same password twice, that the password includes the correct type of characters, and is not in the 'bad_password' list.
	    legal_password = False
	    while legal_password == False:
	        print("Please enter a new password for your account.\n)
			print("It must be at least " + str(min_characters) + " characters.\n")
			print("It must include an uppercase letter, a lowercase letter and a number/symbol")
			#Have them re-enter the password.
	        re_new_password = input("Please re-enter your password:\n")
	        #The following sequence tests the password if its less than the min # of characters needed, and if it contains the required types of characters
	        if new_password == re_new_password: #If the password strings are equal
	            if len(re_new_password) >= min_characters:
	            #If the password is at least the minimum character length
	            	for char in re_new_password:
						if char not in lowercase_letters:
							print("You did not include a lowercase letter.\n")
								continue
						elif char not in uppercase_letters:
							print("You did not include an uppercase letter.\n")
								continue
						elif char not in num_sym:
	                    print("You did not include a number or a symbol.\n")
							continue
						else:
							print("<DEBUG> Your password meets character requirements.")
	        	else: #if password is not minimum length required
					print("Your password is not of the minimum length required.")
					continue
			else:
	            print("That was not the same password. Try again.\n")
	            #The loop restarts immediately if both passwords are not equal
	            continue
			#If all requirements are met:
	        print("Your passwords are the same, and meet all of the requirements. Congratulations.\n")
	        #Passwords are the same, and meet all of the parameters as set when calling the function. Therefore the loop breaks and it returns the legal password value.
			self.password = re_new_password
	        legal_password = True
	        #Legal password has been entered twice, Loop ends, program continues.

	def get_first_name(self):
		return self.first_name

	def get_last_name(self):
		return self.last_name

	def get_email(self):
		return self.email

	def get_password(self):
		return self.password

zseltzer = User('Zev', 'Seltzer', 'zev123@gmail.com') #create a new user, Zev

#print('zseltzer.get_first_name:', zseltzer.get_first_name()) #test User object initiation

def user_login(): #TODO: Complete this user_login function
	print('Welcome to the Login Page')
