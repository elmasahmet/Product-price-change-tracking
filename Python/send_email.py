from email.mime.text import MIMEText
from http import server
import imp
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tabnanny import check






def sendMail(toMail, subject, content):

    fromMail = "#sender mail address" 
    password =  "#sender mail password" 
    server = smtplib.SMTP("smtp.google.com",587)

    server.starttls()

    server.login(fromMail, password)

    message = MIMEMultipart('alternative')
    message['Subject'] = subject

    htmlContent = MIMEText(content, 'html')
    message.attach(htmlContent)

    server.sendmail(
        fromMail,
        toMail,
        message.as_string()
    )
    print("E-posta gönderildi.")
    server.quit()

