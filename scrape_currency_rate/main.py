from bs4 import BeautifulSoup
import requests

def get_currency(in_c, out_c):
    'Get currency rates'
    url = f'https://www.x-rates.com/calculator/?from={in_c}&to={out_c}&amount=1'
    content = requests.get(url).text
    # parse content
    soup = BeautifulSoup(content, 'html.parser')
    # find the currency value span element, and extract the text
    rate = soup.find('span', class_="ccOutputRslt").get_text()
    # remove currency code and change data type
    rate = float(rate[:-4])
    return rate
