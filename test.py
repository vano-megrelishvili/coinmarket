import logging
import example

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('sample.log')
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


logger.info(add(2, 3))
