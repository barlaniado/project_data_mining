import utilities
import requests_webpage
import requests
from bs4 import BeautifulSoup
import project_conf


def get_data_financial_statements(symbol, counter_symbols):
    now_titles = 0
    now_net_income = 0
    title_list = []
    data_dict = {}
    data_indicator = 0
    utilities.program_sleep(counter_symbols)
    print(symbol) # MAKE THIS PRING LOG
    soup = requests_webpage.get_content_financial_statements(symbol)
    all_span = soup.find_all(project_conf.TAG_DATA_FINANCIAL_STATEMENTS)
    for i in all_span:
        current_text = i.text
        if current_text == project_conf.TOTAL_REVENUE_TITLE:
            now_titles = 0
        if now_titles == 1:
            current_title = current_text
            title_list.append(current_title)
            data_dict[current_title] = {}
        elif now_net_income == 1:
            try:
                data_dict[title_list[counter]][project_conf.KEY_NET_INCOME] =\
                int(current_text.replace(project_conf.DELETE_FROM_NET_INCOME_STRING, project_conf.REPLACE_DELETED_CHAR_WITH))
            except ValueError:
                data_dict[title_list[counter]][project_conf.KEY_NET_INCOME] = project_conf.VALUE_IF_CANT_CAST_TO_INT
            counter += 1
            if counter == len(title_list):
                break
        if current_text == project_conf.NEXT_TO_COME_TITLES:
            now_titles = 1
        if current_text == project_conf.NEXT_TO_COME_DATA_NET_INCOME:
            data_indicator = 1
            now_net_income = 1
            counter = 0
    if data_indicator == 1:
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
