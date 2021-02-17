# requests_webpages
#SECTORS = ["Technology", "Basic materials", "Healthcare", "Energy"]
SECTORS = ["Basic materials"]
COUNT = 100
HTML_PARSER = 'html.parser'
HEADERS = {
    'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

# utilities
PRAM_VALUE_SLEEP_NO_COUNTER = None
MIN_TIME_SLEEP_NO_COUNTER = 5
MAX_TIME_SLEEP_NO_COUNTER = 7
WHEN_LONG_SLEEP = 1000
TIME_LONG_SLEEP = 120
NO_REMAINDER = 0
WHEN_MODERATE_SLEEP = 100
TIME_MODERATE_SLEEP = 30




# get_daily_data
TAG_TO_RETRIEVE_DAILY_DATA = 'span'
CLASS_GET_DAILY_DATA = "Trsdu(0.3s)"
PRICE_INDEX = 0
PRICE_CHANGE_INDEX = 1
PRICE_CHANGE_PERCENTAGE = 2
VOLUME_CURRENT_DAY = 3
FIND_AVG_VOL = 'td'
TITLE_AVG_VOL = "Avg Vol (3 month)"
ATTRS_AVG_VOL = 'aria-label'
SYMBOL_INDEX = 0
FIND_LINE_TAG = 'tr'
KEY_TIME = 'Time'
KEY_PRICE = 'Price'
KEY_PRICE_CHANGE = 'Price change'
KEY_PRICE_CHANGE_PERCENTAGE = 'Percentage'
KEY_VOLUME = 'Volume'
KEY_AVG_VOLUME = 'Avg Vol (3 month)'
LOGGER_MESSAGE_BUILD_DAILY_SECTOR_DICT = 'The data was successfully added to the dictionary'
OFFSET_OF_FIRST_PAGE_SECTOR = 0
HOW_MANY_SYMBOLS_EACH_PAGE = 100
TAG_TABLE_IN_PAGE = "tbody"
TABLE_CONTENT_INDEX = 0


# get_data_of_financial_statements
TAG_DATA_FINANCIAL_STATEMENTS = 'span'
TOTAL_REVENUE_TITLE = 'Total Revenue'
DELETE_FROM_NET_INCOME_STRING = ','
REPLACE_DELETED_CHAR_WITH = ""
KEY_NET_INCOME = 'Net Income'
VALUE_IF_CANT_CAST_TO_INT = None
NEXT_TO_COME_TITLES = 'Breakdown'
NEXT_TO_COME_DATA_NET_INCOME = 'Net Income Common Stockholders'




