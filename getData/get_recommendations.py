import requests
import json
from configuration import project_conf
from datetime import date


class StockRecommendation:
    """ StockRecommendation object holds all the recommendations for a specific symbol in a specific date"""
    def __init__(self, symbol):
        self.symbol = symbol
        self.querystring = {"symbol": symbol}
        self.data = self._get_data()

    def _get_data(self):
        """ Get the recommendations for the symbol using  Yahoo Finance API """
        how_many_headers = project_conf.HOW_MANY_HEADERS
        counter = 1
        while counter <= how_many_headers:
            response = requests.request("GET", project_conf.URL, headers=project_conf.LIST_OF_HEADERS[counter - 1],
                                        params=self.querystring)
            try:
                dict_data = json.loads(response.text)
            except json.decoder.JSONDecodeError:
                project_conf.logger.logger.warning(f"{self.symbol}: JSONDecodeError")


            if 'message' in dict_data.keys():
                project_conf.logger.logger.info(f"key{counter} has passed the monthly quota")
                counter += 1
            else:
                break
        if counter > how_many_headers:
            project_conf.logger.logger.error("No more keys- please add new key")
            quit()
        project_conf.logger.logger.debug(dict_data)
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
    """ Recommendations object holds a list of StockRecommendation"""
    def __init__(self, list_symbol):
        self.symbols = list_symbol
        self.dict_recommendations = {}
        self.add_to_dict()

    def add_to_dict(self):
        for s in self.symbols:
            self.dict_recommendations[s] = StockRecommendation(s)




