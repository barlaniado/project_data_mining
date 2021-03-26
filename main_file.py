from getData import main_scraper
from logs import logger as logs
from configuration import project_conf
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--sector_to_scrape', nargs='+', type=str.title,
                        help=project_conf.S_MESSAGE)
    parser.add_argument('-d', '--debug', action='store_true', help=project_conf.D_MESSAGE)
    parser.add_argument('-f', '--financials', action='store_true', help=project_conf.F_MESSAGE)
    args = parser.parse_args()
    project_conf.logger = logs.Logger(args.debug)
    if not args.sector_to_scrape:
        sector_to_scrape = project_conf.SECTORS
    else:
        sector_to_scrape = set(args.sector_to_scrape)
        if not sector_to_scrape.issubset(set(project_conf.SECTORS)):
            project_conf.logger.logger.error(project_conf.NON_EXISTING_SECTOR_ERROR_MESSAGE)
            quit()
    # Build a MainScraperSymbols object. This object holds the scraped data.
    # If args.financials = True the financial data will be scraped also.
    main_scraper.MainScraperSymbols(sector_to_scrape, args.financials)


if __name__ == "__main__":
    main()

