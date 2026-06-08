import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = "dd861675f7171a779011455d7728c"
Lattitude = 28.6139 
longitude = 77.2090

url = f"https://api.openweathermap.org/data/2.5/weather?lat={Lattitude}&lon={longitude}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

print(data)