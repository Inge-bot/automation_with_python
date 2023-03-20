"""
Result can be used in app to highlight incorrect use of words or make suggests for alternatives
"""
import json
import requests

def grammar_checker(text, language):
    "Use the language tool API to check grammar in a specific language"
    URL = 'https://api.languagetoolplus.com/v2/check'
    # pass data as dictionary
    data = {
        'text': text,
        'language': language
    }
    response = requests.post(URL, data=data)

    # convert string into dictionary for easier text extraction
    result = json.loads(response.text)

    return result
