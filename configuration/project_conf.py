# DB Configurations
HOST = 'localhost'
USER = 'root'
PASSWORD = 'Password123#@!'
DB = 'stock_data'
CHARSET = 'utf8mb4'
# main scraper
SECTORS_TABLE = 'sectors'
SYMBOLS_SECTORS_TABLE = 'symbol_sector'
DAILY_DATA_TABLE = 'daily_data'
FINANCIAL_DATA_TABLE = 'financial_data'
RECOMMENDATIONS_TABLE = 'recommendations'
COLUMNS_INSERT_NEW_SYMBOL_SECTOR = 'symbol, id_sector'
COLUMNS_INSERT_DAILY_DATA = 'symbol, time_scraped, price, price_change,' \
                            ' percentage_change, volume, avg_3_months_volume'
COLUMNS_INSERT_FINANCIAL_DATA = 'symbol, date_report, net_income'
COLUMNS_INSERT_RECOMMENDATION = 'symbol, date_recommendations, type_recommendation, how_many'


# main file
NON_EXISTING_SECTOR_ERROR_MESSAGE = " Non-existent sectors were inserted"

# main_scraper
CONNECTION_DB_ERROR = "There is a problem connecting to the DB."
INSERT_DATA_TO_DB_MESSAGE = "Insert the data into the DB"
INSERT_FINANCIAL_DATA_TO_DB_MESSAGE = "Insert the financials data into the DB"
INSERT_NEW_SECTOR = "New sector found: {0}"
ADD_NEW_SECTOR = "Add {0} to {1} table"
INSERT_SYMBOL_DAILY_DATA = "Insert the daily data of {0}"
INSERT_SYMBOL_FINANCIAL_DATA = "Insert the financial data of {0}"

UPDATE_SECTOR = "The sector of {0} needs to be updated"
NEW_SYMBOL_MESSAGE = "A new symbol has been found: {0}"
DUPLICATE_SECTOR = "The sector ({0}) appears more than once in the sectors table"
CHECK_ID_SECTOR_NOT_EXISTS = "The ID of the sector ({0}) not found in the sectors table"
FORMAT_DATE_FINANCIAL = '%m/%d/%Y'

# Queries
GET_SECTORS = f'SELECT DISTINCT(sector) FROM {SECTORS_TABLE}'
SELECT_SYMBOL_SECTOR = 'SELECT id_sector FROM {0} WHERE symbol = "{1}";'
SELECT_SECTOR = 'SELECT sector FROM {0} WHERE sector = "{1}";'
INSERT_SECTOR = 'INSERT INTO {0} (sector) VALUES ("{1}");'
CHANGE_SECTOR_TO_EXIST_SYMBOL = 'UPDATE {0} SET id_sector = {1} WHERE symbol = "{2}"'
ID_OF_SECTOR_QUERY = 'SELECT id_sector FROM {0} WHERE sector = "{1}"'
INSERT_NEW_SYMBOL_SECTOR = "INSERT INTO {0} ({1}) VALUES ('{2}', {3});"
INSERT_DAILY_DATA = 'INSERT IGNORE INTO {0} ({1}) VALUES ("{2}", "{3}", {4}, {5}, {6}, "{7}", "{8}");'
DAILY_DATA_SYMBOL_TIME = 'SELECT symbol FROM {0} WHERE symbol = "{1}" AND DAY(time_scraped) = "{2}";'
INSERT_FINANCIAL_DATA = 'INSERT IGNORE INTO {0} ({1}) VALUES ("{2}", "{3}", {4});'
CHECK_IF_SECTOR_EXISTS_LOG = "Checking if the sector ({0}) of the current symbol ({1}) exists"
INSERT_RECOMMENDATION = 'INSERT IGNORE INTO {0} ({1}) VALUES ("{2}", "{3}", "{4}", {5});'



# argparse
S_MESSAGE = "Specify which sectors to scrape," \
            " if not explicitly specified, the default is to do a scraping" \
            " for all the sectors in the SECTORS list which located in the configurations file." \
            "For example: in order to scrape only 'Technology' and 'Basic Materials' sectors use:" \
            "-s \"Technology\" \"Basic Materials\""
D_MESSAGE = "If the flag is specified the software will work in debug mode"
F_MESSAGE = "If the flag is specified the software will scrape the financial data also"
R_MESSAGE = "If the flag is specified the software will get recommendations for the symbols"

# requests_webpages

SECTORS = ["Technology", "Basic Materials", "Healthcare", "Energy", "Communication Services",
           "Consumer Cyclical", "Consumer Defensive", "Financial Services", "Industrials", "Real Estate", "Utilities"]

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
TIME_LONG_SLEEP = 220
NO_REMAINDER = 0
WHEN_MODERATE_SLEEP = 100
TIME_MODERATE_SLEEP = 45
MIN_SHORT_SLEEP = 10
MAX_SHORT_SLEEP = 12
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
LOGGER_WARNING_MESSAGE_TBODY_MORE_THAN = "Length of the current tbody is more than expected"
LOGGER_WARNING_MESSAGE_TBODY_LESS_THAN = "Length of the current tbody is less than expected"
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

# Recommendations
URL = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-analysis"
HOW_MANY_HEADERS = 13

HEADERS_API1 = {
    'x-rapidapi-key': "6f9df8abb4mshe24d1c070334264p1e54e0jsn47ddfd1cb4f2",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

HEADERS_API2 = {
    'x-rapidapi-key': "f7077a5b9fmshe2402a988b1fcdcp11af63jsnaf866e466f34",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

HEADERS_API3 = {
    'x-rapidapi-key': "8a8b36728emsh3469bf1d8521521p109200jsn1a2326a9eb03",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

HEADERS_API4 = {
    'x-rapidapi-key': "3ae6407b97msh45b0810bfa259a4p1abe26jsndc1924d1b200",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

HEADERS_API5 = {
    'x-rapidapi-key': "7bd79c4382msha526df7f1259f1ep17c11djsn0151c3fe4b12",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

HEADERS_API6 = {
    'x-rapidapi-key': "b1a9bb4903mshbbd52394daf924ep14912ajsn1cd71951d290",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}
HEADERS_API7 = {
    'x-rapidapi-key': "acc98e4d96mshecf7097d7d227cbp17ed84jsn4433bfbd4e81",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}
HEADERS_API8 = {
    'x-rapidapi-key': "2197bb34a7msh4d188ceb6ae4c05p10d500jsnbd31e7e2b04b",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}
HEADERS_API9 = {
    'x-rapidapi-key': "bfb11a16demsh515ca8c1a7adefbp1d6debjsne40a600f4b24",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
}

HEADERS_API10 = {
    'x-rapidapi-key': "de9c2bb43cmsh3bbe05b548b8181p1c099ajsn17c95da5e425",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

HEADERS_API11 = {
    'x-rapidapi-key': "d597962f85msh8180f938d30c85ep1b8137jsne77bb686f196",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }
HEADERS_API12 = {
    'x-rapidapi-key': "8cca3d077emshab0c8ee7421bd9ep14f2fajsndad16330aba6",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }

HEADERS_API13 = {
    'x-rapidapi-key': "271fe15c5fmsh96d3a2799a5c3b2p1eb404jsne0d4490409cd",
    'x-rapidapi-host': "apidojo-yahoo-finance-v1.p.rapidapi.com"
    }



LIST_OF_HEADERS = [HEADERS_API1, HEADERS_API2 , HEADERS_API3, HEADERS_API4, HEADERS_API4, HEADERS_API5, HEADERS_API6,
                   HEADERS_API7, HEADERS_API8, HEADERS_API9, HEADERS_API10, HEADERS_API11, HEADERS_API12, HEADERS_API13]

# logger
logger = None


