import utilities
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
    print(symbol)
    current_url = f'https://finance.yahoo.com/quote/{symbol}/financials?p={symbol}'
    page = requests.get(current_url, headers=project_conf.headers)
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