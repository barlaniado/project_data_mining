import requests
from bs4 import BeautifulSoup
from configuration import project_conf
from utilities import utilities
import logging

logger = logging.getLogger('data_mining')


def get_content_sector_page(page_url):
    try:
        page = requests.get(page_url, headers=project_conf.HEADERS)
    except requests.exceptions.ConnectionError:
        logger.error(" ConnectionError")
        raise requests.exceptions.ConnectionError
    logger.info("The code of the current request: " + str(page.status_code))
    utilities.program_sleep()
    page_soup = BeautifulSoup(page.text, project_conf.HTML_PARSER)
    logger.info("Return a BeautifulSoup object")
    return page_soup

def get_content_financial_statements(symbol):
    logger.info('extract data from the financial statements of: ' + symbol)
    current_url= utilities.build_url_financials_symbol(symbol)
    logger.info('Sending a request to: ' + current_url)
    page = requests.get(current_url, headers=project_conf.HEADERS)
    logger.info("The code of the current request: " + str(page.status_code))
    soup = BeautifulSoup(page.text,  project_conf.HTML_PARSER)
    logger.info("Return a BeautifulSoup object")
    return soup
