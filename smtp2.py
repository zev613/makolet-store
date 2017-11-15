import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def password_recovery(user_email, user_password): #email is same as user_name
    #user_name = "zseltzer@fandm.edu" #Dont need this to test anymore
    #user_password = "my_password123" #Dont need this to test anymore

    fromaddr = "makoletcps111" #The sender email address
    toaddr = user_email #Where to send it to, will be the user's email
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Password for your Makolet® Account" #Subject

    body = "You requested a password recovery for your Makolet® Account.\n\nThe password for your Makolet® account is:\n\n\t\t" + user_password + "\n\nYou can now use this to login to Makolet®, the Text-Based Store™"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587) #Gmail SMTP server info
    server.starttls()
    server.login(fromaddr, "MAKOLET_CPS_111") #password for the MakoletCPS111 gmail account.
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
