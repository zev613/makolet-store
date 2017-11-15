lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num_sym = "`1234567890-=[]\;',./~!@#$%^&*()_+{}|:<>?"

default_min_characters = 8
min_characters = default_min_characters

def character_types_needed(need_lower, need_upper, need_numsym):
    #This function, (more complicated than it really should be) creates the string that tells the user what the parameters for this password are.
    #mostly to ensure the punctuation is correct if one or more of the parameters is 'disabled'
    types_needed = 'at least '
    types_needed_new = ''
    if need_lower == True:
        types_needed_new = types_needed + 'a lowercase letter'
        if need_upper and need_numsym == True:
            types_needed_new = types_needed_new + ', '
        elif need_upper or need_numsym == True:
            types_needed_new = types_needed_new + ', and '
    if need_upper == True:
        types_needed_new = types_needed_new + 'an uppercase letter'
        if need_lower or need_numsym == True:
            types_needed_new = types_needed_new + ', and '
    if need_numsym == True:
        types_needed_new = types_needed_new + 'a number or symbol'
    return types_needed_new

def testfor_characters(char_type, password):
    if any((c in char_type) for c in password):
        return True

'''This function is called on by other classes, and will take the user through the process of creating a password based on a number of parameters:
min number of characters needed for a password
the 1st boolean value determines if the password must include at least one lowercase letter.
The 2nd boolean determines if the password must include at least one uppercase letter.
The 3rd boolean determines if the password must include at least one number or symbol.
If the function was passed a parameter, and the user's entered password does not fit that parameter, the function will loop and have the user restart the process.
'''
def new_password(min_characters, need_lower, need_upper, need_numsym):
    #Loop that ensures user enters the same password twice, that the password includes the correct type of characters, and is not in the 'bad_password' list.
    legal_password = False
    while legal_password == False:
        print("Please enter a new password for your account.\n")
        if min_characters == 0:
            min_characters = ''
        if need_lower == False and need_upper == False and need_numsym == False:
            new_password = input("It must be at least " + str(min_characters) + " characters.\n")
        else:    
            new_password = input("It must be at least " + str(min_characters) + " characters, and it must include " + character_types_needed(need_lower, need_upper, need_numsym) + ".\n")
        #Have them re-enter the password.
        re_new_password = input("Please re-enter your password:\n")
        #The following sequence tests the password if its less than the min # of characters needed, and if it contains the required types of characters

        if new_password == re_new_password:
        #If the password strings are equal,
            if len(re_new_password) >= min_characters:
            #If the password is at least the minimum character length
                if need_lower == True and testfor_characters(lowercase_letters, re_new_password) == False:
                # If it needed a lowercase and the tester did not find a lowercase in the password:
                    print("You did not include a lowercase letter.\n")
                    continue
                    #legal_password = False
                if need_upper == True and testfor_characters(uppercase_letters, re_new_password) == False:
                # If it needed a uppercase and the tester did not find a uppercase in the password:
                    print("You did not include an uppercase letter.\n")
                    continue
                    #legal_password = False
                if need_numsym == True and testfor_characters(num_sym, re_new_password) == False:
                # If it needed a number or symbol and the tester did not find a number or symbol in the password:
                    print("You did not include a Number or Symbol.\n")
                    continue
                    #legal_password = False
            else:
                print("Length of password must be at least " + str(min_characters) + " characters. Please try again.\n")
                #Restart the loop because password was less than the minimum amount of characters
                continue
                #legal_password = False
                
            print("Your passwords are the same, and meet all of the requirements. Congratulations.\n")
            #Passwords are the same, and meet all of the parameters as set when calling the function. Therefore the loop breaks and it returns the legal password value.
            return re_new_password
            legal_password = True
            #Legal password has been entered twice, Loop ends, program continues.
        else:
            print("That was not the same password. Try again.\n")
            #The loop restarts immediately if both passwords are not equal
            continue
            #legal_password = False
        
new_password(8, True, True, True)
#Will return a new password string with a minimum of 8 characters, and will include at least 1 lowercase letter, at least 1 uppercase letter, and at least 1 number or symbol.
