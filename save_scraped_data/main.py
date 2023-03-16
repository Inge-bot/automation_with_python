"Scrape data and save to file"
import time
import datetime
import sched
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import variables

service = Service(variables.DRIVER_PATH)

# create schedule class instance
s = sched.scheduler(time.time, time.sleep)

def run_scheduler():
    "call main function every 2 seconds"
    s.enter(2,1, run_scheduler)
    main()

def create_driver():
    "Create Chrome driver"
    # driver configurations - options to make browsing easier
    options = webdriver.ChromeOptions()
    # remove possible interference of infobars
    options.add_argument("disable-infobar")
    # start browser as maximized - so content doesn"t change
    options.add_argument("start-maximized")
    # remove linux machine issues
    options.add_argument("disable-dev-shm-usage")
    # greater privileges if sandboxing is disabled
    options.add_argument("no-sandbox")
    # avoid being detected by the browser
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    # use Chrome driver
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    "Extract temperature from text and convert into float"
    output = float(text.split(": ")[1])
    return output

# create file and save to text file every 2 seconds
def file_name():
    "Create dynamic file name with date and time"
    now = datetime.datetime.now()
    time_now = now.strftime('%Y-%m-%d.%H-%M-%S')
    print(time_now)
    return time_now

def write_file(text):
    "Write content to file"
    file_title = file_name()
    print(file_title, "file")
    file = open(f'files/{file_title}.txt', 'w+')
    file.write(text)
    file.close()

def main():
    "Scrape html element's text"
    driver = create_driver()
        # get dynamic element by staying on page for 2secs
    time.sleep(2)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    dynamic_text = str(clean_text(element.text))
    write_file(dynamic_text)
    return dynamic_text

if __name__ == '__main__':
    s.enter(2, 1, run_scheduler)
    s.run()
