# utils/alert_utils.py
import smtplib
from email.mime.text import MIMEText

# Function to send email alerts
def send_alert(subject, body):
    # Simulate sending an email alert
    print(f"ALERT! {subject}: {body}")
    # You can expand this to send actual emails or SMS via services like Twilio or SendGrid.
