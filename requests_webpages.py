import requests
from bs4 import BeautifulSoup
import project_conf
import utilities


def get_content_sector_page(page_url):
    page = requests.get(page_url, headers=project_conf.HEADERS)
    utilities.program_sleep()
    page_soup = BeautifulSoup(page.text, project_conf.HTML_PARSER)
    return page_soup
