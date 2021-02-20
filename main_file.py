import get_daily_data
import get_data_of_financial_statements
import utilities
import logger

def main():
    """
    This is the main function that receive the web site url and parse the data to two dictionaries:
    a daily and annual financial data of each company in each sector at that wbe site.
    """
    tuple_dict = get_daily_data.scrape_sector_pages()
    logger.logger.info(f"The Tuple dictionaries was created. the dictionaries size are: {len(tuple_dict[0])}"
                              f" and {len(tuple_dict[1])}")
    list_symbols = list(tuple_dict[0].keys())
    financial_statements = get_data_of_financial_statements.get_all_data_financial_statements(list_symbols)
    logger.logger.info(f"The dictionary of the financial reports was created. the dictionary size is:"
                       f" {financial_statements}")
    utilities.to_json_all(tuple_dict[0], tuple_dict[1], financial_statements)


if __name__ == "__main__":
    main()
