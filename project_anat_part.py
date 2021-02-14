import requests
from bs4 import BeautifulSoup
import re
import time
import random
from datetime import datetime
import math
#SECTORS = ["Technology", "Basic materials", "Healthcare", "Energy"]
SECTORS = ["Basic materials"]
COUNT = 100
headers = {
    'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

def program_sleep(counter=None):
    if counter == None:
        time.sleep(random.randint(4, 7))
    else:
        if counter % 1000 == 0:
            time.sleep(120)
        elif counter % 100 == 0:
            time.sleep(30)
        else:
            time.sleep(random.randint(7, 12))

def get_content_sector_page(page_url):
    page = requests.get(page_url, headers = headers)
    program_sleep()
    page_soup = BeautifulSoup(page.text, 'html.parser')
    return page_soup


def get_how_many_symbols_in_sector(first_page):
    content = first_page.find("div", class_="Pos(r) Pos(r) Mih(265px)")
    return int(content.find("span", class_="Mstart(15px) Fw(500) Fz(s)").text.split(" ")[-2])

def calculate_how_many_pages(how_many_symbols):
    return math.ceil(how_many_symbols / COUNT)

def build_url(sector, offset, count):
    url = f'https://finance.yahoo.com/screener/predefined/ms_{sector.lower().replace(" ", "_")}?offset={offset}&count={count}'
    return url

def get_price(tr):
    data_list = tr.find_all('span', class_="Trsdu(0.3s)")
    price = data_list[0].text
    return price

def get_symbol(tr):
    data_list = tr.find_all("a")
    symbol = data_list[0].text
    return symbol

def get_price_change(tr):
    data_list = tr.find_all('span', class_="Trsdu(0.3s)")
    price_change = data_list[1].text
    return price_change


def get_price_change_percentage(tr):
    data_list = tr.find_all('span', class_="Trsdu(0.3s)")
    price_change_percentage = data_list[2].text
    return price_change_percentage

def get_volume(tr):
    data_list = tr.find_all('span', class_="Trsdu(0.3s)")
    volume = data_list[3].text
    return volume

def get_avg_vol(tr):
    data_list = tr.find_all('td')
    for data in data_list:
        if data.attrs['aria-label'] == "Avg Vol (3 month)":
            avg_vol = data.text
            break # I put break because I need the first one.
    return avg_vol

def build_sectors_and_daily_dict(tbody, sector, symbol_sector_dict, daily_dict):
    all_tr = tbody.find_all("tr")
    for tr in all_tr:
        current_symbol = get_symbol(tr)
        dateTimeObj = datetime.now()
        if current_symbol in symbol_sector_dict:
            symbol_sector_dict[current_symbol].append(sector)
        else:
            symbol_sector_dict[current_symbol] = [sector]
        if current_symbol not in daily_dict:
            daily_dict[current_symbol] = {"Time": dateTimeObj, "Price": get_price(tr), "Price change": get_price_change(tr), "Percentage":  get_price_change_percentage(tr), "Volume":  get_volume(tr), "Avg Vol (3 month)": get_avg_vol(tr)}

def scrape_sector_pages():
    daily_data = {}
    symbol_sector = {}
    for sector in SECTORS:
        page = get_content_sector_page(build_url(sector, 0, COUNT))
        how_many_symbols = get_how_many_symbols_in_sector(page)
        how_many_pages = calculate_how_many_pages(how_many_symbols)
        tbody = page.find_all("tbody")[0]
        build_sectors_and_daily_dict(tbody, sector, symbol_sector, daily_data)
        for offset in range(100, how_many_pages * COUNT, 100):
            page = get_content_sector_page(build_url(sector, offset, COUNT))
            tbody = page.find_all("tbody")[0]
            build_sectors_and_daily_dict(tbody, sector, symbol_sector, daily_data)
    return (symbol_sector,  daily_data)

def get_data_financial_statements(symbol, counter_symbols):
    now_titles = 0
    now_net_income = 0
    title_list = []
    data_dict = {}
    data_indicator = 0
    program_sleep(counter_symbols)
    print(symbol)
    current_url = f'https://finance.yahoo.com/quote/{symbol}/financials?p={symbol}'
    page = requests.get(current_url, headers = headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    all_span = soup.find_all("span")
    if len(all_span) < 100:
        print("less then",len(all_span))
    for i in all_span:
        current_text = i.text
        if current_text == "Total Revenue":
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
    if data_indicator ==1:
        return {symbol: data_dict}
    else:
        return {symbol: None}

def get_all_data_financial_statements(list_symbols):
    counter_symbols = 0
    all_symbols_dict = {}
    for symbol in list_symbols:
        if symbol not in all_symbols_dict:
            all_symbols_dict.update(get_data_financial_statements(symbol, counter_symbols))
        counter_symbols += 1
    return all_symbols_dict

tuple_dict = scrape_sector_pages()
list_symbols = list(tuple_dict[0].keys())
financial_statements = get_all_data_financial_statements(list_symbols)
print(financial_statements)
print(list_symbols)
print(tuple_dict[1])
