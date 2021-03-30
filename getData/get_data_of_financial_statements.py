from utilities import utilities
from getData import requests_webpages
from configuration import project_conf
import requests


class SymbolFinancialReportData:
    """ This class creates objects of the financial data of a specific symbol.
    Each object holds the financial data about specific symbol. """

    def __init__(self, symbol, fin_data):
        """ The constructor of this class gets a symbol and the financial data of the specific symbol """
        self.symbol = symbol
        self.net_income = fin_data

    def __str__(self):
        str_obj = f'Financial Reports - {self.symbol}:\n{self.net_income}'
        return str_obj


class FinancialReportsDataScraper:
    """ This class creates objects of the financial data scraper.
        Each object that is created holds list of SymbolFinancialReportData objects."""

    def __init__(self, symbol_to_scrape):
        """ The constructor of this class gets symbols to scrape """
        self.counter_symbols = 0
        self.data_list = []
        self._get_all_data_financial_statements(symbol_to_scrape)

    def __len__(self):
        """ Define the length of the object """
        return len(self.data_list)

    def __str__(self):
        return self.data_list

    def _get_data_financial_statements(self, symbol):
        """
        The method gets the symbol of a company, retrieve the financial data about that company,
        creates a SymbolFinancialReportData object and append this object to self.data_list.
        """
        now_titles = 0
        now_net_income = 0
        title_list = []
        data_dict = {}
        data_indicator = 0
        utilities.program_sleep(self.counter_symbols)
        try:
            soup = requests_webpages.get_content_financial_statements(symbol)
        except requests.exceptions.ConnectionError:
            project_conf.logger.logger.warning(f"Could not get {symbol}'s financial statements - ConnectionError")
            self.data_list.append(SymbolFinancialReportData(symbol, None))
            return
        except requests.exceptions.HTTPError:
            project_conf.logger.logger.warning(f"Could not get {symbol}'s financial statements - HTTPError")
            self.data_list.append(SymbolFinancialReportData(symbol, None))
            return
        all_span = soup.find_all(project_conf.TAG_DATA_FINANCIAL_STATEMENTS)
        for i in all_span:
            current_text = i.text
            if current_text == project_conf.TOTAL_REVENUE_TITLE:
                now_titles = 0
            if now_titles == 1:
                current_title = current_text
                if current_title != 'ttm':
                    title_list.append(current_title)
                    data_dict[current_title] = {}
            elif now_net_income == 1:
                try:
                    data_dict[title_list[counter]][project_conf.KEY_NET_INCOME] = \
                        int(current_text.replace(project_conf.DELETE_FROM_NET_INCOME_STRING,
                                                 project_conf.REPLACE_DELETED_CHAR_WITH))
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
            project_conf.logger.logger.info(project_conf.DATA_FINANICIALS_ADDED + symbol)
            project_conf.logger.logger.debug(data_dict)
            self.data_list.append(SymbolFinancialReportData(symbol, data_dict))
        else:
            project_conf.logger.logger.warning(project_conf.NO_DATA_MESSAGE_LOGGER + symbol)
            self.data_list.append(SymbolFinancialReportData(symbol, None))

    def _get_all_data_financial_statements(self, list_symbols):
        """
        The method gets a list of all the companies symbols
         abd iterates over the list while calling _get_data_financial_statements(symbol) for each symbol.
        """
        for symbol in list_symbols[0:2]:
            self._get_data_financial_statements(symbol)
            self._update_counter_symbols() # The programs should sleep sometimes
    
    def _update_counter_symbols(self):
        """ This method updates the symbol counter in order to tell the sleeping function how much time
        the program should sleep now"""
        self.counter_symbols += 1
