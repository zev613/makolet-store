import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user_name = "zseltzer@fandm.edu"
user_password = "my_password123"

fromaddr = "makoletcps111"
toaddr = user_name
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Password for your Makolet® Account"

body = "You requested a password recovery for your Makolet® Account.\n\nThe password for your Makolet® account is:\n\n\t\t" + user_password + "\n\nYou can now use this to login to Makolet®, the Text-Based Store™"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "MAKOLET_CPS_111")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()