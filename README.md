# Data Mining Project - Pulling Data From Yahoo Finance!

## Created by Bar Laniado and Anat Kira

In this project we are pulling data from yahoo finance web-site: https://finance.yahoo.com/\
At the site, by pressing the Industries tub you can find a list with different sectors, like Energy, Healthcare, Technology and more...\
In each sector, all the different companies with their daily update stock information.\
We focused at the stock price, the change in the stock price from yesterday and the stock volume of each company, and arrange the data in a dictionary when the key is the company symbol.\
![](appendix/daily_data.PNG)
While our first dictionary holds the daily information about each company, we created a second dictionary for the annual Net income of each company.\
To reach the Net Income at the web-site: press on the company symbol by your interest, a new page will pop-up, choose the Financials tube, scroll down in the table till you reach the row: Net Income Common Stockholders
![](appendix/net_income.PNG)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) (version 21.0.1) to install the requests and beautifulsoup4 libraries.\
we used the versions:\
2.25.1 for requests\
4.9.3 for beautifulsoup4, 0.0.1 for bs4\
1.0.2 for PyMySQL
**Python 3.9.0**

## Before Running
**Building The Database**\
Please take care to build the DB infrastructure properly.\
To do so: go to the db directory and run data_mining_db.sql in your MySql,\
this file will create the data base and the tables that are needed to run this program.\
**Database configutations**\
Please go to the configurations file and change the DB connection details:\
HOST = Put here the host, the default is 'localhost'\
USER: Put here your username\
PASSWORD = Put here your password\
DB = Put here the DB name, the defual is'stock_data'\
CHARSET = The defualt is'utf8mb4'\
SECTORS_TABLE = Put here the table name that will contain all the unique sectors, the default is'sectors'\
SYMBOLS_SECTORS_TABLE = Put here the table name that will contain all the unique symbols and sectors, the default is 'symbol_sector'\
DAILY_DATA_TABLE = Put here the table name that will contain all the daily data, the default is 'daily_data'\
FINANCIAL_DATA_TABLE = Put here the table name that will contain all the financial data, the default is 'financial_data'\
**Note:**
If you built the database with the file provided with this project and did not change anything,\
all you need to change in the DB configurations: USER & PASSWORD

## Usage
**Command line interface**
You can execute the program directly from the command line.\
All you need is to run our: **main_file.py**\
You can also run the program with different arguments.
**Arguments:**
**-s** When you specify this argument you ignore the default sectors to scrape and to actually determine which sectors you want to be scrapped.\
The default is to scrape all the sectors that exist in Yhaoo-Finance:
**"Technology", "Basic Materials", "Healthcare", "Energy", "Communication Services",
"Consumer Cyclical", "consumer Defensive", "Financial Services", "Industrials", "Real Estate","utilities"**.\
If for any reason you don't want to scrape all the sectors, all you need is to specify -s and immediately after all the sectors that you want to be scrapped.\
**For example:**
Let's say I want to scrape only "Technology" and "consumer Defensive" this time.\
In order to so I would run the command:\
python main_file.py -s  "Technology" "consumer Defensive"\
**Do you want to change the default sectors?**
Go to the configuration file and change the SECTORS according to your needs.




You will get all the data about all the companies from all the different sectors from the web-site.\


When running the script it will also create a new file contain the logs output, the file name is data_mining.log and you could find it in the logs directory.\
You can choose one of two options:\
At the first option the logger is set to INFO level, this option is our default option.\
The second option will output exactly the same the only different is that the logger is set to DEBUG.\
For the second option you need to run the file: **run_project_debug_level.py** from the debug_level directory.\
Running that file will create new file: debug_logs.log in the logs directory and a json_files directory inside the debug_level directory containing the two json files with our two dictionaries.

##Hope you will enjoy and start to invest in the stock market (;

#Good Luck!





