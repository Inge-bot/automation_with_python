import requests
import json
import os
from config import api_key

# API keys are available from https://openweathermap.org/
# Get the absolute path to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the file
relative_file_path = 'temp/data.txt'

# Combine the script directory and relative file path to get the absolute file path
absolute_file_path = os.path.join(script_dir, relative_file_path)

def get_weather(city):
    # Get weather forecast for specific city
    weather_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    content = requests.get(weather_url).text
    content_dict = json.loads(content)

    # creates python list
    list_content = content_dict["list"]

    # loop through list and get values
    for w_entry in list_content:
        time = w_entry['dt_txt']
        temperature = w_entry['main']['temp']
        condition = w_entry['weather'][0]['description']
        # Append to file
        file = open(absolute_file_path, 'a')
        file.write(f'{city}, {time}, {temperature}, {condition}\n')
        file.close()

# call function
get_weather('Amsterdam')