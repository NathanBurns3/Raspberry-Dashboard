import requests
import os
import geocoder

def fetch_weather():
    weather_key = os.getenv('WEATHER_API_KEY')
    location = geocoder.ip('me')
    lat = location.latlng[0]
    lon = location.latlng[1]
    currentWeatherUrl = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={weather_key}&units=imperial"
    forcastWeatherUrl = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={weather_key}&lat={lat}&lon={lon}&units=imperial"
    currentWeatherResponse = requests.get(currentWeatherUrl)
    forcastResponse = requests.get(forcastWeatherUrl)
    if currentWeatherResponse.status_code == 200 and forcastResponse.status_code == 200:
        currentWeatherData = currentWeatherResponse.json()
        forcastData = forcastResponse.json()
        currentWeatherTemp = round(currentWeatherData['main']['temp'])
        currentWeather = currentWeatherData['weather'][0]['main']
        forcast = forcastData['list'][:6]
        formattedForecast = [
            {
                "date": entry["dt_txt"],
                "temp": round(entry["main"]["temp"]),
                "weather": entry["weather"][0]["main"]
            }
            for entry in forcast
        ]
        return currentWeatherTemp, currentWeather, formattedForecast
    else:
        return ["Error fetching weather data"]
    