import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

lowercase_letters = 'abcdefghijklmnopqrstuvwxyz' #to check if lowercase in password
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' #to check if uppercase in password
num_sym = "`1234567890-=[]\;',./~!@#$%^&*()_+{}|:<>?" #to check if num/sym in password

def password_recovery(user_email, user_password): #email is same as user_name
    #user_name = "zseltzer@fandm.edu" #Dont need this to test anymore
    #user_password = "my_password123" #Dont need this to test anymore

    fromaddr = "makoletcps111" #The sender email address
    toaddr = user_email #Where to send it to, will be the user's email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Password for your Makolet® Account" #Subject

    body = "You requested a password recovery for your Makolet® Account.\n\nThe password for your Makolet® account is:\n\n\t\t" + user_password + "\n\nYou can now use this to login to Makolet®, the Text-Based Store™ "
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587) #Gmail SMTP server info
    server.starttls()
    server.login(fromaddr, "MAKOLET_CPS_111") #password for the MakoletCPS111 gmail account.
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def new_password(email):
    min_characters = 8
    legal_password = False
    while legal_password == False:
        print("You will now set a password for your account.\n")
        print("It must be at least " + str(min_characters) + " characters.\n")
        print("It must include an uppercase letter, a lowercase letter and a number/symbol")
        new_password = input("Please type your password here.")
        #Have them re-enter the password.
        re_new_password = input("Please re-type your password a second time:\n")
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
        legal_password = True
        return re_new_password
        #Legal password has been entered twice, Loop ends, program continues.
