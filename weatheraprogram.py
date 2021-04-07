from pprint import pprint
import json
import requests

city_name=input('Enter city name:')
API_Key='b1c3f99842642e57065756f29ff7eba4'

base_url='http://api.openweathermap.org/data/2.5/weather'
response=requests.get(base_url+"?q="+city_name+"&appid="+API_Key)
weather_data=json.loads(response.text)
weather_description=weather_data['weather'][0]['description']
print(f'The weather in {city_name} is {weather_description}')