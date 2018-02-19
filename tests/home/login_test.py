# from selenium import webdriver
# from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from utilities.test_status import CheckStatus
import pytest
import unittest


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.login_page = LoginPage(self.driver)
        self.test_status = CheckStatus(self.driver)


    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.login_page.login("loyd@test.comasdf", "123456asdf")
        login_false = self.login_page.verify_invalid_login()
        self.assertTrue(login_false, msg=u'Login with invalid credentials')
        #self.test_status.mark_final("test_invalid_login",login_false, "Invalid login")

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.login_page.login("loyd@test.com", "123456")
        login_title = self.login_page.verify_title()
        # self.assertTrue(login_title, u'Incorrect title')
        self.test_status.mark(login_title, 'Title is incorrect')
        login_true = self.login_page.verify_successful_login()
        #self.test_status.mark(login_true, "Didn't login and find avatar")
        #self.assertTrue(login_true, msg=u"Didn't login")
        self.test_status.mark_final(
            "test_valid_login", login_true, "Valid_login_test failed")


