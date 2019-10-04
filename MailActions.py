import os
import smtplib

EMAIL_ADDRESS = 'compproj1itu@gmail.com'
EMAIL_PASSWORD = 'Compproj1010'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Grab dinner this weekend?'
    body = 'How about dinner at 6pm this saturday'

    msg = f'Subject: {subject}\n\n {body}'

    smtp.sendmail(EMAIL_ADDRESS,'mlkmhmtbyk@gmail.com', msg)