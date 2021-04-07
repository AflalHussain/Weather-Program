from pprint import pprint
import json
import requests
from secrets import OpenWeatherMapAccountKey

city_name=input('Enter city name:')
API_Key=OpenWeatherMapAccountKey

base_url='http://api.openweathermap.org/data/2.5/weather'
response=requests.get(base_url+"?q="+city_name+"&appid="+API_Key)
weather_data=json.loads(response.text)
weather_description=weather_data['weather'][0]['description']
print(f'The weather in {city_name} is {weather_description}')