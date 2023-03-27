"""
Send email from Outlook
"""
import smtplib
from email.message import EmailMessage
import variables

def outlook_email():
    "send email from outlook with smtp server"
    SENDER = variables.EMAIL_OUTLOOK
    RECEIVER = variables.RECEIVER
    PASSWORD = variables.PASSWORD_OUTLOOK

    # create multiline message
    message = """
    Just wanted to say hi from my Outlook address.
    Catch you later!
    """
    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = 'Hello from Outlook!'
    msg['From'] = SENDER
    msg['To'] = RECEIVER

    # start smtp server to send email
    server = smtplib.SMTP('smtp.office365.com', 587) # connect to port 587
    server.starttls() # start TLS encrypted protocol
    server.login(SENDER, PASSWORD)
    server.send_message(msg) # use msg library
    server.quit()

outlook_email()
