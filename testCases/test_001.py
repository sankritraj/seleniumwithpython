import time

from pageObjects.FormPage import FormPage
from pageObjects.HomePage import HomePage
from utilities.customLogger import LogGen


class TestFirst:
    logger = LogGen.loggen()

    def test_001(self, setup):
        self.driver = setup
        self.formPage = FormPage(self.driver)
        self.formPage.click_on_form()
        time.sleep(7)
