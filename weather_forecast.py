import requests
from datetime import datetime

from config import OPENWEATHERMAP_API_KEY

def kelvin_to_fahrenheit(kelvin):
    """Convert temperature from Kelvin to Fahrenheit."""
    return (kelvin - 273.15) * 9/5 + 32


