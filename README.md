#Data Mining Project - pulling data from Yahoo! finance

##Created by Bar Laniado and Anat Kira

In this project we are pulling data from yahoo finance web-site: https://finance.yahoo.com/\
At the site, by pressing the Industries tub you can find a list with different sectors, like Energy, Healthcare, Technology and more...\
In each sector, all the different companies with their daily update stock information.\
We focused at the stock price, the change in the stock price from yesterday and the stock volume of each company, and arrange the data in a dictionary when the key is the company symbol.\
While our first dictionary holds the daily information about each company, we created a second dictionary for the annual Net income of each company.\
To reach the Net income at the web-site: press on the company symbol by your interest --> in the new page press the Financials tube --> scroll down in the table till you reach the tube: Net Income Common Stockholders
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requests and beautifulsoup4 libraries.\
we used versions:\
2.24.0 for requests\
and 4.9.1 for beautifulsoup4

## Usage

All you need is to run our: main_file.py\
You will get all the data about all the companies from all the different sectors in the web-site.\
It will be available in two new files that will created by running the script in the directory: json_files.\
The first one contain the dictionary with the annual information, the name of the file: <datetime.timestamp>_financials.json\
The second one contain the dictionary with the daily information, the name of the file: <datetime.timestamp>_daily_data.json\
When running the script it will also creates a new file contain the logs, the file name is data_mining.log and you can find it in the logs directory.\ 
You can choose one of two options:\
The first option logs set to INFO level.\
The second option will output exactly the same except to the log level changed to DEBUG.\
You can change it to DEBUG level by: 





