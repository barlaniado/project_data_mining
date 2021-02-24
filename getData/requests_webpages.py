import requests
from bs4 import BeautifulSoup
from configuration import project_conf
from utilities import utilities
from logs import logger


def get_content_sector_page(page_url):
    try:
        page = requests.get(page_url, headers=project_conf.HEADERS)
        page.raise_for_status() # raise an exception if status is not 200
    except requests.exceptions.ConnectionError:
        logger.logger.error(" ConnectionError - sector page scraping")
        raise requests.exceptions.ConnectionError
    except requests.exceptions.HTTPError:
        logger.logger.error(" HTTPError - sector page scraping")
        raise requests.exceptions.HTTPError
    response_code = page.status_code
    if response_code == 200:
        logger.logger.info("The code of the current request: " + str(page.status_code))
    elif  response_code == 404:
        logger.logger.warning("The code of the current request: " + str(page.status_code) + ":" + "Page not found")
    utilities.program_sleep()
    page_soup = BeautifulSoup(page.text, project_conf.HTML_PARSER)
    logger.logger.info("Return a BeautifulSoup object")
    return page_soup

def get_content_financial_statements(symbol):
    logger.logger.info(' Extract data from the financial statements of: ' + symbol)
    current_url= utilities.build_url_financials_symbol(symbol)
    logger.logger.info('Sending a request to: ' + current_url)
    try:
        page = requests.get(current_url, headers=project_conf.HEADERS)
        page.raise_for_status() # raise an exception if status is not 200
    except requests.exceptions.ConnectionError:
        logger.logger.error(" ConnectionError - sector page scraping")
        raise requests.exceptions.ConnectionError 
    logger.logger.info("The code of the current request: " + str(page.status_code))
    soup = BeautifulSoup(page.text,  project_conf.HTML_PARSER)
    logger.logger.info("Return a BeautifulSoup object")
    return soup
