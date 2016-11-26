#assim
#import smtplib

#ou assim
from smtplib import SMTP
#host and credentials
host="smtp.gmail.com"
port=587
username="wsapydev@gmail.com"
password="$secad03"
sender = username
receivers = ["zeliasantana221@gmail.com",'wsadevv@gmail.com']

#setting connection with smtp server
try:
    emailConnection = SMTP(host,port)
except Exception as e:
    raise Exception
print(emailConnection.ehlo())

#starting TLS encryption protocol
emailConnection.starttls()
print(emailConnection.login(username,password))

emailConnection.sendmail(sender,receivers,"Standard message.")

# finish:
emailConnection.quit()
