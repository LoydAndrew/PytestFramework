from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.custom_logger import custom_logger
from utilities.util import Util


class BasePage(SeleniumDriver):

    def __init__(self, driver):

        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()
        self.log = custom_logger()

    # noinspection PyUnusedLocal
    def verify_page_title(self, title):

        # noinspection PyBroadException
        try:
            self.get_title()
            return self.util.verify_text_contains(actual_text='',
                                                  expected_text='')
        except:
            self.log.error("Failed to identify text")
            print_stack()
            return False
