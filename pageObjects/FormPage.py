from selenium.webdriver.common.by import By

from utilities.waits import Waits


class FormPage:
    Elements_xpath = "(//h5[normalize-space()='Elements'])[1]"
    form_xpath = "//div[@class='home-body']//div[2]//div[1]//div[2]//*[name()='svg']"

    def __init__(self, driver):
        self.driver = driver
        self.waitTime = Waits(self.driver)

    def click_on_element(self):
        self.waitTime.presence_of_element(By.XPATH, self.Elements_xpath)
        self.waitTime.element_to_be_clickable(By.XPATH, self.Elements_xpath)
        self.driver.find_element(By.XPATH, self.Elements_xpath).click()

    def click_on_form(self):
        self.waitTime.presence_of_element(By.XPATH, self.form_xpath)
        self.driver.find_element(By.XPATH,self.form_xpath).click()
