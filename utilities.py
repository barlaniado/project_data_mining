import time
import random
import math
import project_conf
import utilities

def program_sleep(counter=None):
    """
    The function sends the program to sleep so as not to overload the server.
    """
    if counter == utilities.PRAM_VALUE_SLEEP_NO_COUNTER:
        time.sleep(random.randint(utilities.MIN_TIME_SLEEP_NO_COUNTER,
                                  utilities.MAX_TIME_SLEEP_NO_COUNTER))
    else:
        if counter % utilities.WHEN_LONG_SLEEP ==  utilities.NO_REMAINDER:
            time.sleep(utilities.TIME_LONG_SLEEP)
        elif counter % (utilities.WHEN_MODERATE_SLEEP == utilities.NO_REMAINDER:
            time.sleep(utilities.TIME_MODERATE_SLEEP)
        else:
            time.sleep(random.randint(7, 12))


def get_how_many_symbols_in_sector(first_page):
    """
    the function retrieve the number of companies in each sector.
    """
    content = first_page.find("div", class_="Pos(r) Pos(r) Mih(265px)")
    return int(content.find("span", class_="Mstart(15px) Fw(500) Fz(s)").text.split(" ")[-2])


def calculate_how_many_pages(how_many_symbols):
    """
    The function receive the number of companies in a sector and calculate the number of pages.
    Each page contain 100 companies at most.
    """
    return math.ceil(how_many_symbols / project_conf.COUNT)


def build_url(sector, offset, count):
    """
    The function creates the wanted url.
    """
    url = f'https://finance.yahoo.com/screener/predefined/ms_{sector.lower().replace(" ", "_")}?offset={offset}&count={count}'
    return url


def build_url_financials_symbol(symbol):
    current_url = f'https://finance.yahoo.com/quote/{symbol}/financials?p={symbol}'
    return current_url
    
