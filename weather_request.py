import requests
from datetime import datetime, timedelta


weather_cache = {}


def fetch_weather(city):
    if city in weather_cache:
        cached_temperature, last_update_time = weather_cache[city]

        if datetime.now() - last_update_time < timedelta(minutes=10):
            return cached_temperature  
        
    API_KEY = '1977f4390a80b1869b14b19aa7cad804'  
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = f"{base_url}appid={API_KEY}&q={city}&units=metric"
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']  
        last_update_time = datetime.now()
        weather_cache[city] = (temperature, last_update_time)  
        return temperature
    else:
        return None


