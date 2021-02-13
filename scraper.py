import requests
from bs4 import BeautifulSoup
import re
import time
import random

SECTORS = ["Technology"]
headers = {
    'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}


def program_sleep(counter=None):
    if counter == None:
        time.sleep(random.randint(4, 7))
    else:
        if counter % 1000 == 0:
            time.sleep(180)
        elif counter % 100 == 0:
            time.sleep(60)
        else:
            time.sleep(random.randint(7, 12))


COUNT = 100


def get_symbol():
    links_list = []
    for sector in SECTORS:
        current_links_list = []
        for offset in range(0, 500, 100):
            url = f'https://finance.yahoo.com/screener/predefined/ms_{sector.lower().replace(" ", "_")}?offset={offset}&count={COUNT}'
            print(url)
            page = requests.get(url, headers=headers)
            soup = BeautifulSoup(page.text, 'html.parser')
            tbody = soup.find_all("tbody")
            current_links_list = current_links_list + tbody[0].find_all("a")
            program_sleep(counter=None)
        links_list = links_list + [[symbol.text, sector] for symbol in current_links_list]
    return links_list


def get_data_from_specific_symbol(list_symbol_sector, counter_symbols):
    delete_this_list = []
    program_sleep(counter_symbols)
    print(list_symbol_sector)
    current_url = f'https://finance.yahoo.com/quote/{list_symbol_sector[0]}/financials?p={list_symbol_sector[0]}'
    page = requests.get(current_url)
    print(page)
    soup = BeautifulSoup(page.text, 'html.parser')
    all_span = soup.find_all("span")
    if len(all_span) < 100:
        print(len(all_span))
        delete_this_list.append({list_symbol_sector[0]: soup})

    now_titles = 0
    now_net_income = 0
    title_list = []
    data_dict = {}
    data_indicator = 0
    for i in all_span:
        current_text = i.text
        if current_text == "Total Revenue":
            print(title_list)
            now_titles = 0
        if now_titles == 1:
            current_title = current_text
            title_list.append(current_title)
            data_dict[current_title] = {}
        elif now_net_income == 1:
            try:
                data_dict[title_list[counter]]["Net Income"] = int(current_text.replace(",", ""))
            except ValueError:
                data_dict[title_list[counter]]["Net Income"] = None
            counter += 1
            if counter == len(title_list):
                break
        if current_text == "Breakdown":
            now_titles = 1
        if current_text == "Net Income Common Stockholders":
            data_indicator = 1
            now_net_income = 1
            counter = 0
    if data_indicator == 1:
        return {list_symbol_sector[0]: [list_symbol_sector[1], data_dict]}
    else:
        return {list_symbol_sector[0]: [list_symbol_sector[1], "No data"]}


def all_data_from_all_symbols():
    counter_symbols = 0
    all_symbols_dict = {}
    list_symbols_sectors = get_symbol()
    for symbol_sector in list_symbols_sectors:
        current_dict = get_data_from_specific_symbol(symbol_sector, counter_symbols)
        all_symbols_dict.update(current_dict)
        counter_symbols += 1

    return all_symbols_dict


my_dict = all_data_from_all_symbols()
