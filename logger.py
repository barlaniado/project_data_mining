import logging
import sys


def define_logger():
    logger = logging.getLogger('data_mining')
    logger.setLevel(logging.DEBUG)

    # Create Formatter
    formatter = logging.Formatter('%(asctime)s-%(levelname)s-FILE:%(filename)s-FUNC:%(funcName)s-LINE:%(lineno)d-%(message)s')

    # create a file handler and add it to logger
    file_handler = logging.FileHandler('data_mining.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger