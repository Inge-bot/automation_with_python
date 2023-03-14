import variables
import requests

apiKeyVar = variables.api_key

# Populate data text file with fields: city, time, temperature, condition
# Get data for the next 5 days
# Append to text file 'data.txt'

# NOTE need to wait a few hours for the API to become active
def city_weather(city, forecast_days):
    url = f"https:/api.openweathermap.org/data/2.5/weather?q={city}&appid=bbb6fa7e576aa4d728087673b64b7d08"
    r = requests.get(url)
    # create json object
    weather_forecast = r.json()

    return weather_forecast

print(city_weather(city="london", forecast_days=4))
