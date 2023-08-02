import smtplib
import time
import schedule
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Create a secure SSL connection to the email server
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)  # Replace 'smtp.example.com' with your SMTP server
        server.login(sender_email, sender_password)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        server.sendmail(sender_email, recipient_email, msg.as_string())
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

    server.quit()

# Replace the following variables with your email credentials and desired email content
sender_email = "brianocultic@gmail.com"
sender_password = "yewnypmoenmzkeyu" # use password generated from google account
recipient_email = "Danielmichele47@gmail.com"
subject = "Testing"
body = "You created an email sending bot"

# Schedule the email to be sent every 2 minutes
schedule.every(2).minutes.do(send_email, sender_email, sender_password, recipient_email, subject, body)

# Infinite loop to run the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
