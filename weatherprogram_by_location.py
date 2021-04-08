from pprint import pprint
import json
import requests
from secrets import OpenWeatherMapAccountKey

lat=input('Enter latitude : ')
lon=input('Enter longitude : ')


API_Key=OpenWeatherMapAccountKey

base_url='http://api.openweathermap.org/data/2.5/weather'
response=requests.get(base_url+"?lat="+lat+"&lon="+lon+"&appid="+API_Key)
weather_data=json.loads(response.text)
weather_description=weather_data['weather'][0]['description']
print(f'The weather in the location is {weather_description}')