import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from']='HAMZA MURTAZA'
email['to']='hamzamurtaza11@gmail.com'
email['subject']='You won 1,000,000 dollars !'

email.set_content('I am a python master !')

with smtplib.SMPTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dummyemail@gmail.com','abc123')
    smtp.send_message(email)
    print("email sent")
    