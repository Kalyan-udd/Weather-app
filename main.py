from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

templates = Jinja2Templates(directory='templates')

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):  
    API_KEY = os.getenv("API_KEY_OPEN_WEATHER_API")
    Lattitude = 15.2000
    longitude = 77.2090
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={Lattitude}&lon={longitude}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        tz_offset = data['timezone']

        sunrise_utc = datetime.datetime.fromtimestamp(data['sys']['sunrise'], datetime.timezone.utc)
        sunrise_local = sunrise_utc + datetime.timedelta(seconds=tz_offset)
        
        sunset_utc = datetime.datetime.fromtimestamp(data['sys']['sunset'], datetime.timezone.utc)
        sunset_local = sunset_utc + datetime.timedelta(seconds=tz_offset)

        current_utc = datetime.datetime.fromtimestamp(data['dt'], datetime.timezone.utc)
        current_local = current_utc + datetime.timedelta(seconds=tz_offset)
        formatted_data_time = current_local.strftime('%A, %b %d | %I:%M %p')

        formatted_sunrise = sunrise_local.strftime('%I:%M %p')
        formatted_sunset = sunset_local.strftime('%I:%M %p')
        return templates.TemplateResponse(
            request=request,
            name='green.html',
            context={"data":data,
                     "sunrise":formatted_sunrise,
                     "sunset":formatted_sunset,
                     "current_time":formatted_data_time
                     }
        )
    else:
        error = response.json()
        return templates.TemplateResponse(
            request=request,
            name="red.html",
            context={"error_code": error}
        )
