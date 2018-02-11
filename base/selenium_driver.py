from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import *
from time import strftime
from os import path
from traceback import print_stack
import inspect
import logging


def print_red(prt):
    print("\033[91m{}\033[00m".format(prt))


# noinspection PyMethodMayBeStatic,PyBroadException
class SeleniumDriver:
    def __init__(self, driver):
        self.driver = driver

    # getting locators
    # noinspection PyMethodMayBeStatic
    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID

        if locator_type == "xpath":
            return By.XPATH

        if locator_type == "css":
            return By.CSS_SELECTOR

        if locator_type == "class_name":
            return By.CLASS_NAME

        if locator_type == "link_text":
            return By.LINK_TEXT

        if locator_type == "tag_name":
            return By.TAG_NAME

        if locator_type == "name":
            return By.NAME

        if locator_type == "partial_link_text":
            return By.PARTIAL_LINK_TEXT

        else:
            print_red("Locator type " + str(locator_type) + " is not supported")
        return locator_type

    # getting elements using locators above
    def get_element(self, locator, locator_type="id"):
        element = None
        by_type = self.get_by_type(locator_type)
        try:
            element = self.driver.find_element(by_type, locator)
            if element is not None:
                print("Element %s was found by %s " % (locator, by_type))
        except:
            print_red("!!! Element %s was not found by %s !!!" % (locator, by_type))
        return element

    # clicking on the element
    def click_element(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            print(
                "Clicked on element with locator {0} and locator_type {0}".format(locator, locator_type))
        except:
            print(
                "Cannot click on the element with locator {0} and locator_type {0}".format(
                    locator,
                    locator_type))
            print_stack()

    def send_data(self, data, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            print(
                "Sent data to the element with locator {0} and locator_type {0}".format(locator, locator_type))
        except:
            print(
                "Cannot data to the element with locator {0} and locator_type {0}".format(
                    locator,
                    locator_type))
            print_stack()

    # waiting for element presence
    def wait_for_element(
            self,
            locator,
            locator_type="id",
            timeout=10,
            poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            wait = WebDriverWait(
                self.driver,
                timeout=timeout,
                poll_frequency=poll_frequency,
                ignored_exceptions=[
                    NoSuchElementException,
                    ElementNotSelectableException,
                    ElementNotVisibleException])
            element = wait.until(ec.element_to_be_clickable((
                by_type, locator))
            )
            print("Element appeared on the page")
        except:
            print("Element didn't appear on the page")
            print_stack()
        return element

    # getting screenshots
    def screenshot(self):

        """Implementation of  webdriver.save_screenshot()
         function that takes static directory and adds to it
         a name of the executing script + timestamp + png.
         Thus having dynamic  explicit name for screenshot """

        filename = str(path.basename(__file__)) + str(strftime("%Y-%m-%d %H:%M:%S")) + ".png"
        directory = '/home/andrew/Documents/workspace_automation/Automation/Screenshots/'
        screenshot_directory = directory + filename
        try:
            self.driver.save_screenshot(screenshot_directory)
            print("Screenshot was saved to: " + screenshot_directory)
        except NotADirectoryError:
            print("Directory error")

    # logging stuff
    def custom_logger(self, log_level):
        # getting the name of the method
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        # all messages

        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(filename="{0}.log".format(logger_name), mode='w')
        file_handler.setLevel(log_level)

        formatter = logging.Formatter(
            '%(asctime)s, %(name)s: %(levelname)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
