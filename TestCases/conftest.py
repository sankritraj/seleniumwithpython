import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup():
    baseURL="https://demoqa.com/"
    ser = Service("C:\\Users\\niraj\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
    driver = webdriver.Chrome(service=ser)
    driver.implicitly_wait(15)
    driver.get(baseURL)
    driver.maximize_window()
    return driver
