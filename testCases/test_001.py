import os
import pageObjects.AccountPage
from pageObjects.HomePage import HomePage
from utilities.customLogger import LogGen

class TestFirst:

    def test_001(self,setup):
        self.driver=setup
        self.logger = LogGen.loggen(self)
        self.driver.save_screenshot("..\\screenshots\\test.png")
        self.logger.debug("First logs has been captured")
        self.homePage = HomePage(self.driver)
        self.homePage.click_my_account()
        self.homePage.click_register()
        self.accountPage = pageObjects.AccountPage.AccountPage(self.driver)
        self.accountPage.set_firstname("Name")

