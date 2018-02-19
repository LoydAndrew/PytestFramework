import inspect
import logging

# Implementation of custom_logger

def custom_logger(log_level=logging.DEBUG):
    # getting the name of the method
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)
    if not len(logger.handlers): # need this not to call handler multiply times
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