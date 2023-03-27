"""
Send an HTML email using MIMEMultipart and attach an image
"""
import smtplib
from email.mime.text import MIMEText # use to generate text type MIME documents
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase # object of mimebase protocol
from email import encoders
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

    attachment_path = 'hello.jpg'
    attachment_file = open(attachment_path, 'rb') # create a file object
    payload = MIMEBase('application', 'octate')
    payload.set_payload(attachment_file.read()) # extract content from file
    encoders.encode_base64(payload) # encode payload into base64 format
    payload.add_header('Content-Disposition', 'attachment', filename=attachment_path) # add header
    msg.attach(payload)

    # start smtp server to send email
    server = smtplib.SMTP('smtp.office365.com', 587) # connect to port 587
    server.starttls() # start TLS encrypted protocol
    server.login(SENDER, PASSWORD)
    message_text = msg.as_string()
    server.send_message(msg) # use msg library
    print(message_text)
    print('email sent')
    server.quit()

outlook_email()
