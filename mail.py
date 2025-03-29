import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mails = ["sowjijettiboina@gmail.com","pujithavarre14@gmail.com","chennamsettiharini@gmail.com"]


for i in mails:
    otp = random.randint(1111,9999)
    body = f"OTP for Verification is {otp}"

    msg = MIMEMultipart()
    msg["From"] = "sowjijettiboina.com"
    msg["To"] = i
    msg["Subject"] = "OTP For Validation"
    msg.attach(MIMEText(body,'plain'))

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("sowjijettiboina@gmail.com","mvso xjah jxcl gtml")
    server.send_message(msg)
    server.quit()

    cotp = int(input("Enter OTP Recieved: "))

    if otp == cotp:
        print("OTP Verification Success")
    else:
        print("Invalid OTP")







