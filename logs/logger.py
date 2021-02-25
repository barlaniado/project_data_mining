import logging
import sys
import os
import __main__


def create_logger(path, debug_mode = False):
    """ Creates a logger, when debug_mode = False the level of the logger is
    INFO, when debug_mode = False the level of the logger is DEBUG """
    if not debug_mode:
        set_level_logging = logging.INFO
    elif debug_mode:
        set_level_logging = logging.DEBUG
    logger = logging.getLogger('data_mining')
    logger.setLevel(set_level_logging)
    # Create Formatter
    formatter = logging.Formatter\
        ('%(asctime)s-%(levelname)s-FILE:%(filename)s-FUNC:%(funcName)s-LINE:%(lineno)d-%(message)s')
    # create a file handler and add it to logger
    file_handler = logging.FileHandler(path)
    file_handler.setLevel(set_level_logging)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(set_level_logging)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger


if os.path.basename(__main__.__file__) == "main_file.py":
    # When the top level file is main_file.py the level of the logger is INFO
    path_file = os.path.abspath(os.path.join(os.getcwd(), "logs", "data_minig.log"))
    logger = create_logger(path_file)
if os.path.basename(__main__.__file__) == "run_project_debug_level.py":
    path_file = os.path.join(os.path.abspath(os.path.join(os.getcwd(), os.pardir)),"logs","debug_logs.log")
    logger = create_logger(path_file, debug_mode=True)






