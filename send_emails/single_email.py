"""
Email clients uses SMTP to send/receive emails.
Send single email with gmail client.
Add email account details in a variables.py file
"""
import yagmail
import time
from datetime import datetime as dt
import variables

SENDER = variables.EMAIL
RECEIVER = variables.RECEIVER

def send_email():
    "Sends single email"
    subject = "This is the subject!"
    contents = '''
    Dear John Doe,
    Here is the content of the email!
    Kind regards,
    Jane Austin
    '''
    while True:
        now = dt.now()
        if now.hour == 13 and now.minute == 7: # time when email is first sent
            yag = yagmail.SMTP(user=SENDER, password=variables.PASSWORD)
            yag.send(to=RECEIVER, subject=subject, contents=contents)
            print("Email sent")
            time.sleep(60) # email reoccures every 60 seconds

send_email()
