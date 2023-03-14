from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import variables

service = Service(variables.driver_path)

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

def main():
    "Scrape html element text"
    driver = create_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text

print(main())
