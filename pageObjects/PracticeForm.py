class PracticeForm:
    def __int__(self, driver):
        self.driver = driver

    field_name_xpath= "//input[@id='firstName']"
    field_email_xpath="//input[@id='userEmail']"
    button_gender_male_xpath="//label[@for='gender-radio-1']"
    button_gender_female_xpath = "//label[@for='gender-radio-2']"
    field_phone_id="userNumber"

