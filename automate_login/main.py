"Create Chrome driver and automatically scrape html text"
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

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

    # use Chrome driver to navigate to login page
    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

# def clean_text(text):
#     "Extract temperature from text and convert into float"
#     output = float(text.split(": ")[1])
#     return output

if __name__ == '__main__':
    def main():
        "Scrape html element's text"
        driver = create_driver()
        # select the username field and input username
        driver.find_element(by="id", value="id_username").send_keys("automated")
        time.sleep(1)
        # select password field and input password; click on enter
        driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
        # print current url after logging in
        print(driver.current_url)
        

print(main())
