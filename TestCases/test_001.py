import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import pageObjects.AccountPage
from pageObjects.HomePage import HomePage
from utilities.customLogger import LogGen


class TestFirst:
    loging = LogGen()

    def test_001(self):
        self.logger = self.loging.loggen()
        print(os.path.abspath(os.curdir))
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(15)
        self.driver.get("https://www.selenium.dev/documentation/webdriver/troubleshooting/logging/")
        self.logger.info("url is set")
        self.driver.maximize_window()
        self.homePage = HomePage(self.driver)
        self.homePage.click_my_account()
        self.homePage.click_register()
        self.accountPage = pageObjects.AccountPage.AccountPage(self.driver)
        self.accountPage.set_firstname("Name")
        sleep(15)
