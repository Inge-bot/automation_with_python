"Create Chrome driver and automatically scrape html text"
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import variables

service = Service(variables.DRIVER_PATH)

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

if __name__ == '__main__':
    def main():
        "Scrape html element's text"
        driver = create_driver()
        # get dynamic element by staying on page for 2secs
        time.sleep(2)
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        return clean_text(element.text)
    