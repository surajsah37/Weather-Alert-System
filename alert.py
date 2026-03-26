def check_alert(weather_data):
    alerts = []

    temp = weather_data["temperature"]
    humidity = weather_data["humidity"]
    condition = weather_data["weather"]

    if temp > 35:
        alerts.append("🔥 High Temperature Alert")

    elif temp < 10:
        alerts.append("❄️ Cold Weather Alert")

    if condition in ["Rain", "Thunderstorm"]:
        alerts.append("🌧️ Rain Alert")

    if condition in ["Haze", "Smoke"]:
        alerts.append("😷 Air Quality Alert")

    if humidity > 80:
        alerts.append("💧 High Humidity Alert")

    return alerts