import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

email = EmailMessage()
email['from'] = '#your_name'
email['to'] = '#sender_email'
email['subject'] = '#subject'

email.set_content('This is an automated python email')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login('#your_email', '#your_password')
  smtp.send_message(email)
  print('all good boss!')