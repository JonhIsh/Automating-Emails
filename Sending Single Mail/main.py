import yagmail
import os
import time
from datetime import datetime as dt

sender = os.getenv('email_address')
receiver = "nebayor992@kytstore.com"

subject = "Dummy test"

contents = """
Hello, this is a test email.
"""


while True:
    now = dt.now()
    if now.hour == 12 and now.minute == 48:
        yag = yagmail.SMTP(user=sender, password=os.getenv('email_password'))
        yag.send(to=receiver, subject=subject, contents=contents)
        time.sleep(60)