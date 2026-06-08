import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY_OPEN_WEATHER_API")
Lattitude = 28.6139 
longitude = 77.2090

def fetch_data():
    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={Lattitude}&lon={longitude}&appid={API_KEY}&units=metric"
    response = requests.get(url=url)
    if response.status_code == 200:
        data = response.json()
        city = data['city']['name']
        TimeZone = (data['city']['timezone'])/3600
        sunrise = data['city']['sunrise']/3600
        sunset = data['city']['sunset']/3600
        for i in range(0,40):
            interval = data['list'][i]
            time = interval['dt_txt']
            print(f"Date and Time : {time}")
            temp = round(interval['main']['temp'])
            print(f"Temperature : {temp}*c")
            temp_feels_like = round(interval['main']['feels_like'])
            print(f"Feels like : {temp_feels_like}*c")
            pressure = interval['main']['pressure']
            print(f"Pressure : {pressure}")
            sea_level_pressure = interval['main']['sea_level']
            print(f"Sea Level Pressure : {sea_level_pressure}")
            grnd_level_pressure = interval['main']['grnd_level']
            print(f"Ground Level Pressure : {grnd_level_pressure}")
            humidity = interval['main']['humidity']
            print(f"Humidity : {humidity}%")
            weather = interval['weather'][0]
            clouds = weather['main']
            print(f"weather condition : {clouds}")
            description_clouds = weather['description']
            print(f"Clouds description : {description_clouds}")
            visibility = interval['visibility']/1000
            print(f"visibility : {visibility}Km")
            wind = round((interval['wind']['speed'])*18/5, 3)
            print(f"Wind speed : {wind} Kph")
            pop = interval['pop']
            print(f"Chance of rain : {pop}%")
            print()
            print()

        return f"{city}, {TimeZone}hrs, {sunrise}, {sunset}, {time}, {temp}*c, {wind}Kph, chances of rain:{pop}%."

    else:
        return f"{response.status_code}, {response.json()['message']}"
    
print(fetch_data())
