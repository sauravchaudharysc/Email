import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Saurav Chaudhary'
email['to'] = 'sauravchaudhary717@gmail.com'
email['subject'] = 'You won million dollar!'

email.set_content(html.substitute({'name' : 'Tintin'}))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('email','password')
	smtp.send_message(email)
	print('All done')