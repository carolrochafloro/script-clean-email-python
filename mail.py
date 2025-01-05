import imaplib
import json
from criteria import delete

with open('config.json') as config_file:
    config = json.load(config_file)

login_email = config['email']
password = config['password']

def login(user, password):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    result = mail.login(user, password)
    print(result[0])
    return mail
    
def delete_email(mail, delete):
     print('Starting delete function')
     for email in delete:
        criteria = f'(FROM "{email}")'
        mail.select('inbox')
        status, messages = mail.search(None, criteria)
        email_ids = messages[0].split()

        print(f'{len(email_ids)} found in criteria {email}')

        for email_id in email_ids:
            mail.store(email_id, '+FLAGS', '\\Deleted')
            print(f'{email_id} flagged to be deleted.')
        
        mail.expunge()
        print(f'E-mails from {email} expunged.')

def main():
    mail = login(login_email, password)
    delete_email(mail, delete)
    mail.logout()

main()
