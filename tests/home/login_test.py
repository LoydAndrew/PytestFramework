from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import pytest
import unittest


class LoginTest(unittest.TestCase):
    # @pytest.mark.run(order=1)
    def test_valid_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/")
        driver.implicitly_wait(2)

        login_page = LoginPage(driver)
        login_page.login("loyd@test.com", "123456")
        user_icon = driver.find_element(By.CSS_SELECTOR, '.gravatar')

        if user_icon is not None:
            print("---> Login Successfully")
        else:
            print("Didn't login")
        driver.quit()

    # def test_invalid_login(self):
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()
    #     driver.get("https://letskodeit.teachable.com/")
    #     driver.implicitly_wait(3)
    #
    #     login_page = LoginPage(driver)
    #     login_page.login("loyd@testfa.com", "")
    #
    #     error = '---> Login with invalid credentials'
    #     user_icon = driver.find_element(By.CSS_SELECTOR, '.gravatar')
    #     if user_icon is not None:
    #         self.assertFalse(user_icon, error)  # if user_icon is not present aka TRUE  - it will pass the test
    #     driver.quit()
