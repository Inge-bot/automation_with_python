"""Send email and modify attachments dynamically
"""
import yagmail
import variables
import pandas

SENDER = variables.EMAIL

def generate_file(filename, content):
    "generate text file"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(str(content))

def send_email():
    "sends single email with the attachment specified in the contacts list"

    df = pandas.read_csv('contacts.csv')

    for index, row in df.iterrows():
        name = row['name']
        filename = name + 'txt'
        amount = row['amount']
        receiver = row['email']
       

        generate_file(filename, amount)

        subject = "Email subject!"
        contents = f"""
        Dear {name}
        Please find this month's bill attached. 
        Please pay the amount, {amount}, by the end of the month.
        Kind regards,
        Penny
        """
        
        yag = yagmail.SMTP(user=SENDER, password=variables.PASSWORD)
        yag.send(to=receiver, subject=subject, contents=contents, attachments=filename≈q
       
send_email()
