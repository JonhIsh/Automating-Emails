import smtplib
import os
import time
from datetime import datetime as dt

sender = os.getenv('email_address')
receiver = "nebayor992@kytstore.com"

subject = "Dummy test"

message = """\
Subject: Hello

What's up?
"""
server = smtplib.SMTP('smtp.office365.com', 587)
server.starttls()
server.login(sender, os.getenv('email_password'))
server.send(sender, receiver, message)
server.quit()