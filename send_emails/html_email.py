"""
Send an HTML email using MIMEMultipart
"""
import smtplib
from email.mime.text import MIMEText # use to generate text type MIME documents
from email.mime.multipart import MIMEMultipart
import variables

def outlook_email():
    "send email from outlook with smtp server"
    SENDER = variables.EMAIL_OUTLOOK
    RECEIVER = variables.RECEIVER
    PASSWORD = variables.PASSWORD_OUTLOOK

    msg = MIMEMultipart()
    msg['From'] = SENDER
    msg['To'] = RECEIVER
    msg['Subject'] = 'Hello from Outlook!'

    # create multiline message
    body = """
    <h3>Hey stranger</h3>
    Just wanted to say hi from my Outlook address.
    Catch you later!
    """

    mimetext = MIMEText(body, 'html') # set body to html format
    msg.attach(mimetext)
    print(mimetext)
    # start smtp server to send email
    server = smtplib.SMTP('smtp.office365.com', 587) # connect to port 587
    server.starttls() # start TLS encrypted protocol
    server.login(SENDER, PASSWORD)
    server.send_message(msg) # use msg library
    print('email sent')
    server.quit()

outlook_email()
