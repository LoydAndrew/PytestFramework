# from selenium import webdriver
# from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import pytest
import unittest


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.login_page = LoginPage(self.driver)

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

