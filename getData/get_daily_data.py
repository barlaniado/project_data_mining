from getData import requests_webpages
from datetime import datetime
from configuration import project_conf
from utilities import utilities
import requests


class SecurityDailyLevel:
    def __init__(self, symbol, time_scraped, sector, price, price_change, change_percentage, volume, average_volume):
        self.symbol = symbol
        self.time = time_scraped
        self.sector = sector
        self.price = price
        self.price_change = price_change
        self.change_percentage = change_percentage
        self.volume = volume
        self.average_volume = average_volume

    def __str__(self):
        str_representation = f'Daily data for {self.symbol} on {self.time}:\n'\
        f'Price: {self.price}\nPrice change: {self.price_change}\nChange in percentages: {self.change_percentage}\nVolume: {self.volume}\nAverage volume: {self.average_volume}'
        return str_representation


class DailyDataScraper:
    def __init__(self, sector_to_scrape):
        self.date = str(datetime.now())
        self.how_many_symbols = 0
        self.daily_data = []
        self._scrape_sector_pages(sector_to_scrape)
        self._update_how_many_symbols()

    def get_list_of_symbols(self):
        return [sym.symbol for sym in self.daily_data]

    def _scrape_sector_pages(self, sector_to_scrape):
        """
        The function iterates over a list of sector and create a list of symbols and a dictionary:
        1) "symbol_list" contain the stock symbols
        2) "daily_dict" contain the daily data of the stocks.
        The function returns tuple of these two (symbol_list, daily_data)
        """
        project_conf.logger.logger.info(project_conf.START_SCRAPE_SECTOR_MESSAGE)
        for sector in sector_to_scrape:
            try:
                page = requests_webpages.get_content_sector_page \
                    (utilities.build_url(sector, project_conf.OFFSET_OF_FIRST_PAGE_SECTOR, project_conf.COUNT))
            except requests.exceptions.ConnectionError:
                project_conf.logger.logger.warning(
                    f" ConnectionError occured while trying to scrape the first page of {sector}, therefore all companies in the {sector} sector will not be scraped.")
                continue
            except requests.exceptions.HTTPError:
                project_conf.logger.logger.warning(
                    f" HTTPError occured while trying to scrape the first page of {sector}, therefore all companies in the {sector} sector will not be scraped.")
                continue
            how_many_symbols = utilities.get_how_many_symbols_in_sector(page)
            how_many_pages = utilities.calculate_how_many_pages(how_many_symbols)
            project_conf.logger.logger.info(utilities.build_message_how_many_symbols_pages_for_logger
                                            (sector, how_many_symbols, how_many_pages))
            tbody = page.find_all(project_conf.TAG_TABLE_IN_PAGE)
            if len(tbody) > project_conf.ASSUMPTION_TBODY_LEN:
                project_conf.logger.logger.warning(project_conf.LOGGER_WARNING_MESSAGE_TBODY_MORE_THAN)
            if len(tbody) < project_conf.ASSUMPTION_TBODY_LEN:
                project_conf.logger.logger.warning(project_conf.LOGGER_WARNING_MESSAGE_TBODY_LESS_THAN)
            tbody = tbody[project_conf.TABLE_CONTENT_INDEX]
            self._add_securities(tbody, sector)
            for offset in range(project_conf.HOW_MANY_SYMBOLS_EACH_PAGE, how_many_pages * project_conf.COUNT,
                                project_conf.HOW_MANY_SYMBOLS_EACH_PAGE):
                try:
                    page = requests_webpages.get_content_sector_page(
                        utilities.build_url(sector, offset, project_conf.COUNT))
                except requests.exceptions.ConnectionError:
                    project_conf.logger.logger.warning(
                        f" ConnectionError occured while trying to scrape the a page of {sector} (which is not the first page of that sector), therefore the companies in this page will not be scraped.")
                    continue
                except requests.exceptions.HTTPError:
                    project_conf.logger.logger.warning(
                        f" HTTPError occured while trying to scrape the first page of {sector}, therefore all companies in the {sector} sector will not be scraped.")
                    continue
                tbody = page.find_all(project_conf.TAG_TABLE_IN_PAGE)
                if len(tbody) > project_conf.ASSUMPTION_TBODY_LEN:
                    project_conf.logger.logger.warning(project_conf.LOGGER_WARNING_MESSAGE_TBODY_MORE_THAN)
                if len(tbody) < project_conf.ASSUMPTION_TBODY_LEN:
                    project_conf.logger.logger.warning(project_conf.LOGGER_WARNING_MESSAGE_TBODY_LESS_THGE)
                tbody = tbody[project_conf.TABLE_CONTENT_INDEX]
                self._add_securities(tbody, sector)
                project_conf.logger.logger.info(project_conf.FINISH_SECTOR_SCRAPING_MESSAGE)
                project_conf.logger.logger.info(project_conf.LEN_OF_DICT_DAILY_LOGGER_MESSAGE + str(len(self.daily_data)))

    def _add_securities(self, tbody, sector):
        """
        The function gets content of a table in specific sector page (tbody), and the sector itself (sector)
        and adding more data from the current sector page to the two dictionaries (symbol_sector_dict, daily_dict).
        tbody is the data retrieved from page which was created from beautiful-soap in the function _scrape_sector_pages,
        it is an object of the class 'bs4.element.Tag'.
        In addition, the function gets two dictionaries
        1) Contain the stock symbols and their sectors (symbol_sector_dict)
        2) Contain the daily data of the stocks (daily_dict)
        """
        all_tr = tbody.find_all(project_conf.FIND_LINE_TAG)
        if not all_tr:
            project_conf.logger.logger.warning(project_conf.DATA_LIST_EMPTY)
        for tr in all_tr:
            current_symbol = DailyDataScraper._get_symbol(tr)
            project_conf.logger.logger.info(project_conf.NOW_SYMBOLS_MESSAGE_LOGGER + current_symbol)
            date_time_obj = str(datetime.now())
            if current_symbol not in self.daily_data:
                current_object = SecurityDailyLevel(current_symbol, date_time_obj, sector,  DailyDataScraper._get_price(tr),
                                                    DailyDataScraper._get_price_change(tr), DailyDataScraper._get_symbol_percentage(tr), DailyDataScraper._get_volume(tr),  DailyDataScraper._get_avg_vol(tr))
                self.daily_data.append(current_object)
                project_conf.logger.logger.debug(str(current_object))
                project_conf.logger.logger.info(project_conf.LOGGER_MESSAGE_BUILD_DAILY_SECTOR_DICT)
            else:
                project_conf.logger.logger.info(current_symbol + project_conf.SYMBOL_EXISTS_LOGGER_MESSAGE)

    def _update_how_many_symbols(self):
        self.how_many_symbols = len(self.daily_data)

    def  __str__(self):
        return f'The object contains data about {self.how_many_symbols} symbols'

    @staticmethod
    def _get_price(tr):
        """
        The function retrieve the daily price of a stock of a company.
        """
        data_list = tr.find_all(project_conf.TAG_TO_RETRIEVE_DAILY_DATA, class_=project_conf.CLASS_GET_DAILY_DATA)
        if not data_list:
            project_conf.logger.logger.warning(project_conf.DATA_LIST_EMPTY)
        try:
            price = data_list[project_conf.PRICE_INDEX].text
        except IndexError:
            return None
        try:
            price = price.replace(",", "")
            price = float(price)
            if price < 0:
                raise ValueError  # price can not be less than 0
        except ValueError:
            project_conf.logger.logger.error(project_conf.INVALID_PRICE_LOG_MESSAGE)
            return None
        return price

    @staticmethod
    def _get_symbol(tr):
        """
        The function retrieve the symbol of a company.
        """
        data_list = tr.find_all("a")
        if not data_list:
            project_conf.logger.logger.warning(project_conf.DATA_LIST_EMPTY)
        try:
            symbol = data_list[0].text
        except IndexError:
            return None
        return symbol

    @staticmethod
    def _get_price_change(tr):
        """
        The function retrieve the difference between the last price of a stock from yesterday
        and the current price of that stock.
        """
        data_list = tr.find_all(project_conf.TAG_TO_RETRIEVE_DAILY_DATA, class_=project_conf.CLASS_GET_DAILY_DATA)
        if not data_list:
            project_conf.logger.logger.warning(project_conf.DATA_LIST_EMPTY)
        try:
            price_change = data_list[project_conf.PRICE_CHANGE_INDEX].text
        except IndexError:
            return None
        try:
            price_change = price_change.replace(",", "")
            price_change = float(price_change)
        except ValueError:
            project_conf.logger.logger.error(project_conf.INVALID_PRICE_CHANGE_LOG_MESSAGE)
            return None
        return price_change

    @staticmethod
    def _get_symbol_percentage(tr):
        """
        The function retrieve the difference in percentage, between the last price of a stock from yesterday
        and the current price of that stock.
        """
        data_list = tr.find_all(project_conf.TAG_TO_RETRIEVE_DAILY_DATA, class_=project_conf.CLASS_GET_DAILY_DATA)
        if not data_list:
            project_conf.logger.logger.warning(project_conf.DATA_LIST_EMPTY)
        try:
            price_change_percentage = data_list[project_conf.PRICE_CHANGE_PERCENTAGE].text
        except IndexError:
            return None
        try:
            if price_change_percentage[project_conf.INDEX_PERCENTAGE_IN_TEXT] != project_conf.PERCENTAGE_SIGN:
                raise ValueError
            price_change_percentage = price_change_percentage.replace(",", "")
            price_change_percentage = float(price_change_percentage.replace(project_conf.PERCENTAGE_SIGN, "",
                                                                            project_conf.HOW_MANY_REPLACE_PERCENTAGE_ALLOWED))
        except ValueError:
            project_conf.logger.logger.error(project_conf.INVALID_PRICE_CHANGE_PERCETAGE_LOG_MESSAGE)
            return None
        return price_change_percentage

    @staticmethod
    def _get_volume(tr):
        """
        The function retrieve the volume of a company.
        """
        data_list = tr.find_all(project_conf.TAG_TO_RETRIEVE_DAILY_DATA, class_=project_conf.CLASS_GET_DAILY_DATA)
        if not data_list:
            project_conf.logger.logger.warning(project_conf.DATA_LIST_EMPTY)
        try:
            volume = data_list[project_conf.VOLUME_CURRENT_DAY].text
        except IndexError:
            return None
        return volume

    @staticmethod
    def _get_avg_vol(tr):
        """
        The function retrieve the average volume of a company.
        """
        data_list = tr.find_all(project_conf.FIND_AVG_VOL)
        if not data_list:
            project_conf.logger.logger.warning(project_conf.DATA_LIST_EMPTY)
        for data in data_list:
            if data.attrs[project_conf.ATTRS_AVG_VOL] == project_conf.TITLE_AVG_VOL:
                avg_vol = data.text
                break  # I put break because I need the first one.
        return avg_vol

