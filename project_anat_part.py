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


def get_price():
    url = "https://finance.yahoo.com/screener/predefined/ms_technology?offset=0&count=100"
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    data = soup.find('tbody')
    data_list = data.find_all('span', class_="Trsdu(0.3s)")
    price = data_list[0].text
    print(price)
    return(price)


def get_price_change():
    url = "https://finance.yahoo.com/screener/predefined/ms_technology?offset=0&count=100"
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    data = soup.find('tbody')
    data_list = data.find_all('span', class_="Trsdu(0.3s)")
    price_change = data_list[1].text
    print(price_change)
    return(price_change)


def get_price_change_percentage():
    url = "https://finance.yahoo.com/screener/predefined/ms_technology?offset=0&count=100"
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    data = soup.find('tbody')
    data_list = data.find_all('span', class_="Trsdu(0.3s)")
    price_change_percentage = data_list[2].text
    print(price_change_percentage)
    return(price_change_percentage)


def get_volume_1():
    url = "https://finance.yahoo.com/screener/predefined/ms_technology?offset=0&count=100"
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    data = soup.find('tbody')
    data_list = data.find_all('span', class_="Trsdu(0.3s)")
    volume = data_list[3].text
    print(volume)
    return(volume)


def get_volume_2():
    url = "https://finance.yahoo.com/screener/predefined/ms_technology?offset=0&count=100"
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    data_list = soup.find_all('td', class_="Va(m) Ta(end) Pstart(20px) Fz(s)")
    for data in data_list:
        if data.attrs['aria-label'] == "Volume":
            volume = data.text
            break # I put break because I need the first one.
    print(volume)
    return(volume)


def get_avg_vol():
    url = "https://finance.yahoo.com/screener/predefined/ms_technology?offset=0&count=100"
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'lxml')
    data_list = soup.find_all('td', class_="Va(m) Ta(end) Pstart(20px) Fz(s)")
    for data in data_list:
        if data.attrs['aria-label'] == "Avg Vol (3 month)":
            avg_vol = data.text
            break # I put break because I need the first one.
    print(avg_vol)
    return(avg_vol)


get_price()
get_price_change()
get_price_change_percentage()
get_volume_1()
get_volume_2()
get_avg_vol()


"""
def get_price_change_percentage(price, price_change):
    price = float(price)
    price_change = float(price_change)
    price_change_percentage = round(100 * price_change/ (price - price_change), 2)
    if price_change_percentage > 0:
        price_change_percentage_str = f"+{price_change_percentage}%"
    else:
        price_change_percentage_str = f"{price_change_percentage}%"
    print(price_change_percentage_str)
    return price_change_percentage_str
"""