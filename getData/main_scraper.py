from getData import get_daily_data as get_d
from getData import get_data_of_financial_statements as get_f
class MainScraperSymbols:
    def __init__(self, sector_to_scrape):
        self.daily_data = None
        self.financial_report = None
        self._get_daily_data(sector_to_scrape)
        self._get_financial(self.daily_data.get_list_of_symbols())

    def _get_daily_data(self, sector_to_scrape):
        self.daily_data = get_d.DailyDataScraper(sector_to_scrape)

    def _get_financial(self, symbols):
        self.financial_report = get_f.FinancialReportsDataScraper(symbols)