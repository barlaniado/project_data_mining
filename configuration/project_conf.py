# requests_webpages
SECTORS = ["Technology", "Basic materials", "Healthcare", "Energy", "Communication Services",
            "Consumer Cyclical", "consumer Defensive", "Financial Services", "Industrials", "Real Estate",
            "utilities"]
COUNT = 100
HTML_PARSER = 'html.parser'
HEADERS = {
    'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko)'
        ' Chrome/56.0.2924.87 Safari/537.36'
}


# utilities
VALUE_SLEEP_NO_COUNTER = None
MIN_TIME_SLEEP_NO_COUNTER = 5
MAX_TIME_SLEEP_NO_COUNTER = 7
WHEN_LONG_SLEEP = 1000
TIME_LONG_SLEEP = 0 #120
NO_REMAINDER = 0
WHEN_MODERATE_SLEEP = 100
TIME_MODERATE_SLEEP = 0 #30
MIN_SHORT_SLEEP = 0 #5
MAX_SHORT_SLEEP = 0 #7
MAIN_TAG_HOW_MANY_SYMBOLS = 'div'
MAIN_CLASS_HOW_MANY_SYMBOLS = 'Pos(r) Pos(r) Mih(265px)'
SUB_TAG_HOW_MANY_SYMBOLS = 'span'
SUB_CLASS_HOW_MANY_SYMBOLS = 'Mstart(15px) Fw(500) Fz(s)'
CHER_SPLIT_TO_GET_HOW_MANY_SYMBOLS = ' '
INDEX_HOW_MANY_AFTER_SPLIT = -2
START_URL_SECTOR_PAGE = 'https://finance.yahoo.com/screener/predefined/ms_'
SPACE_TO_REPLACE = ' '
CHAR_INSTEAD_SPACE = '_'
OFFSET_IS = '?offset='
COUNT_IS = '&count='
START_URL_FINANCIALS = 'https://finance.yahoo.com/quote/'
REST_URL_FINANCIALS = '/financials?p='
LONG_SLEEP_DEBUG_LOGGER = "The program is sleeping"
JSON_FILES_PATH = "json_files"
CREATE_JSON_FOLDER_MESSAGE = "Json folder was created"
FINANCIALS_DATA_FILE_NAME = "_financials.json"
DAILY_DATA_FILE_NAME = "_daily_data.json"


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
KEY_SECTOR = 'Sector'
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
START_SCRAPE_SECTOR_MESSAGE = "Started to scrape sectors pages"
FINISH_SECTOR_SCRAPING_MESSAGE = "Finished to scrape sectors pages"
ASSUMPTION_TBODY_LEN = 1
LEN_OF_DICT_DAILY_LOGGER_MESSAGE = "The length of the daily data dict that was created is: "
NOW_SYMBOLS_MESSAGE_LOGGER = "Found the symbol: "
ALREADY_EXIST_SYMBOL = "already exists in the dictionary"
SYMBOL_SECTOR_DATA_FILE_NAME = "_symbol_sector.json"
DATA_LIST_EMPTY = "Can't find the wanted data."
RESPONSE_EMPTY = "The response is empty of the required content."
SYMBOL_EXISTS_LOGGER_MESSAGE = ": Data about the current symbol already exists in the daily dictionary"
INVALID_PRICE_LOG_MESSAGE = "Invalid price"
INVALID_PRICE_CHANGE_LOG_MESSAGE = "Invalid price change"
INVALID_PRICE_CHANGE_PERCETAGE_LOG_MESSAGE = "The percentage change is invalid"
INDEX_PERCENTAGE_IN_TEXT = -1
PERCENTAGE_SIGN = "%"
HOW_MANY_REPLACE_PERCENTAGE_ALLOWED = 1


# get_data_of_financial_statements
TAG_DATA_FINANCIAL_STATEMENTS = 'span'
TOTAL_REVENUE_TITLE = 'Total Revenue'
DELETE_FROM_NET_INCOME_STRING = ','
REPLACE_DELETED_CHAR_WITH = ""
KEY_NET_INCOME = 'Net Income'
VALUE_IF_CANT_CAST_TO_INT = None
NEXT_TO_COME_TITLES = 'Breakdown'
NEXT_TO_COME_DATA_NET_INCOME = 'Net Income Common Stockholders'
NO_DATA_MESSAGE_LOGGER = "Report data was not obtained - "
DATA_FINANICIALS_ADDED = "The data on the financial statements have been added to the dictionary - "



