from selenium.webdriver.common.by import By
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
    def get_login(self):
        return self.driver.find_element(By.LINK_TEXT, self._login_link)

    def get_email(self):
        return self.driver.find_element(By, self._email_field)

    def get_password(self):
        return self.driver.find_element(By, self._password_field)

    def get_button(self):
        return self.driver.find_element(By, self._login_button)

    # Actions on the elements
    def click_login(self):
        self.get_login().click()

    def enter_email(self, email):
        self.get_password().send_keys(email)

    def enter_password(self, password):
        self.get_password().send_keys(password)

    def submit_button(self):
        self.get_button().click()

    # Applying actions on the elements
    def login(self, email, password):
        self.click_login()
        self.enter_email(email)
        self.enter_password(password)
        self.submit_button()
