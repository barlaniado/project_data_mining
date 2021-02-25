import json


with open('./DataForTests/financials_statements_for_tests.json') as data:
    financial_data = json.load(data)


def test_get_data_financial_statements():
    # Basic Materials
    assert financial_data['RIO']['12/31/2020']['Net Income'] == 9769000
    # Communication Services
    assert financial_data['DIS']['9/30/2017']['Net Income'] == 8980000
    # Consumer Cyclical
    assert financial_data['ROST']['1/31/2020']['Net Income'] == 1660928
    # Consumer Defensive
    assert financial_data['CAG']['5/31/2019']['Net Income'] == 678300
    # Energy
    assert financial_data['E']['12/31/2018']['Net Income'] == 4126000
    # Technology
    assert financial_data['LAZR'] == None
    # Financial Services
    assert financial_data['COOL'] == None
    # Real Estate
    assert financial_data['SBAC']['ttm']['Net Income'] == 146991


def test_number_of_titles():
    # Utilities
    assert len(financial_data['FE']) == 5
    # Basic Materials
    assert len(financial_data['CRH']) == 4
    # Industrials
    assert len(financial_data['HON']) == 5
    # Financial Services
    assert len(financial_data['LMND']) == 3


def main():
    test_get_data_financial_statements()
    test_number_of_titles()


if __name__ == "__main__":
    main()