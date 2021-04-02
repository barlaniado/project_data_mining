from getData import get_daily_data as get_d
from getData import get_data_of_financial_statements as get_f
import pymysql.cursors
from configuration import project_conf
import datetime


class MainScraperSymbols:
    """ This class creates objects of the main scraper.
    Each object that is created holds: DailyDataScraper object and FinancialReportsDataScraper object.
    The data is added directly into the DB.
    Please update the configurations file to allow proper connection to DB."""

    def __init__(self, sector_to_scrape, financials):
        """ The constructor of this class gets sector to scrape and
         a boolean parameter (financial) that indicate whether to scrape the financials data also """

        # Initialize class attributes
        self.daily_data = None  # Will be a DailyDataScraper object
        self.financial_report = None  # Will be a FinancialReportsDataScraper object
        self.connection = None  # Will be a connection object
        self.cur = None  # Will be a cursor object
        self._connect_db(project_conf.HOST,
                         project_conf.USER, project_conf.PASSWORD, project_conf.DB, project_conf.CHARSET)
        self._get_daily_data(sector_to_scrape)  # build the DailyDataScraper object of the daily_data attribute
        if financials:
            # build the FinancialReportsDataScraper object of the d financial_report attribute
            self._get_financial(self.daily_data.get_list_of_symbols())
        self._add_all_scraped_date(financials)

    def _get_daily_data(self, sector_to_scrape):
        """ Create a DailyDataScraper object.
        The method changes change self.daily_data inplace """
        self.daily_data = get_d.DailyDataScraper(sector_to_scrape)

    def _get_financial(self, symbols):
        """ Create a FinancialReportsDataScraper object.
        The method changes self.financial_report inplace"""
        self.financial_report = get_f.FinancialReportsDataScraper(symbols)

    def _connect_db(self, host, user, password, db, charset):
        """ Connect to the database """
        try:
            self.connection = pymysql.connect(host=host,
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset=charset,
                                              cursorclass=pymysql.cursors.DictCursor)
        except (RuntimeError, pymysql.err.OperationalError):
            project_conf.logger.logger.error(project_conf.CONNECTION_DB_ERROR)
            quit()
        self.cur = self.connection.cursor()

    def _add_all_scraped_date(self, financials):
        """ Add the data to the DB """
        project_conf.logger.logger.info(project_conf.INSERT_DATA_TO_DB_MESSAGE)
        self._add_new_sectors_and_daily()
        if financials:
            project_conf.logger.logger.info(project_conf.INSERT_FINANCIAL_DATA_TO_DB_MESSAGE)
            self._insert_financial_data()

    def _add_new_sectors_and_daily(self):
        """ Add only sectors, symbols and daily data (This function is called by _add_all_scraped_date) """
        for daily_stock in self.daily_data.daily_data:
            self._check_if_sector_exists_and_add(daily_stock)  # add to sectors table
            self._check_if_symbol_exists_and_add(daily_stock)  # add to symbol_sector table
            self._insert_daily_data(daily_stock)  # add to daily_data table

    def _check_if_sector_exists_and_add(self, current_symbol_daily):
        """ Check if specific sector exists in the sectors table and add it if not"""
        query = project_conf.SELECT_SECTOR.format(project_conf.SECTORS_TABLE,
                                                  current_symbol_daily.sector)
        project_conf.logger.logger.debug(project_conf.CHECK_IF_SECTOR_EXISTS_LOG.format(current_symbol_daily.sector,
                                                                                        current_symbol_daily.symbol))
        project_conf.logger.logger.debug(query)
        self.cur.execute(query)
        sector_exist = len(self.cur.fetchall())
        if sector_exist == 0:
            # add the new sector to sectors table
            query = project_conf.INSERT_SECTOR.format(project_conf.SECTORS_TABLE, current_symbol_daily.sector)
            project_conf.logger.logger.info(project_conf.INSERT_NEW_SECTOR.format(current_symbol_daily.sector))
            project_conf.logger.logger.info(project_conf.ADD_NEW_SECTOR.format(current_symbol_daily.sector,
                                                                               project_conf.SECTORS_TABLE))
            project_conf.logger.logger.debug(query)
            self.cur.execute(query)
            self.connection.commit()

    def _check_if_symbol_exists_and_add(self, current_symbol_daily):
        """ check if a symbol exists in the symbol_sector table, if not add it.
        If the sector already exists check if its sector needs to be updated"""

        query = project_conf.SELECT_SYMBOL_SECTOR.format(project_conf.SYMBOLS_SECTORS_TABLE,
                                                         current_symbol_daily.symbol)
        self.cur.execute(query)
        result = self.cur.fetchall()
        symbol_exist = len(result)
        if symbol_exist > 0:  # Only if the sector already exists
            assert symbol_exist == 1
            # Now the function checks if the sector of the symbol has changed, maybe the sector needs to be updated
            if self.check_id_of_sector(current_symbol_daily.sector) != result[0].get('id_sector'):
                query = project_conf.CHANGE_SECTOR_TO_EXIST_SYMBOL.format(project_conf.SYMBOLS_SECTORS_TABLE,
                                                                          self.check_id_of_sector(
                                                                              current_symbol_daily.sector),
                                                                          current_symbol_daily.symbol)
                project_conf.logger.logger.info(project_conf.UPDATE_SECTOR(project_conf.SECTORS_TABLE))
                project_conf.logger.logger.debug(query)
                self.cur.execute(query)
                self.connection.commit()
        else:
            query = project_conf.INSERT_NEW_SYMBOL_SECTOR.format(project_conf.SYMBOLS_SECTORS_TABLE,
                                                                 project_conf.COLUMNS_INSERT_NEW_SYMBOL_SECTOR,
                                                                 current_symbol_daily.symbol,
                                                                 self.check_id_of_sector(current_symbol_daily.sector))
            project_conf.logger.logger.info(project_conf.NEW_SYMBOL_MESSAGE.format(current_symbol_daily.symbol))
            project_conf.logger.logger.debug(query)
            self.cur.execute(query)
            self.connection.commit()

    def check_id_of_sector(self, sector):
        """ The function gets a sector and returns its id_sector from the sectors table.
        If the sector does not exist in the sectors table returns None """
        self.cur.execute(project_conf.ID_OF_SECTOR_QUERY.format(project_conf.SECTORS_TABLE, sector))
        result = self.cur.fetchall()
        the_len_of_the_result = len(result)
        if the_len_of_the_result > 0:
            try:
                assert the_len_of_the_result == 1
            except AssertionError:
                project_conf.logger.logger.warning(project_conf.DUPLICATE_SECTOR.format(sector))
            return result[0].get('id_sector')
        else:
            project_conf.logger.logger.info(project_conf.CHECK_ID_SECTOR_NOT_EXISTS(sector))
            return None

    def _insert_daily_data(self, daily_stock):
        """ Insert the daily data into the db """
        query = project_conf.INSERT_DAILY_DATA.format(project_conf.DAILY_DATA_TABLE,
                                                      project_conf.COLUMNS_INSERT_DAILY_DATA,
                                                      daily_stock.symbol, daily_stock.time_scraped,
                                                      daily_stock.price, daily_stock.price_change,
                                                      daily_stock.change_percentage,
                                                      daily_stock.volume, daily_stock.average_volume)
        project_conf.logger.logger.debug(project_conf.INSERT_SYMBOL_DAILY_DATA.format(daily_stock.symbol))
        project_conf.logger.logger.debug(query)
        self.cur.execute(query)
        self.connection.commit()

    def _insert_financial_data(self):
        """ Insert the financial data to the db """
        for symbol_data in self.financial_report.data_list:
            if symbol_data.net_income:
                for date, net_income in symbol_data.net_income.items():
                    query = project_conf.INSERT_FINANCIAL_DATA.format(project_conf.FINANCIAL_DATA_TABLE,
                                                                      project_conf.COLUMNS_INSERT_FINANCIAL_DATA,
                                                                      symbol_data.symbol,
                                                                      datetime.datetime.strptime(date,
                                                                                     project_conf.FORMAT_DATE_FINANCIAL),
                                                                      net_income['Net Income'])
                    project_conf.logger.logger.debug(project_conf.INSERT_SYMBOL_FINANCIAL_DATA .format(symbol_data.symbol))
                    self.cur.execute(query)
                    self.connection.commit()
