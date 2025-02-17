import yagmail
import os

sender = os.getenv('email_address')
receiver = "nebayor992@kytstore.com"

subject = "Dummy test"

contents = """
Hello, this is a test email.
"""

yag = yagmail.SMTP(user=sender, password=os.getenv('email_password'))
yag.send(to=receiver, subject=subject, contents=contents)