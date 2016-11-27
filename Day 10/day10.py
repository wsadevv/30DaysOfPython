# assim
import smtplib

# ou assim
from smtplib import SMTP
#host and credentials
host = "smtp.gmail.com"
port = 587
username = "your_mail"
password = "your_pass"
sender = username
receivers = ["receiver_mail", 'receiver_mail']

# setting connection with smtp server
try:
    emailConnection = SMTP(host, port)
except Exception as e:
    raise Exception
print(emailConnection.ehlo())

# starting TLS encryption protocol
emailConnection.starttls()
print(emailConnection.login(username, password))

emailConnection.sendmail(sender, receivers, "Standard message.")

# finish:
emailConnection.quit()

def magic():
    print("Magic")
