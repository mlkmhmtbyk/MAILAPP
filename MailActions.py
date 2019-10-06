import os
import smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login("compproj1itu@gmail.com","Compproj1010")

    subject = "Grab dinner this weekend?"
    body = 'How about dinner at 6pm this saturday?'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail("conpproj1itu@gmail.com", "mlkmhmtbyk@gmail.com", msg)