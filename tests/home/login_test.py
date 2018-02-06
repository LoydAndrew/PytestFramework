from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class LoginTest(unittest.TestCase):
    @classmethod
    def test_valid_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/")
        driver.implicitly_wait(3)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("loyd@test.com")
        driver.find_element(By.ID, 'user_password').send_keys("123456")
        driver.find_element(By.NAME, 'commit').click()

        userIcon = driver.find_element(By.CSS_SELECTOR, '.gravatar')
        if userIcon is not None:
            print("Login Successfully")
        else:
            print("Didn't login")
        driver.quit()
    @classmethod
    def test_invalid_login(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/")
        driver.implicitly_wait(3)

        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.find_element(By.ID, "user_email").send_keys("loyd@testdfasd.com")
        driver.find_element(By.ID, 'user_password').send_keys("123454123")
        driver.find_element(By.NAME, 'commit').click()

        userIcon = driver.find_element(By.CSS_SELECTOR, '.gravatar')
        if userIcon is not None:
            print("Login Successfully")
        else:
            print("Didn't login")

if __name__ == '__main__':
    unittest.main(verbosity=2)


