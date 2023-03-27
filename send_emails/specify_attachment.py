"""
Sends email with attachment specified in the CSV file
"""
import yagmail
import variables
import pandas

SENDER = variables.EMAIL

def send_email():
    "Sends single email with the attachment specified in the contacts list"

    df = pandas.read_csv('contacts.csv')


    for index, row in df.iterrows():
        subject = "Email subject!"

        # create list to add attachment file
        contents = [f"""
        Dear {row['name']}
        Please find this month's bill.
        Kind regards,
        Penny
        """]

        yag = yagmail.SMTP(user=SENDER, password=variables.PASSWORD)
        yag.send(to=row['email'], subject=subject, contents=contents, attachments=row['attachment'])

send_email()
