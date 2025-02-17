import yagmail
import os
import pandas

sender = os.getenv('email_address')

subject = "Dummy test"

yag = yagmail.SMTP(user=sender, password=os.getenv('email_password'))

df = pandas.read_csv('contacts.csv')

for index, row in df.iterrows():
  contents = f"""
    Hi {row['name']}!
    """
  yag.send(to=row['email'], subject=subject, contents=contents)