
from selenium.webdriver.common.by import By

from utilities.waits import Waits


class HomePage:
    link_myAccount_xpath = "//span[normalize-space()='My Account']"
    link_register_xpath = "//a[normalize-space()='Register']"
    link_login_linkText = "Login"

    def __init__(self, driver):
        self.driver = driver
        self.waitTime = Waits(self.driver)

    def click_my_account(self):
        # self.waitTime.presence_of_element("xpath",self.link_myAccount_xpath)
        self.waitTime.presence_of_element(By.XPATH, self.link_myAccount_xpath)
        self.driver.find_element(by=By.XPATH, value=self.link_myAccount_xpath).click()

    def click_register(self):
        self.waitTime.element_to_be_clickable(By.XPATH, self.link_register_xpath)
        self.driver.find_element(by=By.XPATH, value=self.link_register_xpath).click()
