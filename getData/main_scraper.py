from getData import get_daily_data as get_d
from getData import get_data_of_financial_statements as get_f
import pymysql.cursors
from configuration import project_conf


class MainScraperSymbols:
    def __init__(self, sector_to_scrape):
        self.daily_data = None
        self.financial_report = None
        self.connection = None
        self.cur = None
        self._connect_db(project_conf.HOST,
                         project_conf.USER, project_conf.PASSWORD, project_conf.DB, project_conf.CHARSET)
        self._get_daily_data(sector_to_scrape)
        self._get_financial(self.daily_data.get_list_of_symbols())
        self._add_new_sectors_and_daily()

    def _get_daily_data(self, sector_to_scrape):
        self.daily_data = get_d.DailyDataScraper(sector_to_scrape)

    def _get_financial(self, symbols):
        self.financial_report = get_f.FinancialReportsDataScraper(symbols)

    def _connect_db(self, host, user, password, db, charset):
        # Connect to the database
        self.connection = pymysql.connect(host=host,
                                          user=user,
                                          password=password,
                                          db=db,
                                          charset=charset,
                                          cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.connection.cursor()

    def _add_new_sectors_and_daily(self):
        list_to_iterate = self.daily_data.daily_data
        for daily_stock in list_to_iterate:
            self._check_if_sector_exist_and_add(daily_stock)
            self._check_if_symbol_exist_and_add(daily_stock)
            self._insert_daily_data(daily_stock)

    def _insert_daily_data(self, daily_stock):
        self.cur.execute(project_conf.INSERT_DAILY_DATA.format(project_conf.DAILY_DATA_TABLE,
                                                               project_conf.COLUMNS_INSERT_DAILY_DATA,
                                                               daily_stock.symbol, daily_stock.time_scraped,
                                                               daily_stock.price, daily_stock.price_change,
                                                               daily_stock.change_percentage,
                                                               daily_stock.volume, daily_stock.average_volume))
        self.connection.commit()

    def _check_if_sector_exist_and_add(self, current_symbol_daily):
        self.cur.execute(project_conf.SELECT_SECTOR.format(project_conf.SECTORS_TABLE,
                                                           current_symbol_daily.sector))
        sector_exist = len(self.cur.fetchall())
        if sector_exist == 0:
            # add the new sector to sectors table
            self.cur.execute(project_conf.INSERT_SECTOR.format(project_conf.SECTORS_TABLE, current_symbol_daily.sector))
            self.connection.commit()

    def _check_if_symbol_exist_and_add(self, current_symbol_daily):
        self.cur.execute(project_conf.SELECT_SYMBOL_SECTOR.format(project_conf.SYMBOLS_SECTORS_TABLE,
                                                                  current_symbol_daily.symbol))
        result = self.cur.fetchall()
        symbol_exist = len(result)
        if symbol_exist > 0:
            assert symbol_exist == 1
            if self.check_id_of_sector(current_symbol_daily.sector) != result[0].get('id_sector'):
                self.cur.execute(project_conf.CHANGE_SECTOR_TO_EXIST_SYMBOL.format(project_conf.SYMBOLS_SECTORS_TABLE,
                                                                                   self.check_id_of_sector(
                                                                                       current_symbol_daily.sector),
                                                                                   current_symbol_daily.symbol))
                self.connection.commit()
        else:
            self.cur.execute(project_conf.INSERT_NEW_SYMBOL_SECTOR.format
                             (project_conf.SYMBOLS_SECTORS_TABLE,
                              project_conf.COLUMNS_INSERT_NEW_SYMBOL_SECTOR,
                              current_symbol_daily.symbol,
                              self.check_id_of_sector(current_symbol_daily.sector)))
            self.connection.commit()

    def check_id_of_sector(self, sector):
        self.cur.execute(project_conf.ID_OF_SECTOR_QUERY.format(project_conf.SECTORS_TABLE, sector))
        result = self.cur.fetchall()
        assert len(result) == 1
        return result[0].get('id_sector')
