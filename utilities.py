import time
import random
import math
import project_conf


def program_sleep(counter=None):
    """
    The function sends the program to sleep so as not to overload the server.
    """
    if counter == project_conf..PRAM_VALUE_SLEEP_NO_COUNTER:
        time.sleep(random.randint(project_conf..MIN_TIME_SLEEP_NO_COUNTER,
                                  project_conf.MAX_TIME_SLEEP_NO_COUNTER))
    else:
        if counter % project_conf.WHEN_LONG_SLEEP ==  project_conf.NO_REMAINDER:
            time.sleep(project_conf.TIME_LONG_SLEEP)
        elif counter % (project_conf.WHEN_MODERATE_SLEEP == project_conf.NO_REMAINDER:
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
    url = f'{project_conf.START_URL_SECTOR_PAGE}\
    {sector.lower().replace(project_conf.SPACE_TO_REPLACE,\
    project_conf.CHAR_INSTEAD_SPACE)}{project_conf.OFFSET_IS}{offset}{project_conf.COUNT_IS}{count}'
    return url


def build_url_financials_symbol(symbol):
    current_url = f'{project_conf.START_URL_FINANCIALS}{symbol}{project_conf.REST_URL_FINANCIALS}{symbol}'
    return current_url
    
