from selenium import webdriver

class WebdriverFactory:

    def __init__(self, browser):

        self.browser = browser

    def get_driver_instance(self):
        base_url = "https://letskodeit.teachable.com/"
        if self.browser == "ieexplorer":
            driver = webdriver.Ie()

        elif self.browser == "firefox":
            driver = webdriver.Firefox()

        elif self.browser == "chrome":
            driver = webdriver.Chrome()

        else:
            driver = webdriver.Chrome()

        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(base_url)
        return driver