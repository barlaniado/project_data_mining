import logging
import sys
import os
import argparse


class Logger:
    """
    Creates a logger, when debug_mode = False the level of the logger is
    INFO, when debug_mode=True the level of the logger is DEBUG
    """
    def __init__(self, debug_mode):
        print('**** logger')
        self.mode = debug_mode
        if not debug_mode:
            set_level_logging = logging.INFO
            file_name = 'data_mining_info_level.log'
        else:
            set_level_logging = logging.DEBUG
            file_name = 'data_mining_debug_level.log'
        path = os.path.abspath(os.path.join(os.getcwd(), "logs", file_name))
        self.logger = logging.getLogger('data_mining')
        self.logger.setLevel(set_level_logging)
        # Create Formatter
        formatter = logging.Formatter\
            ('%(asctime)s-%(levelname)s-FILE:%(filename)s-FUNC:%(funcName)s-LINE:%(lineno)d-%(message)s')
        # create a file handler and add it to logger
        file_handler = logging.FileHandler(path)
        file_handler.setLevel(set_level_logging)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(set_level_logging)
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)








