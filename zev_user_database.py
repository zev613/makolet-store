import json
from passwd import *
import sys

#These were the original user files before I created the json file
'''
users = {"dfrank": {"user_name": "dfrank", "first_name": "David", "last_name":"Frank", "password": "T00tsieRoll"}, "jsmith" :
{"user_name": "jsmith", "first_name": "John", "last_name": "Smith", "password": "New_York_City"}
, "mbrown": {"user_name": "mBrown", "first_name": "Mary", "last_name": "Brown", "password": "IH8Computers"}
, "sKaplan": {"user_name": "sKaplan", "first_name": "Samuel", "last_name": "Kaplan", "password": "DesktopLamp1"}}
'''

#didctionary that is used when program runs, then is dumped to database.json
users = {}

#Loads .json file with previous user entries.
json_data = json.load(open('database.json'))
users.update(json_data)

#The following function is called if the user enters 'y', that they want to create a new user. It then will ask the user for input to give their first and last names.
def new_user_query():
	#User types their first name. Then we call .lower() on it to ensure all values in database are the same case.
    new_first_name = input("Please enter your First Name. Must be at least 2 characters long:  ").lower()
	#User types their last name. Then we call .lower() on it to ensure all values in database are the same case.
    new_last_name = input("Please enter your Last Name. Must be at least 2 characters long:   ").lower()
	#Then create a username for that user, which takes the first character of the first name, and the whole last name. For example: 'zseltzer'
    new_username = new_first_name[0] + new_last_name
	#print username for Debugging
    print("User_name is: " + new_username)

#Once we have the first_name, last_name and username, we call the new_password function. This function is located in passwd.py.

#The function returns the password once the user types it twice, and the program tests that the password fits the requirement arguments

#These can include minimum number of characters to make it a valid password, and 3 Booleans that set what types of characters must be in this password.

#In this case, we have the user create a password that requires lowercase AND uppercase letters, in addition to numbers or symbols in the string.

#The new_password value is equal to the string that the new_password() function returns.

    new_user_password = new_password(8, True, True, True)
    users.update({new_username : make_user(new_first_name, new_last_name, new_user_password, new_username)})
    print("Taking you back to Main Menu....")
    main_menu()

    #call the make_user function, which takes a first_name, last_name username and user_password arguments.
    #The make_user function is separate from the new_user_query function to allow us to create a formatted dict value for any user, even if those values aren't entered in the new_user_query().

def make_user(first_name_arg, last_name_arg, new_password_arg, new_username_arg):
	#This function returns a complete dict value, complete with all 4 values it needs: "first_name", "last_name", "user_name", and "password"
	return {"user_name": new_username_arg, 'first_name': first_name_arg, 'last_name': last_name_arg, 'password': new_password_arg}

print("Thank you for using the User Database, powered by 'JSON'.\n")

# Main Block of the Code starts here.
#Loop that requires user to input 'y' or 'n', depending on if they want to create a new user, or just view the old entries of the database.
def main_menu():
    while True:
        print("What would you like to do? You can:\n")
        print("A - Create a new user with your credentials.\n")
        print("B - Login with your account.\n")
        print("You can also exit the program by typing 'quit' or 'exit'\n")
        choice = input("Choose one of the options\n")
        
        if choice.lower() == 'a':
            new_user_query()
            #Calls the new_user_query function which has the user input their credentials
            break

        elif choice.lower() == 'b':
            print("Sending you to the Login page...")
            login_menu()
            #continue, to just show the previous entries in the database
            break

        elif choice.lower() == 'exit' or choice.lower() == 'quit':
            print("Quitting program...")
            sys.exit(0)
            #continue, to just show the previous entries in the database
            break

def login_menu():
    while True:
        print("To login, please enter your assigned username.\n")
        print("It should be the first letter of your first name and then your last name.\n")
        login_input_u = input("Type your username here. If you don't know what your username is, type 'help'. You can also quit by typing 'quit' or 'exit'.")
        if login_input_u.lower() == 'help':
            print("The login help page is not up yet. Sorry.\n")
            continue
            #login_help_page()
        elif login_input_u.lower() == 'quit' or login_input_u.lower() == 'exit':
            break
            sys.exit(0)
        else:
            testfor_username = login_input_u
        
    while True:
        print("To login, please enter your password.\n")
        print("It should be the password that is associated with your account.\n")
        login_input_p = input("Type your password here. If you don't know what your password is, type 'help'. You can also quit by typing 'quit' or 'exit'.\n")
        if login_input_p.lower() == 'help':
            print("The login help page is not up yet. Sorry.\n")
            continue
            #login_help_page()
        elif login_input_p.lower() == 'quit' or login_input_p.lower() == 'exit':
            break
            sys.exit(0)
        else:
            testfor_password = login_input_p
            


def login_help_page():
    print("What do you need help with? Options are: 'username' if you don't know what your is username.\n")
    print("Or, 'password' if you don't know your password.\n")
    print("If you need help, choose one of the options first, and then you will be brought back to this menu. You can also quit by typing 'quit' or 'exit'.\n")
    while True:
        login_help_input = input("Type either password or username.\n")
        if login_help_input.lower() != 'password' or login_help_input.lower() != 'username':
            print("You did not choose one of the options. Please try again.\n")
            continue
        elif login_help_input == 'username':
            login_username_help()
        elif login_help_input == 'password':
            login_password_help()
        else:
            print("Error. Try again.\n")
            continue

def login_username_help():
    print("It looks like you need help with your username.\n")
    first_name_input = input("Type your first name so we can look up your credentials.\n")
    last_name_input = input
def login_password_help():
    print("It looks like you need help with your username.\n")
    

    
#the Main Menu function
#this probably should be some sort of __init__ function, but I forget how you do that in Python. 
main_menu()

#dumps updated json file to the database.json
with open('database.json', 'w') as dbase_json:
    json.dump(users, dbase_json)

#Print the complete user database as it stands now. Keep in mind that the dictionary keys ("first_name", "last_name", etc...) are not sorted.
#Eventually I may have the program sort the dictionary keys for each user, to have the username printed as first key, first_name 2nd and so on.
print("<Debug> This is the current state of 'users': "+ str(users))
print("There are: " + str(len(users)) + " Users in the Database as of now.\n")

