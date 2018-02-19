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


def print_yel(prt):
    print("\033[33m{}\033[00m".format(prt))  # \033m[00m needed for not printing everything in yellow


def custom_logger(log_level=logging.DEBUG):
    # getting the name of the method
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    if not len(logger.handlers):
         # all messages
        directory = '/home/andrew/Documents/workspace_automation/PytestFramework/logs/'
        logger.setLevel(logging.DEBUG)

        file_handler = logging.FileHandler(directory +"pytest.log", mode='a')
        file_handler.setLevel(log_level)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger


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
            custom_logger().error("Locator type " + str(locator_type) + " is not supported")
        return locator_type


    # finding if element is present
    def is_present (self, locator, locator_type=id):
        element = None
        by_type = self.get_by_type(locator_type)
        try:
            element = self.driver.find_element(by_type , locator)
            if element is not None:
                custom_logger().info(
                    "Element with locator {0} and locator_type {1} is present".format(locator, locator_type))
                return True
        except:
            custom_logger().error(
                "Element with locator {0} and locator_type {1} is not located".format(locator, locator_type))
            return False




    # getting elements using locators above
    def get_element(self, locator, locator_type="id"):
        element = None
        by_type = self.get_by_type(locator_type)
        try:
            element = self.driver.find_element(by_type, locator)
            if element is not None:
                custom_logger().info("Element %s was found by %s " % (locator, locator_type))
        except:
            custom_logger().error("!!! Element %s was not found by %s !!!" % (locator, by_type))
        return element

    # clicking on the element
    def click_element(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            custom_logger().info(
                "Clicked on element with locator '{0}' and locator_type '{1}'".format(
                    locator,
                    locator_type))
        except:
            custom_logger().error(
                "Couldn't click on the element with locator '{0}' and 'locator_type' {1}".format(
                    locator,
                    locator_type))
            print_stack()

    def send_data(self, data, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
            custom_logger().info(
                "Sent data to the element with locator '{0}' and locator_type '{1}'".format(
                    locator,
                    locator_type))
        except:
            custom_logger().error(
                "Cannot sent data to the element with locator '{0}' and locator_type '{1}'".format(
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
            custom_logger().info("Element appeared on the page")
        except:
            custom_logger().error("Element didn't appear on the page")
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

