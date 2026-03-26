import requests
import os
from dotenv import load_dotenv

# ✅ load .env file
load_dotenv()

# ✅ get API key from .env
API_KEY = os.getenv("API_KEY")

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    return {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["main"]
    }