import requests
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("APYKEY")

def get_data(place, forecastDays):
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
        response = requests.get(url)
        data = response.json()
        filtered_data = data["list"]
        number_values = 8 * forecastDays
        filtered_data = filtered_data[:number_values]
        return filtered_data
       