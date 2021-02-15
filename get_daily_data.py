import requests_webpages
from datetime import datetime
import project_conf
import utilities
import logger

the_logger = logger.define_logger()



def get_price(tr):
    """
    The function retrieve the daily price of a stock of a company.
    """
    data_list = tr.find_all('span', class_="Trsdu(0.3s)")
    price = data_list[0].text
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
    data_list = tr.find_all('span', class_="Trsdu(0.3s)")
    price_change = data_list[1].text
    return price_change


def get_price_change_percentage(tr):
    """
    The function retrieve the difference in percentage, between the last price of a stock from yesterday
    and the current price of that stock.
    """
    data_list = tr.find_all('span', class_="Trsdu(0.3s)")
    price_change_percentage = data_list[2].text
    return price_change_percentage


def get_volume(tr):
    """
    The function retrieve the volume of a company.
    """
    data_list = tr.find_all('span', class_="Trsdu(0.3s)")
    volume = data_list[3].text
    return volume


def get_avg_vol(tr):
    """
    The function retrieve the average volume of a company.
    """
    data_list = tr.find_all('td')
    for data in data_list:
        if data.attrs['aria-label'] == "Avg Vol (3 month)":
            avg_vol = data.text
            break # I put break because I need the first one.
    return avg_vol


def build_sectors_and_daily_dict(tbody, sector, symbol_sector_dict, daily_dict):
    """
    The function creates a dictionary that contain the daily data of the stocks
    of all the companies in a sector.
    """
    all_tr = tbody.find_all("tr")
    for tr in all_tr:
        current_symbol = get_symbol(tr)
        dateTimeObj = datetime.now()
        if current_symbol in symbol_sector_dict:
            symbol_sector_dict[current_symbol].append(sector)
        else:
            symbol_sector_dict[current_symbol] = [sector]
        if current_symbol not in daily_dict:
            daily_dict[current_symbol] = {"Time": dateTimeObj,
                                          "Price": get_price(tr),
                                          "Price change": get_price_change(tr),
                                          "Percentage":  get_price_change_percentage(tr),
                                          "Volume":  get_volume(tr),
                                          "Avg Vol (3 month)": get_avg_vol(tr)}
    the_logger.debug("The daily dictionary created successfully")
    return

def scrape_sector_pages():
    daily_data = {}
    symbol_sector = {}
    for sector in project_conf.SECTORS:
        page = requests_webpages.get_content_sector_page(utilities.build_url(sector, 0, project_conf.COUNT))
        how_many_symbols = utilities.get_how_many_symbols_in_sector(page)
        how_many_pages = utilities.calculate_how_many_pages(how_many_symbols)
        tbody = page.find_all("tbody")[0]
        build_sectors_and_daily_dict(tbody, sector, symbol_sector, daily_data)
        for offset in range(100, how_many_pages * project_conf.COUNT, 100):
            page = requests_webpages.get_content_sector_page(utilities.build_url(sector, offset, project_conf.COUNT))
            tbody = page.find_all("tbody")[0]
            build_sectors_and_daily_dict(tbody, sector, symbol_sector, daily_data)
    return (symbol_sector,  daily_data)
