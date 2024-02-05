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

    try:
        # Make API request
        response = requests.get(api_url, params=params).json()
        forecast_list = response['list']

        # Display header
        print("# Date         Temperature (°F)       Precipitation")

        # Track unique dates to avoid duplicate entries
        unique_dates = set()

        # Iterate through the forecast list
        for forecast in forecast_list:
            # Extract date and format it
            forecast_date = datetime.utcfromtimestamp(forecast['dt']).strftime('%m/%d/%Y')

            # Skip if date is already processed
            if forecast_date in unique_dates: continue
            unique_dates.add(forecast_date)
            
            # Convert temperatures to Fahrenheit
            temp_max, temp_min = map(kelvin_to_fahrenheit, [forecast['main']['temp_max'], forecast['main']['temp_min']])
            
            # Get precipitation, default to 0 if not available
            precipitation = forecast['rain']['3h'] if 'rain' in forecast and 'rain' in forecast else 0

            

