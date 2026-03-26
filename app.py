from flask import Flask, jsonify
from weather import get_weather
from alert import check_alert
from email_alert import send_email
import pandas as pd
from datetime import datetime
from whatsapp_alert import send_whatsapp

app = Flask(__name__)

@app.route("/")
def home():
    weather = get_weather("Delhi")
    alerts = check_alert(weather)

    weather["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    df = pd.DataFrame([weather])
    df.to_csv("weather_log.csv", mode='a', header=False, index=False)

    print("DEBUG alerts:", alerts)   # ✅ debug

    send_email(alerts, weather)     # ✅ IMPORTANT
    send_whatsapp(alerts, weather)

    return jsonify({
        "status": "success",
        "data": weather,
        "alerts": alerts
    })

if __name__ == "__main__":
    app.run(debug=True)