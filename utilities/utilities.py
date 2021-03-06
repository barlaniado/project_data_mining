import time
import random
import math
from configuration import project_conf
import json
from datetime import datetime
import os

def program_sleep(counter=None):
    """
    The function sends the program to sleep so as not to overload the server.
    """
    if counter == project_conf.VALUE_SLEEP_NO_COUNTER:
        time.sleep(random.randint(project_conf.MIN_TIME_SLEEP_NO_COUNTER,
                                  project_conf.MAX_TIME_SLEEP_NO_COUNTER))
    else:
        if counter % project_conf.WHEN_LONG_SLEEP == project_conf.NO_REMAINDER:
            project_conf.logger.logger.debug(project_conf.LONG_SLEEP_DEBUG_LOGGER)
            time.sleep(project_conf.TIME_LONG_SLEEP)
        elif counter % project_conf.WHEN_MODERATE_SLEEP == project_conf.NO_REMAINDER:
            time.sleep(project_conf.TIME_MODERATE_SLEEP)
        else:
            time.sleep(random.randint(project_conf.MIN_SHORT_SLEEP, project_conf.MAX_SHORT_SLEEP))


def get_how_many_symbols_in_sector(first_page):
    """
    the function retrieve the number of companies in each sector.
    """
    content = first_page.find(project_conf.MAIN_TAG_HOW_MANY_SYMBOLS, class_=project_conf.MAIN_CLASS_HOW_MANY_SYMBOLS)
    return int(content.find(project_conf.SUB_TAG_HOW_MANY_SYMBOLS,\
                            class_=project_conf.SUB_CLASS_HOW_MANY_SYMBOLS).text.\
               split(project_conf.CHER_SPLIT_TO_GET_HOW_MANY_SYMBOLS)[project_conf.INDEX_HOW_MANY_AFTER_SPLIT])


def calculate_how_many_pages(how_many_symbols):
    """
    The function receive the number of companies in a sector and calculate the number of pages.
    Each page contain 100 companies at most.
    """
    return math.ceil(how_many_symbols / project_conf.COUNT)


def build_url(sector, offset, count):
    """
    The function creates the url to the sector page.
    """
    url = f"{project_conf.START_URL_SECTOR_PAGE}" \
          f"{sector.lower().replace(project_conf.SPACE_TO_REPLACE,project_conf.CHAR_INSTEAD_SPACE)}" \
          f"{project_conf.OFFSET_IS}{offset}{project_conf.COUNT_IS}{count}"
    return url


def build_url_financials_symbol(symbol):
    """
    The function gets a symbol and returns the url of the financials reports of the company
    """
    current_url = f'{project_conf.START_URL_FINANCIALS}{symbol}{project_conf.REST_URL_FINANCIALS}{symbol}'
    return current_url


def build_message_how_many_symbols_pages_for_logger(sector, how_many_symbols, how_many_pages):
    """
    The function gets: sector, how many symbols in this sector (how_many_symbols) and how many
    pages the program have to scrape and created from the data a message for the logger.
    The function returns a string.
    """
    return f'The {sector} has {how_many_symbols} symbols and {how_many_pages} pages'


def create_timestamp():
    """
    The function returns the time stamp of this moment.
    """
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    return timestamp


def check_if_json_folder_exist_and_create():
    """
    The function checks whether the folder containing the Json files
    with the obtained data exists or not. If not the function creates this folder.
    """
    if not os.path.exists(os.path.abspath(os.path.join(os.getcwd(),project_conf.JSON_FILES_PATH))):
        os.makedirs(project_conf.JSON_FILES_PATH)
        project_conf.logger.logger.info(project_conf.CREATE_JSON_FOLDER_MESSAGE)


def to_json_daily_data(daily_data):
    """
    The function gets the obtained daily data and write it to a json file.
    The name of the file: "timestamp_daily_data.json"
    """
    check_if_json_folder_exist_and_create()
    path_file = os.path.abspath(os.path.join(os.getcwd(),project_conf.JSON_FILES_PATH , str(create_timestamp()).replace(".", "-") + project_conf.DAILY_DATA_FILE_NAME))
    print(path_file)
    with open(path_file, 'w') as outfile:
        json.dump(daily_data, outfile, indent=4)
    project_conf.logger.logger.info("A json file with the daily data was created")


def to_json_financials(financials_data):
    """
    The function gets the obtained data from the financials reports and write it to a json file.
    The name of the file: "timestamp_financials.json
    """
    path_file = os.path.abspath(os.path.join(os.getcwd(),project_conf.JSON_FILES_PATH , str(create_timestamp()).replace(".", "-") + project_conf.FINANCIALS_DATA_FILE_NAME))
    print(path_file)
    with open(path_file, 'w') as outfile:
        json.dump(financials_data, outfile, indent=4)
    project_conf.logger.logger.info("A json file with the financials data was created")


def to_json_all(daily_data, financials_data):
    """
    The function gets the data that obtained and calls to the functions: to_json_financials and to_json_daily_data.
    """
    to_json_daily_data(daily_data)
    to_json_financials(financials_data)
