import smtplib
from email.message import EmailMessage

# Your email address and app password
EMAIL = "masten010@gmail.com"
APP_PASSWORD = "xpcq szcm aowu cwpc"  # ← Paste your 16-character app password here

# Create the email
msg = EmailMessage()
msg["Subject"] = "📚 Python Learning Reminder"
msg["From"] = EMAIL
msg["To"] = EMAIL
msg.set_content("Hey! Time to study Python for at least 30 minutes. Let’s go! 🧠🔥")

# Connect and send
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(EMAIL, APP_PASSWORD)
    smtp.send_message(msg)

print("✅ Reminder sent to your inbox.")
