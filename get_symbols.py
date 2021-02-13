import requests
from bs4 import BeautifulSoup
import re
import time
import random
import math

COUNT = 100
SECTORS = ["Technology"]


def get_how_many_symbols_in_sector(first_page):
    content = first_page.find("div", class_="Pos(r) Pos(r) Mih(265px)")
    return int(content.find("span", class_="Mstart(15px) Fw(500) Fz(s)").text.split(" ")[-2])


def calculate_how_many_pages(how_many_symbols):
    return math.ceil(how_many_symbols / COUNT)


def get_content_sector_page(page_url):
    page = requests.get(page_url)
    page_soup = BeautifulSoup(page.text, 'html.parser')
    return (page_soup)


def build_url(sector, offset, count):
    url = f'https://finance.yahoo.com/screener/predefined/ms_{sector.lower().replace(" ", "_")}?offset={offset}&count={count}'
    return url


def get_symbols():
    links_list = []
    for sector in SECTORS:
        current_links_list = []
        page = get_content_sector_page(build_url(sector, 0, COUNT))
        how_many_symbols = get_how_many_symbols_in_sector(page)
        how_many_pages = calculate_how_many_pages(how_many_symbols)
        tbody = page.find_all("tbody")
        current_links_list = current_links_list + tbody[0].find_all("a")
        for offset in range(100, how_many_pages * COUNT, 100):
            soup = get_content_sector_page(build_url(sector, offset, COUNT))
            tbody = soup.find_all("tbody")
            current_links_list = current_links_list + tbody[0].find_all("a")
        links_list = links_list + [[symbol.text, sector] for symbol in current_links_list]
    return links_list



