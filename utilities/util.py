from time import sleep
from traceback import print_stack
from random import choice
from utilities.custom_logger import custom_logger
from string import (
    ascii_letters,
    ascii_lowercase,
    ascii_uppercase,
    digits)


class Util:
    log = custom_logger()

    def sleeping(self, sec, info=''):

        if info is not None:
            self.log.info("Wait :: {0} seconds for {}".format(str(sec), info))
            try:
                sleep(sec)
            except InterruptedError:
                print_stack()
    @staticmethod
    def get_alpha_num(length, types='letters'):
        """

        :param length:
        :param types: 'lower', 'upper', 'digits', 'mix'
        :return: string
        """

        alpha_num = ''
        if types == 'lower':
            case = ascii_lowercase
        elif types == 'upper':
            case = ascii_uppercase
        elif types == 'digits':
            case = digits
        elif types == 'mix':
            case = ascii_letters + digits
        else:
            case = ascii_letters
        return alpha_num.join(choice(case) for i in range(length))

    def get_unique_name(self, count=10):
        return self.get_alpha_num(count, 'lower')

    def get_unique_list(self, list_size=5, item_length=None):
        name_list = []
        for i in range(0, list_size):
            name_list.append(self.get_unique_name(item_length[i]))
        return name_list

    def verify_text_contains(self, actual_text, expected_text):

        if actual_text.lower() in expected_text.lower():
            self.log.info("Actual text '{}' exists".format(actual_text))
            return True
        else:
            self.log.info(
                "Actual text '{0}' doesn't appear in expected text {1}".format(
                    actual_text, expected_text))
            return False

    def verify_text_match(self, actual_text, expected_text):
        if actual_text.lower() == expected_text.lower():
            self.log.info("Actual text '{0}' match expected text '{1}'".format(
                actual_text, expected_text))
            return True
        else:
            self.log.info(
                "Actual text '{0}' doesn't match  expected text {1}".format(
                    actual_text, expected_text))
            return False

    @staticmethod
    def verify_list_match(actual_list, expected_list):
        return set(actual_list) == set(expected_list)

    @staticmethod
    def verify_list_contains(actual_list, expected_list):

        length = len(expected_list)
        for i in range(0, length):
            if expected_list[i] not in actual_list:
                return False
        else:
            return True
            # todo: verify that shit works, may need to swap lists
