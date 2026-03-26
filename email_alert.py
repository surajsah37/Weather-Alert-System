import smtplib
import os
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

def send_email(alerts, weather):
    print("📩 Email function called")

    # force alert for testing
    alerts = alerts if alerts else ["Test Alert"]

    subject = "Weather Alert Notification"   # ❌ removed emoji

    body = f"""
Weather Alert

City: {weather.get('city')}
Temperature: {weather.get('temperature')}°C
Humidity: {weather.get('humidity')}%
Condition: {weather.get('weather')}

Alerts:
{', '.join(alerts)}

Time: {weather.get('time')}
"""

    try:
        # ✅ Create MIME message (UTF-8 support)
        msg = MIMEMultipart()
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain", "utf-8"))

        # ✅ SMTP setup
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)

        # ✅ send email
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()

        print("✅ Email sent successfully!")

    except Exception as e:
        print("❌ Email failed:", e)