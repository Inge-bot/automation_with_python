# import flask class
from flask import Flask, jsonify
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
    'Get currency rate'
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find('span', class_='ccOutputRslt').get_text()
    rate = float(rate[:-4])

    return rate

# holds string of script 'main'
app = Flask(__name__)

@app.route('/')
def home():
    'App home page'
    return '<h1>Currency Rate API</h1> <p>Example API URL: /api/v1/usd-eur</p>'

@app.route('/api/v1/<input_curr>-<output_curr>')

def api(input_curr, output_curr):
    'Create API'
    rate = get_currency(input_curr, output_curr)
    result_dict = {"input_currency": input_curr, "output_currency": output_curr, "rate": rate}
    return jsonify(result_dict)
app.run()
