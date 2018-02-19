# Checking statuses of assertions
from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_logger
import logging
import unittest
from traceback import print_stack



class CheckStatus(SeleniumDriver, unittest.TestCase):
    log = custom_logger(logging.INFO)

    def __init__(self, driver):

        super(CheckStatus, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info("Successful verification:: " )
                else:
                    self.screenshot(resultMessage)
                    self.result_list.append("FAILED")
                    self.log.error("Failed verification:: " + resultMessage)
            else:
                self.screenshot(resultMessage)
                self.result_list.append("FAILED")
                self.log.error(
                    "Failed verification, check if result is None:: " + resultMessage)
        except:
            self.screenshot(resultMessage)
            self.result_list.append("FAILED")
            self.log.error("Exception occured in verification!!!")
            print_stack()

    def mark(self, result, resultMessage):
        """
        Mark the result of the verification
        :param testName:
        :param result:
        :param resultMessage:
        :return:
        """
        self.set_result(result,resultMessage)

    def mark_final(self, testName, result, resultMessage):
        """
        Mark the final result of the verification
        :param testName:
        :param result:
        :param resultMessage:
        :return:
        """
        self.set_result(result, resultMessage)
        if "FAILED" in self.result_list:
            self.log.error(testName + "###test FAILED " + resultMessage)
            self.result_list.clear()
            self.assertFalse(True, 'There is failed tests')
        else:
            self.log.info(testName + "### test Successful")
            self.result_list.clear()
            assert True == True

