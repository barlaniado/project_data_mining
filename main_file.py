from getData import get_daily_data
from getData import get_data_of_financial_statements
from utilities import utilities
from logs import logger as logs
from configuration import project_conf
import argparse


def main():
    """
    This is the function that manages the whole scraping process.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--sector_to_scrape', nargs='+', type = str.title)
    parser.add_argument('-d','--debug', nargs='+', type =bool, default = False)
    args = parser.parse_args()
    if not args.sector_to_scrape:
        sector_to_scrape = project_conf.SECTORS
    else:
        sector_to_scrape = set(args.sector_to_scrape)
        if not sector_to_scrape.issubset(set(project_conf.SECTORS)):
            print("Non-existent sectors were inserted")
            quit()
    project_conf.logger = logs.Logger(args.debug)
    tuple_list_dict = get_daily_data.scrape_sector_pages(sector_to_scrape)
    list_symbols = list(tuple_list_dict[0])
    financial_statements = get_data_of_financial_statements.get_all_data_financial_statements(list_symbols)
    project_conf.logger.logger.info(f"The dictionary of the financial reports was created. the dictionary size is:"
                       f" {len(financial_statements)}")
    utilities.to_json_all(tuple_list_dict[1], financial_statements)


if __name__ == "__main__":
    main()

