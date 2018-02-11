# from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver


class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    # End of locators

    # Getting all the elements
    # def get_login(self):
    #     return self.driver.find_element(By.LINK_TEXT, self._login_link)
    #
    # def get_email(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def get_password(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def get_button(self):
    #     return self.driver.find_element(By.NAME, self._login_button)

    # ======Became redundant after using "custom_driver Class" where are exist all
    # the implementations of finding and interacting with elements on page========

    # Actions on the elements
    def click_login(self):
        self.click_element(self._login_link, "link_text")

    def enter_email(self, email):
        self.send_data(email, self._email_field)

    def enter_password(self, password):
        self.send_data(password, self._password_field)

    def submit_button(self):
        self.click_element(self._login_button, 'name')

    # Applying actions on the elements
    def login(self, email, password):
        self.click_login()
        self.enter_email(email)
        self.enter_password(password)
        self.submit_button()
