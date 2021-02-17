import requests_webpages
from datetime import datetime
import project_conf
import utilities
import logging
import logger


logger = logging.getLogger('data_mining')


def get_price(tr):
    """
    The function retrieve the daily price of a stock of a company.
    """
    data_list = tr.find_all(project_conf.TAG_TO_RETRIEVE_DAILY_DATA, class_=project_conf.CLASS_GET_DAILY_DATA)
    price = data_list[project_conf.PRICE_INDEX].text
    return price


def get_symbol(tr):
    """
    The function retrieve the symbol of a company.
    """
    data_list = tr.find_all("a")
    symbol = data_list[0].text
    return symbol


def get_price_change(tr):
    """
    The function retrieve the difference between the last price of a stock from yesterday
    and the current price of that stock.
    """
    data_list = tr.find_all(project_conf.TAG_TO_RETRIEVE_DAILY_DATA, class_= project_conf.CLASS_GET_DAILY_DATA)
    price_change = data_list[project_conf.PRICE_CHANGE_INDEX].text
    return price_change


def get_price_change_percentage(tr):
    """
    The function retrieve the difference in percentage, between the last price of a stock from yesterday
    and the current price of that stock.
    """
    data_list = tr.find_all(project_conf.TAG_TO_RETRIEVE_DAILY_DATA, class_=project_conf.CLASS_GET_DAILY_DATA)
    price_change_percentage = data_list[project_conf.PRICE_CHANGE_PERCENTAGE].text
    return price_change_percentage


def get_volume(tr):
    """
    The function retrieve the volume of a company.
    """
    data_list = tr.find_all(project_conf.TAG_TO_RETRIEVE_DAILY_DATA, class_=project_conf.CLASS_GET_DAILY_DATA)
    volume = data_list[project_conf.VOLUME_CURRENT_DAY].text
    return volume


def get_avg_vol(tr):
    """
    The function retrieve the average volume of a company.
    """
    data_list = tr.find_all(project_conf.FIND_AVG_VOL)
    for data in data_list:
        if data.attrs[project_conf.ATTRS_AVG_VOL] == project_conf.TITLE_AVG_VOL:
            avg_vol = data.text
            break # I put break because I need the first one.
    return avg_vol


def build_sectors_and_daily_dict(tbody, sector, symbol_sector_dict, daily_dict):
    """
    The funcion gets content of a table in spesific sector page (tbody), and the sector itself (sector).
    In addtion, the function gets two dictionaries
    1) Contain the stock symbols and their sectors (symbol_sector_dict)
    2) Contain the daily data of the stocks (daily_dict)
    the function adds more data to these dictionary and changes them inplace.
    """
    
    all_tr = tbody.find_all(project_conf.FIND_LINE_TAG)
    for tr in all_tr:
        current_symbol = get_symbol(tr)
        dateTimeObj = datetime.now()
        if current_symbol in symbol_sector_dict:
            symbol_sector_dict[current_symbol].append(sector)
        else:
            symbol_sector_dict[current_symbol] = [sector]
        if current_symbol not in daily_dict:
            daily_dict[current_symbol] = {project_conf.KEY_TIME: dateTimeObj,
                                          project_conf.KEY_PRICE: get_price(tr),
                                          project_conf.KEY_PRICE_CHANGE: get_price_change(tr),
                                          project_conf.KEY_PRICE_CHANGE_PERCENTAGE: get_price_change_percentage(tr),
                                          project_conf.KEY_VOLUME:  get_volume(tr),
                                          project_conf.KEY_AVG_VOLUME: get_avg_vol(tr)}
    logger.info(project_conf.LOGGER_MESSAGE_BUILD_DAILY_SECTOR_DICT)
    return


def scrape_sector_pages():
    """
    The function iterates over a list of sector and creates two dictionaries:
    1) Contain the stock symbols and their sectors (symbol_sector_dict)
    2) Contain the daily data of the stocks (daily_dict)
    The function returns tuple of these two dictionaries (symbol_sector, daily_data)
    """

    logger.info(project_conf.START_SCRAPE_SECTOR_MESSAGE)
    daily_data = {}
    symbol_sector = {}
    for sector in project_conf.SECTORS:
        page = requests_webpages.get_content_sector_page\
            (utilities.build_url(sector, project_conf.OFFSET_OF_FIRST_PAGE_SECTOR, project_conf.COUNT))
        how_many_symbols = utilities.get_how_many_symbols_in_sector(page)
        how_many_pages = utilities.calculate_how_many_pages(how_many_symbols)
        logger.info(utilities.build_message_how_many_symbols_pages_for_logger
                    (sector, how_many_symbols, how_many_pages))
        tbody = page.find_all(project_conf.TAG_TABLE_IN_PAGE)
        if len(tbody) > 1:
            logger.warning(project_conf.LOGGER_WARNING_MESSAGE)
        tbody = tbody[project_conf.TABLE_CONTENT_INDEX]
        build_sectors_and_daily_dict(tbody, sector, symbol_sector, daily_data)
        for offset in range(project_conf.HOW_MANY_SYMBOLS_EACH_PAGE, how_many_pages * project_conf.COUNT,
                            project_conf.HOW_MANY_SYMBOLS_EACH_PAGE):
            page = requests_webpages.get_content_sector_page(utilities.build_url(sector, offset, project_conf.COUNT))
            tbody = page.find_all(project_conf.TAG_TABLE_IN_PAGE)
            if len(tbody) > project_conf.ASSUMPTION_TBODY_LEN:
                logger.warning(project_conf.LOGGER_WARNING_MESSAGE)
            tbody = tbody[project_conf.TABLE_CONTENT_INDEX]
            build_sectors_and_daily_dict(tbody, sector, symbol_sector, daily_data)
            logger.info(project_conf.FINISH_SECTOR_SCRAPING_MESSAGE)
            logger.info(project_conf.LEN_OF_DICT_SECTOR_LOGGER_MESSAGE + str(len(symbol_sector)) + "\n" +
                        project_conf.LEN_OF_DICT_DAILY_LOGGER_MESSAGE + str(len(daily_data)))
    return symbol_sector, daily_data
