from getData import get_daily_data
from getData import get_data_of_financial_statements
from utilities import utilities
from logs import logger


def main():
    """
    This is the main function that receive the web site url and parse the data to two dictionaries:
    a daily and annual financial data of each company in each sector at that wbe site.
    """
    tuple_list_dict = get_daily_data.scrape_sector_pages()

    list_symbols = list(tuple_list_dict[0])
    financial_statements = get_data_of_financial_statements.get_all_data_financial_statements(list_symbols)
    logger.logger.info(f"The dictionary of the financial reports was created. the dictionary size is:"
                       f" {len(financial_statements)}")
    utilities.to_json_all(tuple_list_dict[1], financial_statements)


if __name__ == "__main__":
    main()

