import json
import os

# load daily data

with open('./DataForTests/daily_data_for_test.json') as data:
    daily_data = json.load(data)


def test_get_price():
    # Basic Materials
    assert float(daily_data['RPM']['Price']) == 83.11
    assert float(daily_data['WPM']['Price']) == 37.65
    assert float(daily_data['GOLD']['Price']) == 19.78
    assert float(daily_data['RIO']['Price']) == 89.99
    assert float(daily_data['X']['Price']) == 17.9
    assert float(daily_data['OLN']['Price']) == 29.98
    assert float(daily_data['NEU']['Price']) == 394.04
    assert float(daily_data['SA']['Price']) == 18.25
    assert float(daily_data['RYAM']['Price']) == 8.7
    assert float(daily_data['SPPP']['Price']) == 18.56
    assert float(daily_data['CGA']['Price']) == 5.35
    # Communication Services
    assert float(daily_data['GOOG']['Price'].replace(",", "")) == 2101.14
    assert float(daily_data['FB']['Price']) == 261.56
    assert float(daily_data['KT']['Price']) == 11.75
    assert float(daily_data['YELP']['Price']) == 36.15
    assert float(daily_data['GTN-A']['Price']) == 17.38
    # Consumer Cyclical
    assert float(daily_data['AMZN']['Price'].replace(",", "")) == 3249.9
    assert float(daily_data['IP']['Price']) == 48.95
    assert float(daily_data['TNL']['Price']) == 55.25
    # Consumer Defensive
    assert float(daily_data['WMT']['Price']) == 138.34
    assert float(daily_data['GO']['Price']) == 41.48
    assert float(daily_data['KOF']['Price']) == 45.19
    # Energy
    assert float(daily_data['VLO']['Price']) == 71.53
    assert float(daily_data['ALIN-PB']['Price']) == 23.03
    assert float(daily_data['TGP-PB']['Price']) == 25.56
    # Financial Services
    assert float(daily_data['V']['Price']) == 204.73
    assert float(daily_data['AXP']['Price']) == 131.71
    assert float(daily_data['FULTP']['Price']) == 25.72
    # Healthcare
    assert float(daily_data['BDX']['Price']) == 247.93
    assert float(daily_data['MRNA']['Price']) == 174.74
    assert float(daily_data['TFX']['Price']) == 390.43
    # Industrials
    assert float(daily_data['CNI']['Price']) == 109.08
    assert float(daily_data['DAL']['Price']) == 45.67
    assert float(daily_data['J']['Price']) == 112.41
    # Real Estate
    assert float(daily_data['WY']['Price']) == 34.99
    assert float(daily_data['OPEN']['Price']) == 31.58
    assert float(daily_data['JLL']['Price']) == 156.92
    # Utilities
    assert float(daily_data['ES']['Price']) == 81.46
    assert float(daily_data['HE']['Price']) == 35.02
    assert float(daily_data['JE']['Price']) == 5.77
    # Technology
    assert float(daily_data['AAPL']['Price']) == 129.87
    assert float(daily_data['TSM']['Price']) == 136.66
    assert float(daily_data['CRM']['Price']) == 246.56


def test_get_change():
    # Basic Materials
    assert daily_data['ICL']['Price change'] == '+0.07'
    assert daily_data['X']['Price change'] == '+0.90'
    assert daily_data['SUM']['Price change'] == '+2.12'
    # Communication Services
    assert daily_data['Z']['Price change'] == '-0.03'
    assert daily_data['IQ']['Price change'] == '-0.89'
    assert daily_data['IPG']['Price change'] == '+0.75'
    # Consumer Cyclical
    assert daily_data['BABA']['Price change'] == '-0.92'
    assert daily_data['TSLA']['Price change'] == '-6.08'
    assert daily_data['EBAYL']['Price change'] == '-0.02'
    # Consumer Defensive
    assert daily_data['UL']['Price change'] == '-1.24'
    assert daily_data['CL']['Price change'] == '-1.52'
    assert daily_data['K']['Price change'] == '-1.62'
    # Energy
    assert daily_data['SU']['Price change'] == '+0.21'
    assert daily_data['ET']['Price change'] == '+0.22'
    assert daily_data['AM']['Price change'] == '+0.01'
    # Financial Services
    assert daily_data['JPM']['Price change'] == '+2.43'
    assert daily_data['PYPL']['Price change'] == '-3.89'
    assert daily_data['C']['Price change'] == '+2.30'
    # Healthcare
    assert daily_data['PFE']['Price change'] == '-0.12'
    assert daily_data['BDX']['Price change'] == '-7.89'
    assert daily_data['A']['Price change'] == '-0.81'
    # Industrials
    assert daily_data['CP']['Price change'] == '+8.21'
    assert daily_data['ROK']['Price change'] == '+4.04'
    assert daily_data['FAST']['Price change'] == '-0.06'
    # Real Estate
    assert daily_data['O']['Price change'] == '+0.17'
    assert daily_data['AVB']['Price change'] == '+0.24'
    assert daily_data['A']['Price change'] == '-0.81'
    # Utilities
    assert daily_data['ES']['Price change'] == '-1.09'
    assert daily_data['WEC']['Price change'] == '-0.25'
    assert daily_data['NI']['Price change'] == '0.00'
    # Technology
    assert daily_data['NVDA']['Price change'] == '+3.90'
    assert daily_data['MU']['Price change'] == '+2.42'
    assert daily_data['IBM']['Price change'] == '-1.74'


def test_get_change_percentage():
    # Basic Materials
    assert daily_data['DOW']['Percentage'] == '+4.92%'
    assert daily_data['FNV']['Percentage'] == '-1.86%'
    assert daily_data['MT']['Percentage'] == '+4.14%'
    # Communication Services
    assert daily_data['T']['Percentage'] == '-0.79%'
    assert daily_data['NFLX']['Percentage'] == '-1.46%'
    assert daily_data['ZM']['Percentage'] == '-0.16%'
    # Consumer Cyclical
    assert daily_data['SBUX']['Percentage'] == '-1.52%'
    assert daily_data['NIO']['Percentage'] == '+1.12%'
    assert daily_data['GM']['Percentage'] == '+0.79%'
    # Consumer Defensive
    assert daily_data['TAL']['Percentage'] == '+4.12%'
    assert daily_data['PPC']['Percentage'] == '-0.62%'
    assert daily_data['BIG']['Percentage'] == '+3.06%'
    # Energy
    assert daily_data['E']['Percentage'] == '+1.59%'
    assert daily_data['TS']['Percentage'] == '+1.33%'
    assert daily_data['SUN']['Percentage'] == '+1.37%'
    # Financial Services
    assert daily_data['MA']['Percentage'] == '-1.56%'
    assert daily_data['RY']['Percentage'] == '+1.05%'
    assert daily_data['ICE']['Percentage'] == '-0.45%'
    # Healthcare
    assert daily_data['SEM']['Percentage'] == '+2.15%'
    assert daily_data['NFH']['Percentage'] == '+0.36%'
    assert daily_data['IVC']['Percentage'] == '+5.45%'
    # Industrials
    assert daily_data['ROP']['Percentage'] == '-1.68%'
    assert daily_data['GNRC']['Percentage'] == '+3.42%'
    assert daily_data['TRU']['Percentage'] == '-0.49%'
    # Real Estate
    assert daily_data['VTR']['Percentage'] == '+1.53%'
    assert daily_data['DRE']['Percentage'] == '-0.07%'
    assert daily_data['CPT']['Percentage'] == '+1.28%'
    # Utilities
    assert daily_data['FE']['Percentage'] == '-0.64%'
    assert daily_data['NI']['Percentage'] == '0.00%'
    assert daily_data['UGI']['Percentage'] == '+1.92%'
    # Technology
    assert daily_data['UBER']['Percentage'] == '-1.03%'
    assert daily_data['SHOP']['Percentage'] == '+3.64%'
    assert daily_data['NOW']['Percentage'] == '-0.88%'


def test_get_volume():
    # Basic Materials
    assert daily_data['MT']['Volume'][0] == '3'
    assert daily_data['MT']['Volume'][-1] == 'M'
    assert daily_data['FNV']['Volume'][0] == '1'
    assert daily_data['FNV']['Volume'][-1] == 'M'
    assert daily_data['OLN']['Volume'][0] == '1'
    assert daily_data['OLN']['Volume'][-1] == 'M'
    # Communication Services
    assert daily_data['IQ']['Volume'][0] == '8'
    assert daily_data['IQ']['Volume'][-1] == 'M'
    assert daily_data['IQ']['Volume'][0] == '8'
    assert daily_data['VIV']['Volume'][0] == '1'
    assert daily_data['VIV']['Volume'][-1] == 'M'
    # Consumer Cyclical
    assert daily_data['TM']['Volume'][0:2] == '23'
    assert daily_data['ROST']['Volume'][0] == '1'
    assert daily_data['ROST']['Volume'][-1] == 'M'
    assert daily_data['F']['Volume'][0] == '4'
    assert daily_data['F']['Volume'][-1] == 'M'
    # Consumer Defensive
    assert daily_data['PG']['Volume'][-1] == 'M'
    assert daily_data['SYY']['Volume'][0] == '2'
    assert daily_data['SYY']['Volume'][-1] == 'M'
    # Financial Services
    assert daily_data['BAC']['Volume'][-0] == '5'
    assert daily_data['BAC']['Volume'][-1] == 'M'
    # Energy
    assert daily_data['VLO']['Volume'][0] == '5'
    assert daily_data['VLO']['Volume'][-1] == 'M'
    # Healthcare
    assert daily_data['PFE']['Volume'][0] == '2'
    assert daily_data['PFE']['Volume'][-1] == 'M'
    # Industrials
    assert daily_data['NEE']['Volume'][0] == '9'
    assert daily_data['NEE']['Volume'][-1] == 'M'
    # Real Estate
    assert daily_data['WY']['Volume'][0] == '4'
    assert daily_data['WY']['Volume'][-1] == 'M'
    # Utilities
    assert daily_data['NI']['Volume'][0] == '3'
    assert daily_data['NI']['Volume'][-1] == 'M'
    # Technology
    assert daily_data['ORCL']['Volume'][0] == '1'
    assert daily_data['ORCL']['Volume'][-1] == 'M'


def main():
    test_get_price()
    test_get_change()
    test_get_change_percentage()
    test_get_volume()


if __name__ == '__main__':
    main()