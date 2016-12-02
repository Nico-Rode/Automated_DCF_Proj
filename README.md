PyFinancialData
===============

-A python library for pulling financial data from Morningstar and Yahoo.

-Includes over 100 functions for income statement, balance sheet, and cashflow items, as well as various valuation metrics.

-Data is fetched from Morningstar and Yahoo Finance.

-FREQUENCY refers to Annual (A), or Quarterly (Q) for financial metrics,
 TIME is how many columns (Years) the script scrapes from the downloaded excel file (1 - 5)
 For a pure DCF Implementation the default TIME should be 5 representing the last 5 years of financial data


- Credit to VincentRaia for the skeleton code of pulling the financial data from Morningstar and Yahoo
   - https://github.com/VincentRaia



Dependencies
===============

-urllib2

-pandas

-Quandl


===============

# THIS IS ENTIRELY DEPENDANT ON MORNGINGSTAR; IF THEY DECIDE TO CHANGE THEIR URL ADDRESSES OR SHUTDOWN THIS
# PROGRAM BECOMES USELESS.

# FREQUENCY refers to Annual (A), or Quarterly (Q) for financial metrics,
# TIME is how many columns (Years) the script scrapes from the downloaded excel file (1 - 5)
# For a pure DCF Implementation the default TIME should be 5 representing the last 5 years of financial data


#**********************************************************************************


#************************************** TO DO ******************************

# Still need to fix all the functions on the function page, follow format of functions.revenue, or
# functions.cost_of_goods, functions.income_before_taxed, etc.

# Still need various QA implementations, and more efficient and cleaner code to grab all the data. Maybe download the
# income statement, balance sheet, and cashflow sheet ONCE and put them into three separate data frames. From
# there you can parse through in order to find the relevant metrics for each functions.

# Implement different functions for overall DCF process and segment the parts of DCF process into smaller functions
# such as the implementation of the Income statement, Balance sheet, and Cashflow, add functionality for other Metrics
# as well.

# Also need to figure out a way to deal with modularity and flexibility. By these I mean what happens when the rows
# don't exactly match the ones in your array. What happens when the numbers don't add up or a stock doesn't label their
# data the exact same as you have it. This will take a lot of trial and error, try and except blocks. You also thought
# about using either the row #, or the attribute name as it appears in the excel file as keys for the dictionary.
# If you pair the attribute name and then continue with the low level approach of working down with the excel file,
# I think that it would absolutely ensure accuracy when placing the data, even if the row and column NUMBERS change.

# Maybe implement machine learning functions in order to make educated guesses on assumptions

# You for sure can pull data for the initial global assumptions though

# Modularity is HUGE

# Safe guards to check and see if the stock's net income, free cash flow, etc. match up with the ones found in the
# csv files and the company's reported numbers.

# Make sure to check and see if the data is reported in millions or thousands; if thousands then just truncate the nums
