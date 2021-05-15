import requests
import json
from configuration import project_conf
from datetime import date


class StockRecommendation:
    def __init__(self, symbol):
        self.symbol = symbol
        self.querystring = {"symbol": symbol}
        self.data = self._get_data()


    def _get_data(self):
        response = requests.request("GET", project_conf.URL, headers=project_conf.HEADERS, params=self.querystring)
        dict_data = json.loads(response.text)
        self.date_recommendation = StockRecommendation.get_current_date()
        try:
            data = dict_data['recommendationTrend']['trend'][0]
        except KeyError:
            project_conf.logger.logger.warning(f"There are no recommendations for {self.symbol}")
            return None
        try:
            assert data['period'] == '0m'
            data.pop('period')
        except AssertionError:
            project_conf.logger.logger.warning(f"There are no current recommendations for {self.symbol}")
            return None
        else:
            project_conf.logger.logger.info(f"Got commendations for {self.symbol}")
            return data

    @staticmethod
    def get_current_date():
        return date.today()


class Recommendations:
    def __init__(self, list_symbol):
        self.symbols = list_symbol
        self.dict_recommendations = {}
        self.add_to_dict()

    def add_to_dict(self):
        for s in self.symbols:
            self.dict_recommendations[s] = StockRecommendation(s)




