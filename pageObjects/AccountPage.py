from selenium.webdriver.common.by import By


class AccountPage:
    link_firstName_id = "input-firstname"
    link_lastName_id = "input-lastname"

    def __init__(self, driver):
        self.driver = driver

    def set_firstname(self, first_name):
        self.driver.find_element(by=By.ID, value=self.link_firstName_id).send_keys(first_name)

    def set_lastname(self, last_name):
        self.driver.find_element(by=By.ID, value=self.link_lastName_id).send_keys(last_name)
