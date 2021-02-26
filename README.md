#Data Mining Project - pulling data from Yahoo! finance

##Created by Bar Laniado and Anat Kira

In this project we are pulling data from yahoo finance web-site: https://finance.yahoo.com/\
At the site, by pressing the Industries tub you can find a list with different sectors, like Energy, Healthcare, Technology and more...\
In each sector, all the different companies with their daily update stock information.\
We focused at the stock price, the change in the stock price from yesterday and the stock volume of each company, and arrange the data in a dictionary when the key is the company symbol.\
![Screenshot](daily_data.png)
While our first dictionary holds the daily information about each company, we created a second dictionary for the annual Net income of each company.\
To reach the Net Income at the web-site: press on the company symbol by your interest, a new page will pop-up, choose the Financials tube, scroll down in the table till you reach the row: Net Income Common Stockholders
![Screenshot](net_income.png)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requests and beautifulsoup4 libraries.\
we used the versions:\
2.25.1 for requests\
4.9.3 for beautifulsoup4, 0.0.1 for bs4\
**Python 3**

## Usage

All you need is to run our: **main_file.py**\
You will get all the data about all the companies from all the different sectors from the web-site.\
It will be available in two new files that will created by running the script, in the directory: json_files.\
The first one will contain the dictionary with the annual information, the name of the file will be: <datetime.timestamp>_financials.json\
The second one will contain the dictionary with the daily information, the name of the file will be: <datetime.timestamp>_daily_data.json\
When running the script it will also create a new file contain the logs output, the file name is data_mining.log and you could find it in the logs directory.\
You can choose one of two options:\
At the first option the logger is set to INFO level, this option is our default option.\
The second option will output exactly the same the only different is that the logger is set to DEBUG.\
For the second option you need to run the file: **run_project_debug_level.py** from the debug_level directory.\
Running that file will create new file: debug_logs.log in the logs directory and a json_files directory inside the debug_level directory containing the two json files with our two dictionaries.

##Hope you will enjoy and start to invest in the stock market (;

#Good Luck!





