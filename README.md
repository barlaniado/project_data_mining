#Data Mining Project - pulling data from Yahoo! finance

##Created by Bar Laniado and Anat Kira

In this project we are pulling data from yahoo finance web-site: https://finance.yahoo.com/\
At the site by pressing the Industries tub you can find a list with different sectors, like Energy, Healthcare, Technology and more...\
In each sector all the different companies with their daily update stock information.\
We focused at the stock price, the change in the stock price from yesterday and the stock volume of each company and arrange the data in a dictionary when the key is the company symbol.\
While our first dictionary holds the daily information about each company, we created a second dictionary for the annual Net income of each company.\ 
To reach the Net income at the web-site: press on the company symbol you interested --> in the new page press the Financials tube --> scroll down in the table till you reach the tube: Net Income Common Stockholders\
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requests and beautifulsoup4 libraries.
we use this versions:
2.24.0 for requests
and 4.9.1 for beautifulsoup4



