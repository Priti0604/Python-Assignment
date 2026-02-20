import smtplib
from email.message import EmailMessage

def SendEmail():
    msg = EmailMessage()
    msg['Subject'] = "Marvellous Data Shield Notification"
    msg['From'] = "sender@gmail.com"
    msg['To'] = "receiver@gmail.com"
    msg.set_content("Backup process executed successfully")

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("sender@gmail.com", "APP_PASSWORD")
    server.send_message(msg)
    server.quit()