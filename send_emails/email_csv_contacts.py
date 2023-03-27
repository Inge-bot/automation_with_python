"""
Send email to list of contacts in a CSV file
"""
import yagmail
import variables
import pandas

SENDER = variables.EMAIL

def send_email():
    "Sends single email to each contact in csv file"

    df = pandas.read_csv('contacts.csv')

    for index, row in df.iterrows():
        subject = "Email subject!"
        contents = f"""
        Dear {row['name']}
        Here is the content of the email!
        Kind regards,
        Jane Austin
        """

        yag = yagmail.SMTP(user=SENDER, password=variables.PASSWORD)
        yag.send(to=row['email'], subject=subject, contents=contents)

send_email()
