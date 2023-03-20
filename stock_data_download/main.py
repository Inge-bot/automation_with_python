"download historical stock data"
from datetime import datetime
import time
import requests # download files

if __name__ == '__main__':
    def main():
        "download data and write to csv file"

        # Request stock code e.g. SNAP
        ticker = input('Enter ticker symbol: ')

         # request stock dates
        from_date = input('Enter start date in yyyy/mm/dd format: ')
        to_date = input('Enter end date in yyyy/mm/dd format: ')

        from_datetime = datetime.strptime(from_date, '%Y/%m/%d') # convert dates' format
        to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

        from_epoch = int(time.mktime(from_datetime.timetuple()))
        to_epoch = int(time.mktime(to_datetime.timetuple()))

        url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true'
        
        # impersonate browser to allow file download
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

        # grab content of request
        content = requests.get(url, headers=headers).content

        # write byte data to file
        with open('temp/data.csv', 'wb') as file:
            file.write(content)

main()
