import functions
import openpyxl
import quandl


#****************************************READ ME***********************************

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

# YOU HAVE TO CHECK FOR DIFFERENT NAMING CONVENTIONS. CHANGE TICKER TO CRM AND SEE THE ERRORS THAT POP UP.

#**************************TICKER************************
ticker = "AAPL"
#********************************************************




#*******************QUANDL TICKER INFORMATION************************
# Optional, it returns the last couple days of open and closed stock price


#quandl.ApiConfig.api_key = 'cBs2HV_F6r9ybCynEToS'
# quandl_ticker = ("WIKI/" + ticker)
# ticker_current_data = quandl.get(quandl_ticker).tail()
#
# print ticker, "OPEN: ", ticker_current_data["Open"], ticker, "CLOSE: ", ticker_current_data["Close"]

#************************************************************************


#**************************BASE CASE ROWS & COLUMNS************************
Base_Case_Excel_Rows = ['4','5','7','9','10','11','15','16','19','20','21','22','23','24','25','26','27'] #Relevant rows that need inputs on Base Case sheet
Base_Case_Excel_Col = ['F','E','D','C','B'] #Relevant columns that need inputs on Base Case sheet
DCF_Data_Keys = ["Revenue","COGS","SG&A and other expenses","Income before taxes","Provision for income expense","Other income expense",
                 "CAPEX","Depreciation_and_amort", "Inventories"
                  ,"Short Term Investments","Current Assets","Total Assets"
    ,"Short-term debt","Total Current Liabilities","Long-term debt","Total Liabilities",
                 "Total stockholder's equity"]
#**************************************************************************


#**************************Income statement metrics for DCF************************

# Dict of current financial metrics; contains all relevant metrics for DCF process
DCF_Data = {}
DCF_file = openpyxl.load_workbook(filename="WSIG DCF Template.xlsx")

#***********************************************************************************


#**************************INPUTTING DATA FOR INCOME STATMENT ON BASECASE***********************
# DCF_file = openpyxl.load_workbook(filename="WSIG DCF Template.xlsx")
# Base_Case_sheet = DCF_file.get_sheet_by_name("Base Case")
#
# for data in range(0, len(DCF_Data)): #For how every many financial metrics you have
#     counter = 0
#     for col in Base_Case_Excel_Col: #Go through the 5 columns
#         Base_Case_sheet[col + Base_Case_Excel_Rows[data]] = DCF_Data[data][counter] #Insert the corresponding year-metric to each year column
#         counter = counter + 1 #Makes sure that the DCF data gets all 5 of the entries for the metric
#
# DCF_file.save("WSIG DCF Output.xlsx")

#*****************************************************************************************************


def get_cashflow_statements(ticker): # FOR SOME REASON THIS IS THE QUARTERLY REPORT, NOT ANNUAL
    Cashflow_statement = {}

    Cashflow_statement["Depreciation_and_amort"] = functions.depreciation_amort_expense(ticker=ticker,frequency='A',time=5)
    Cashflow_statement["CAPEX"] = functions.capital_expenditures(ticker=ticker,frequency='A',time=5)

    return Cashflow_statement

def get_income_statement(ticker):
    Income_statement = {}

    Income_statement["Revenue"] = functions.revenue(ticker=ticker, time=5)
    Income_statement["COGS"] = functions.cost_of_goods(ticker=ticker, frequency="A", time=5)
    Income_statement["SG&A and other expenses"] = functions.sga_and_other_expenses(ticker=ticker, frequency="A", time=5)  # Off a little//Maybe fixed now?
    Income_statement["Income before taxes"] = functions.income_before_taxed(ticker=ticker, frequency="A", time=5)
    Income_statement["Provision for income expense"] = functions.provision_for_income_expense(ticker=ticker, frequency="A", time=5)
    Income_statement["Other income expense"] = functions.other_income_expense(ticker=ticker, frequency="A", time=5)

    # Is net income formula wrong? It's off by the amount of "Other income expense" If you take it out of the formula
    # in row 12, then the numbers match up. Check it out

    return Income_statement

def get_balance_sheet(ticker):
    Balance_sheet = {}

    Balance_sheet["Inventories"] = functions.inventories(ticker=ticker, frequency='A',time=5)
    Balance_sheet["Short Term Investments"] = functions.cash_and_short_term_investments(ticker=ticker,frequency='A',time=5) # Changed, but not sure if this adds up correctly
    Balance_sheet["Current Assets"] = functions.current_assets(ticker=ticker,frequency='A',time=5)
    Balance_sheet["Total Assets"] = functions.total_assets(ticker=ticker, frequency='A',time=5)
    Balance_sheet["Short-term debt"] = functions.shortterm_debt(ticker=ticker,frequency='A',time=5) # This doesnt add up
    Balance_sheet["Total Current Liabilities"] = functions.total_current_liabilities(ticker=ticker,frequency='A',time=5)
    Balance_sheet["Long-term debt"] = functions.longterm_debt(ticker=ticker, frequency='A',time=5)

    Balance_sheet["Total Liabilities"] = functions.total_liabilities(ticker=ticker,frequency='A',time=5)
    Balance_sheet["Total stockholder's equity"] = functions.total_stockholder_equity(ticker=ticker,frequency='A',time=5)
    #Balance_sheet["Change in working Capital"] = functions.working_capital() # This is an optional field in the DCF implement if you have time

    return Balance_sheet

def populate_DCF(DCF_Data):
    Base_Case_sheet = DCF_file.get_sheet_by_name("Base Case")

    for data in range(0, len(DCF_Data)): # For how every many financial metrics you have (17)*
        counter = 0
        for col in Base_Case_Excel_Col: #Go through the 5 columns
            # print "DCF data:    ", DCF_Data_Keys[data]
            # print "counter:     ", counter
            Base_Case_sheet[col + Base_Case_Excel_Rows[data]] = DCF_Data[DCF_Data_Keys[data]][counter]
            # Insert the corresponding year-metric to each year column
            # It references the dictionary within the dictionary. DCF_data is the singular dict that is
            # comprised of the three previous ones. (balance, income, cashflow)

            # DCF_Data_Keys is the list of keys that is found within the Indexes through with
            # [counter] going up to 5 (num of columns) and [data] going up to number of attributes in DCF model
            # which is 17 at the moment of this writing.
            counter += 1  # Makes sure that the DCF data gets all 5 of the entries for the metric

            # Holy shit. it works.


    DCF_file.save("WSIG DCF Output.xlsx")
    Output_Gross_Income = Base_Case_sheet['F4'].value - Base_Case_sheet['F5'].value
    Output_Operating_Income = Output_Gross_Income - Base_Case_sheet['F7'].value
    Output_Net_Income = Base_Case_sheet['F9'].value - Base_Case_sheet['F10'].value + Base_Case_sheet['F11'].value

    # Checking to see if the calculated cells in the output file match the official numbers from morning star

    if Output_Gross_Income >= (functions.gross_income(ticker=ticker,frequency='A',time=1)[0]+2) or Output_Gross_Income <= (functions.gross_income(ticker=ticker,frequency='A',time=1)[0]-2):
        # print "BASE CASE: ", Output_Gross_Income, "CSV: ", functions.gross_income(ticker=ticker,frequency='A',time=1)[0]
        print "Error in Gross income"
    if Output_Operating_Income >= (functions.operating_income(ticker=ticker,time=1)[0]+2) or Output_Operating_Income <= (functions.operating_income(ticker=ticker,time=1)[0]-2):
        print "Error in Operating income"
    if Output_Net_Income >= (functions.net_income(ticker=ticker,frequency='A',time=1)[0]+2 or Output_Net_Income <= (functions.operating_income(ticker=ticker,time=1)[0]-2)):
        print "Error in net income"

def Automate_DCF(ticker):

    # Appends all three function dictionaries (income statement, cashflow statement, and balance sheet)
    # to one singular dict
    DCF_Data.update(get_income_statement(ticker=ticker))
    DCF_Data.update(get_cashflow_statements(ticker=ticker))
    DCF_Data.update(get_balance_sheet(ticker=ticker))
    # for key in DCF_Data:
    #     print "key: ", key, "       ", DCF_Data[key][0]


    populate_DCF(DCF_Data)


def Begin():

    # Preliminary function to set up sheets for proper automation
    Title_sheet = DCF_file.get_sheet_by_name("Title Page")
    Title_sheet['B4'] = ticker
    Title_sheet['B10'] = '9/18/2016'
    Title_sheet['B11'] = '12/18/2016'



Begin()
Automate_DCF(ticker)

