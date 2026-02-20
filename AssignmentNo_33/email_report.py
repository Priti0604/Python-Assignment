import smtplib
from email.message import EmailMessage
import os

def EmailCommand(LogFilePath):
    msg = EmailMessage()
    msg['Subject'] = "Platform Surveillance Report"
    msg['From'] = "sender@gmail.com"
    msg['To'] = "receiver@gmail.com"
    msg.set_content("Please find the attached log file")

    with open(LogFilePath, 'rb') as f:
        msg.add_attachment(
            f.read(),
            maintype='text',
            subtype='plain',
            filename=os.path.basename(LogFilePath)
        )

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("sender@gmail.com", "APP_PASSWORD")
    server.send_message(msg)
    server.quit()