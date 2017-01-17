from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


host = "smtp.gmail.com"
port = 587

username = "wsadevv@gmail.com"
password = "$sec#wsabsi630"
sender = username
to_list = "williansantana.angola@gmail.com"

# it dont render hrml
email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
# email_conn.sendmail(sender, to_list, "Howdy")
# email_conn.quit()

# it now renders html

the_msg = MIMEMultipart("alternative")
the_msg['Subject'] = "Hello there"
the_msg['From'] = sender
the_msg['To'] = to_list

plain_txt = "Testing the message"
html = """\
<html> <head></head>
<body> <p>Hey!<br>
Testing this email <b>message</b>
Made by <a href='http://www.google.com'>Link</p>
</body>
<html>
"""
part_one = MIMEText(plain_txt, 'plain')
part_two = MIMEText(html, 'html')

the_msg.attach(part_one)
the_msg.attach(part_two)
email_conn.sendmail(sender, to_list, the_msg.as_string())
email_conn.quit()

print(the_msg.as_string())
