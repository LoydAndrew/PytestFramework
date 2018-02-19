from selenium import webdriver
# from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import pytest
import unittest


class LoginTest(unittest.TestCase):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://letskodeit.teachable.com/")
    driver.implicitly_wait(2)
    login_page = LoginPage(driver)

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.login_page.login("loyd@test.comasdf", "123456asdf")
        login_false = self.login_page.verify_invalid_login()
        self.assertTrue(login_false, msg=u'Login with invalid credentials')

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.login_page.login("loyd@test.com", "123456")
        login_true = self.login_page.verify_successful_login()
        self.assertTrue(login_true, msg=u"Didn't login")
        self.driver.quit()

