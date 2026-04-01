from datetime import datetime


def fetch_weather_data(city):
    return {
        "city": city,
        "temp": 20,
        "condition": "sunny",
        "humidity": 50
    }


def fetch_forecast(city, days=3):
    forecast = []
    for i in range(days):
        forecast.append({"day": i + 1, "temp": 20 + i, "condition": "sunny"})
    return forecast


def get_current_hour():
    return datetime.now().hour
