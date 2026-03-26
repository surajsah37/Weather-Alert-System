from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

SID = os.getenv("TWILIO_SID")
AUTH = os.getenv("TWILIO_AUTH")
TWILIO_NUMBER = os.getenv("TWILIO_WHATSAPP")
MY_NUMBER = os.getenv("MY_NUMBER")

def send_whatsapp(alerts, weather):
    print("📱 WhatsApp function called")

    # 👉 force alert for testing
    alerts = alerts if alerts else ["Test Alert 🚀"]

    message_body = f"""
🚨 Weather Alert

City: {weather.get('city')}
Temp: {weather.get('temperature')}°C
Humidity: {weather.get('humidity')}%
Condition: {weather.get('weather')}

Alerts:
{', '.join(alerts)}
"""

    try:
        client = Client(SID, AUTH)

        message = client.messages.create(
            body=message_body,
            from_=f"whatsapp:{TWILIO_NUMBER}",
            to=f"whatsapp:{MY_NUMBER}"
        )

        print("✅ WhatsApp sent!", message.sid)

    except Exception as e:
        print("❌ WhatsApp failed:", e)