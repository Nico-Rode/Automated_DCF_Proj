PyFinancialData
===============

-A python library for pulling financial data from Morningstar and Yahoo.

-Includes over 100 functions for income statement, balance sheet, and cashflow items, as well as various valuation metrics.

-Data is fetched from Morningstar and Yahoo Finance.


- Credit to VincentRaia for the skeleton code of pulling the financial data from Morningstar and Yahoo
   - https://github.com/VincentRaia



Dependencies
===============

-urllib2

-pandas

-Quandl


TODO
===============

-Fix financial statement requests for bank stocks

-Add graphing capability

#Net income is off a little, the column that doesn't match is SG&A + other expenses. Need to investigate further

#Still need to fix all the functions on the function page, follow format of functions.revenue, or
# functions.cost_of_goods, functions.income_before_taxed, etc.

#FREQUENCY refers to Annual (A), or Quarterly (Q) for financial metrics,
#TIME is how many columns (Years) the script scrapes from the downloaded excel file (1 - 5)
#For a pure DCF Implementation the default TIME should be 5 representing the last 5 years of financial data

#Consider making the BASE_CASE_Excel_Rows a dictionary of which the keys are the names of the metrics.

#Still need various QA implementations, and more efficient and cleaner code to grab all the data

#Implement different functions for overall DCF process and segment the parts of DCF process into smaller functions
#such as the implementation of the Income statement, Balance sheet, and Cashflow, add functionality for other Metrics
#as well.