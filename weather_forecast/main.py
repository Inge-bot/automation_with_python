"Module gets 3 hourly weather forecast for specific city for a period of several days"
import os
import json
import requests
from config import api_key

# API keys are available from https://openweathermap.org/
# Get the absolute path to the directory where the script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the file
RELATIVE_FILE_PATH = 'temp/data.txt'

# Combine the script directory and relative file path to get the absolute file path
absolute_file_path = os.path.join(SCRIPT_DIR, RELATIVE_FILE_PATH)

def get_weather(city):
    "Get weather forecast for specific city"
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
