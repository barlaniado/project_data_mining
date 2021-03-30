from getData import requests_webpages
from datetime import datetime
from configuration import project_conf
from utilities import utilities
import requests


class SecurityDailyLevel:
    """ This class creates objects of daily data of a specific symbol.
    Each object holds daily data about specific symbol. """

    def __init__(self, symbol, time_scraped, sector, price, price_change, change_percentage, volume, average_volume):
        """ The constructor of this class gets all the daily data of the specific symbol """
        self.symbol = symbol
        self.time_scraped = time_scraped
        self.sector = sector
        self.price = price
        self.price_change = price_change
        self.change_percentage = change_percentage
        self.volume = volume
        self.average_volume = average_volume

    def __str__(self):
        str_representation = f'Daily data for {self.symbol} on {self.time_scraped}:' \
                             f'\nPrice: {self.price}\n' \
                             f'Price change: {self.price_change}\n' \
                             f'' \
                             f'Change in percentages: {self.change_percentage}\n' \
                             f'Volume: {self.volume}\nAverage volume: {self.average_volume}'
        return str_representation


class DailyDataScraper:
    """ This class creates objects of the daily data scraper.
        Each object that is created holds list of SecurityDailyLevel objects."""

    def __init__(self, sector_to_scrape):
        """ The constructor of this class gets sector to scrape """
        self.date = datetime.now()
        self.daily_data = []
        self._scrape_sector_pages(sector_to_scrape)

    def get_list_of_symbols(self):
        """ get a list of symbols that were scrapped """
        return [sym.symbol for sym in self.daily_data]

    def _scrape_sector_pages(self, sector_to_scrape):
        """
        The method iterates over a list of sectors, and call _add_securities(tbody, sector) method for each symbol
        in each sector.
        """
        project_conf.logger.logger.info(project_conf.START_SCRAPE_SECTOR_MESSAGE)
        for sector in sector_to_scrape:
            try:
                page = requests_webpages.get_content_sector_page \
                    (utilities.build_url(sector, project_conf.OFFSET_OF_FIRST_PAGE_SECTOR, project_conf.COUNT))
            except requests.exceptions.ConnectionError:
                project_conf.logger.logger.warning(
                    f" ConnectionError occured while trying to scrape the first page of {sector},"
                    f" therefore all companies in the {sector} sector will not be scraped.")
                continue
            except requests.exceptions.HTTPError:
                project_conf.logger.logger.warning(
                    f" HTTPError occured while trying to scrape the first page of {sector},"
                    f" therefore all companies in the {sector} sector will not be scraped.")
                continue
            how_many_symbols = utilities.get_how_many_symbols_in_sector(page)
            # For each sector the program needs to know how many page to scrape
            how_many_pages = utilities.calculate_how_many_pages(how_many_symbols)
            project_conf.logger.logger.info(utilities.build_message_how_many_symbols_pages_for_logger
                                            (sector, how_many_symbols, how_many_pages))
            tbody = page.find_all(project_conf.TAG_TABLE_IN_PAGE)
            if len(tbody) > project_conf.ASSUMPTION_TBODY_LEN:
                project_conf.logger.logger.warning(project_conf.LOGGER_WARNING_MESSAGE_TBODY_MORE_THAN)
            if len(tbody) < project_conf.ASSUMPTION_TBODY_LEN:
                project_conf.logger.logger.warning(project_conf.LOGGER_WARNING_MESSAGE_TBODY_LESS_THAN)
            tbody = tbody[project_conf.TABLE_CONTENT_INDEX]
            # The first call to the _add_securities(tbody, sector) function
            # for each sector (the first page for each sector) is performed outside the loop,
            # all others calls are performed in a loop.
            self._add_securities(tbody, sector)
            # Iterate over the pages of the current sector
            for offset in range(project_conf.HOW_MANY_SYMBOLS_EACH_PAGE, how_many_pages * project_conf.COUNT,
                                project_conf.HOW_MANY_SYMBOLS_EACH_PAGE):
                try:
                    page = requests_webpages.get_content_sector_page(
                        utilities.build_url(sector, offset, project_conf.COUNT))
                except requests.exceptions.ConnectionError:
                    project_conf.logger.logger.warning(
                        f" ConnectionError occured while trying to scrape the a page of {sector}"
                        f" (which is not the first page of that sector),"
                        f" therefore the companies in this page will not be scraped.")
                    continue
                except requests.exceptions.HTTPError:
                    project_conf.logger.logger.warning(
                        f" HTTPError occured while trying to scrape the first page of {sector},"
                        f" therefore all companies in the {sector} sector will not be scraped.")
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
        The method gets content of a table in specific sector page (tbody), and the sector itself (sector)
        and creates a SecurityDailyLevel objects for each symbol in the current page.
        The method append each new object to the daily_data attribute inplace.
        """

        all_tr = tbody.find_all(project_conf.FIND_LINE_TAG)
        if not all_tr:
            project_conf.logger.logger.warning(project_conf.DATA_LIST_EMPTY)
        for tr in all_tr:
            current_symbol = DailyDataScraper._get_symbol(tr)
            project_conf.logger.logger.info(project_conf.NOW_SYMBOLS_MESSAGE_LOGGER + current_symbol)
            date_time_obj = datetime.now()
            if current_symbol not in self.daily_data:
                current_object = SecurityDailyLevel(current_symbol, date_time_obj, sector,
                                                    DailyDataScraper._get_price(tr),
                                                    DailyDataScraper._get_price_change(tr),
                                                    DailyDataScraper._get_symbol_percentage(tr),
                                                    DailyDataScraper._get_volume(tr),
                                                    DailyDataScraper._get_avg_vol(tr))
                self.daily_data.append(current_object)
                project_conf.logger.logger.debug(str(current_object))
                project_conf.logger.logger.info(project_conf.LOGGER_MESSAGE_BUILD_DAILY_SECTOR_DICT)
            else:
                project_conf.logger.logger.info(current_symbol + project_conf.SYMBOL_EXISTS_LOGGER_MESSAGE)

    def __str__(self):
        """ The method defines the print of the object """
        return f'The object contains data about {self.how_many_symbols} symbols'

    @staticmethod
    def _get_price(tr):
        """
        The method retrieve the daily price of a specific symbol.
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
        The method retrieve the symbol of a company.
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
        The method retrieve the difference between the last price of a stock from yesterday
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
        The method retrieve the difference in percentage, between the last price of a stock from yesterday
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
        The method retrieve the volume of a company.
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
        The method retrieve the average volume of a company.
        """
        data_list = tr.find_all(project_conf.FIND_AVG_VOL)
        if not data_list:
            project_conf.logger.logger.warning(project_conf.DATA_LIST_EMPTY)
        for data in data_list:
            if data.attrs[project_conf.ATTRS_AVG_VOL] == project_conf.TITLE_AVG_VOL:
                avg_vol = data.text
                break
        return avg_vol

