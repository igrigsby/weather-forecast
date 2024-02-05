import requests
from datetime import datetime

from config import OPENWEATHERMAP_API_KEY

def kelvin_to_fahrenheit(kelvin):
    """Convert temperature from Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32

def get_weather_forecast(zip_code):
    """Get 5-day weather forecast for the given zip code."""
    api_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {'zip': zip_code, 'appid': OPENWEATHERMAP_API_KEY}


