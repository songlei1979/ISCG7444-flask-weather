import os
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")


@app.route("/")
def home():
    return jsonify({
        "message": "Weather Flask API is running"
    })


@app.route("/weather")
def get_weather():
    city = request.args.get("city", "Auckland")

    if not WEATHER_API_KEY:
        return jsonify({
            "error": "WEATHER_API_KEY is missing"
        }), 500

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return jsonify({
            "error": "Failed to fetch weather data",
            "status_code": response.status_code,
            "details": response.json()
        }), response.status_code

    data = response.json()
    icon = data["weather"][0]["icon"]
    icon_url = f"https://openweathermap.org/img/wn/{icon}.png"
    result = {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "weather": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],
        "icon_url": icon_url
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)