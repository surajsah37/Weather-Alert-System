import schedule
import time
from weather import get_weather
from alert import check_alert
from email_alert import send_email
from whatsapp_alert import send_whatsapp
from datetime import datetime
import pandas as pd

def job():
    print("⏱️ Running scheduled job...")

    weather = get_weather("Delhi")
    alerts = check_alert(weather)

    weather["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # save data
    df = pd.DataFrame([weather])
    df.to_csv("weather_log.csv", mode='a', header=False, index=False)

    # send alerts
    send_email(alerts, weather)
    send_whatsapp(alerts, weather)

    print("✅ Job completed\n")


# ⏰ Run every 10 minutes
schedule.every(10).minutes.do(job)

# First run तुरंत
job()

while True:
    schedule.run_pending()
    time.sleep(1)