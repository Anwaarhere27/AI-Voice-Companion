import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_weather(location: str):

    if not API_KEY:
        return "Weather API key missing."

    url = "http://api.weatherapi.com/v1/current.json"

    params = {
        "key": API_KEY,
        "q": location
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        # DEBUG
        print("DEBUG WEATHER:", data)

        if "error" in data:
            return f"Sorry, I couldn't find weather for {location}."

        city = data["location"]["name"]
        country = data["location"]["country"]

        temp = data["current"]["temp_c"]
        feels = data["current"]["feelslike_c"]

        condition = data["current"]["condition"]["text"]

        humidity = data["current"]["humidity"]

        return (
            f"Current weather in {city}, {country}: "
            f"{condition}. Temperature is {temp} degrees Celsius, "
            f"feels like {feels} degrees. "
            f"Humidity is {humidity} percent."
        )

    except Exception as e:
        return f"Weather API error: {str(e)}"