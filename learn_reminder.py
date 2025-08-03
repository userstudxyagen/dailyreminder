import smtplib
import os
from email.message import EmailMessage

# Load email and password from environment
EMAIL = os.environ.get("EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

# Create the email
msg = EmailMessage()
msg["Subject"] = "📚 Python Learning Reminder"
msg["From"] = EMAIL
msg["To"] = EMAIL
msg.set_content("Hey! Time to study Python for at least 30 minutes today. Let's go! 🧠🔥")

# Connect and send
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL, APP_PASSWORD)
    smtp.send_message(msg)

print("✅ Reminder sent to your inbox.")
