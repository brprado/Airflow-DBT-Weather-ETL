from dotenv import load_dotenv
import requests
import os
import json

load_dotenv()

def fetch_data():
    print('Fetching WeatherStack data from API')
    
    try:
        api_key = os.environ.get("WEATHERSTACK_API_KEY")
        api_url = os.environ.get("API_URL")
        url = f"{api_url}?access_key={api_key}&query=Camaçari"

        response = requests.get(url)
        response.raise_for_status()
        print("API Response passed succcesfully!")
        
        return response.json()
    except requests.excepions.RequestExceprion as e:
        print(f"An error ocurred {e}")
        raise

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Camaçari, Brazil', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Camaçari', 'country': 'Brazil', 'region': 'Bahia', 'lat': '-12.483', 'lon': '-38.217', 'timezone_id': 'America/Bahia', 'localtime': '2026-05-18 14:24', 'localtime_epoch': 1779114240, 'utc_offset': '-3.0'}, 'current': {'observation_time': '05:24 PM', 'temperature': 28, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0002_sunny_intervals.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '05:44 AM', 'sunset': '05:15 PM', 'moonrise': '07:33 AM', 'moonset': '07:08 PM', 'moon_phase': 'Waxing Crescent', 'moon_illumination': 2}, 'air_quality': {'co': '82.85', 'no2': '5.45', 'o3': '42', 'so2': '2.25', 'pm2_5': '9.75', 'pm10': '12.45', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 10, 'wind_degree': 130, 'wind_dir': 'SE', 'pressure': 1015, 'precip': 0, 'humidity': 74, 'cloudcover': 75, 'feelslike': 30, 'uv_index': 5, 'visibility': 10, 'is_day': 'yes'}}