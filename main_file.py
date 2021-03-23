from getData import main_scraper
from utilities import utilities
from logs import logger as logs
from configuration import project_conf
import argparse


def main():
    """
    This is the function that manages the whole scraping process.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sector_to_scrape', nargs='+', type=str.title)

    parser.add_argument('-d', '--debug', action='store_true')
    args = parser.parse_args()
    if not args.sector_to_scrape:
        sector_to_scrape = project_conf.SECTORS
    else:
        sector_to_scrape = set(args.sector_to_scrape)
        if not sector_to_scrape.issubset(set(project_conf.SECTORS)):
            print("Non-existent sectors were inserted")
            quit()
    project_conf.logger = logs.Logger(args.debug)
    main_scraper.MainScraperSymbols(sector_to_scrape)


if __name__ == "__main__":
    main()

