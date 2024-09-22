from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def get_by(locator):
    locator_map = {
        "id": "BY.ID",
        "xpath": "By.XPATH",
        "link_text": "BY.LINK_TEXT"

    }
    return locator_map[locator]


class Waits:
    def __init__(self, driver):
        self.driver = driver

    def element_to_be_clickable(self, by, locator_value):
        try:
            # wait 10 seconds before looking for element
            WebDriverWait(self.driver, 40).until(ec.element_to_be_clickable((by, locator_value)))
            print("Waiting")
        except Exception as e:
            print("exception error:  " + e.__str__())

    def presence_of_element(self, by, locator_value):
        try:
            # wait 10 seconds before looking for element
            WebDriverWait(self.driver, 20).until(ec.visibility_of_element_located((by, locator_value)))
            print("Waiting")
        except Exception as e:
            print("exception error" + e.__str__())
