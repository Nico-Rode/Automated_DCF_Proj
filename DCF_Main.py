import functions
import openpyxl
import quandl


#****************************************READ ME***********************************

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

#**********************************************************************************


#**************************************OTHER THOUGHTS******************************

# Figure out the best way to pull all the data. Since you'll be doing one stock at a time, it feels rather inefficient
# to download the same csv files over and over again. Maybe download once and then pull the data from the excel file?
# Only disadvantage to that is that it would be more low level and dealing with openpyxl functionality which is tough

# Also need to figure out a way to deal with modularity and flexibility. By these I mean what happens when the rows
# don't exactly match the ones in your array. What happens when the numbers don't add up or a stock doesn't label their
# data the exact same as you have it. This will take a lot of trial and error, try and except blocks. You also thought
# about using either the row #, or the attribute name as it appears in the excel file as keys for the dictionary.
# If you pair the attribute name and then continue with the low level approach of working down with the excel file,
# I think that it would absolutely ensure accuracy when placing the data, even if the row and column NUMBERS change.



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
DCF_Data_Keys = ["Revenue","COGS","SG&A","Income before taxes","Provision for income expense","Other income expense","Depreciation_and_amort","CAPEX","Inventories","Short Term Investments","Current Assets","Total Assets","Short-term debt","Total Current Liabilities","Long-term debt","Total Liabilities",
                 "Total stockholder's equity"]
#**************************************************************************


#**************************Income statement metrics for DCF************************
#array of current financial metrics, right now only contains Income statement elements
DCF_Data = {}
#***********************************************************************************


#**************************INPUTTING DATA FOR INCOME STATMENT ON BASECASE************************
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


def get_cashflow_statements(ticker):
    Cashflow_statement = {}

    Cashflow_statement["Depreciation_and_amort"] = functions.depreciation_amort_expense(ticker=ticker,frequency='A',time=5)
    Cashflow_statement["CAPEX"] = functions.capital_expenditures(ticker=ticker,frequency='A',time=5)

    return Cashflow_statement

def get_income_statement(ticker):
    Income_statement = {}

    Income_statement["Revenue"] = functions.revenue(ticker=ticker, time=5)
    Income_statement["COGS"] = functions.cost_of_goods(ticker=ticker, frequency="A", time=5)
    Income_statement["SG&A"] = functions.sales_administrative_expense(ticker=ticker, frequency="A", time=5)
    Income_statement["Income before taxes"] = functions.income_before_taxed(ticker=ticker, frequency="A", time=5)
    Income_statement["Provision for income expense"] = functions.provision_for_income_expense(ticker=ticker, frequency="A", time=5)
    Income_statement["Other income expense"] = functions.other_income_expense(ticker=ticker, frequency="A", time=5)

    return Income_statement

def get_balance_sheet(ticker):
    Balance_sheet = {}

    Balance_sheet["Inventories"] = functions.inventories(ticker=ticker, frequency='A',time=5)
    Balance_sheet["Short Term Investments"] = functions.short_term_investments(ticker=ticker,frequency='A',time=5) # doesn't include cash, might not match up with 10k output
    Balance_sheet["Current Assets"] = functions.current_assets(ticker=ticker,frequency='A',time=5) # No idea if this works, check 'BS'
    Balance_sheet["Total Assets"] = functions.total_assets(ticker=ticker, frequency='A',time=5)
    Balance_sheet["Short-term debt"] = functions.shortterm_debt(ticker=ticker,frequency='A',time=5) #Again, this is just short term debt, doesn't include long term portion
    Balance_sheet["Total Current Liabilities"] = functions.total_current_liabilities(ticker=ticker,frequency='A',time=5)
    Balance_sheet["Long-term debt"] = functions.longterm_debt(ticker=ticker, frequency='A',time=5) #Not sure if this is the actual TOTAL long term debt

    Balance_sheet["Total Liabilities"] = functions.total_liabilities(ticker=ticker,frequency='A',time=5) #DCF calls for the combination of these two? Just double check
    Balance_sheet["Total stockholder's equity"] = functions.total_stockholder_equity(ticker=ticker,frequency='A',time=5) # and make sure that the numbers add up
    #Balance_sheet["Change in working Capital"] = functions.working_capital() # This is an optional field in the DCF implement if you have time

    print Balance_sheet



    return Balance_sheet

def populate_DCF(DCF_Data):

    DCF_file = openpyxl.load_workbook(filename="WSIG DCF Template.xlsx")
    Base_Case_sheet = DCF_file.get_sheet_by_name("Base Case")

    for data in range(0, len(DCF_Data)): #For how every many financial metrics you have
        counter = 0
        for col in Base_Case_Excel_Col: #Go through the 5 columns
            # print "DCF data:    ", DCF_Data_Keys[data]
            # print "counter:     ", counter
            Base_Case_sheet[col + Base_Case_Excel_Rows[data]] = DCF_Data[DCF_Data_Keys[data]][counter] #Insert the corresponding year-metric to each year column
            counter = counter + 1 #Makes sure that the DCF data gets all 5 of the entries for the metric

            #HOLY FUCKING SHIT THIS WORKS

    DCF_file.save("WSIG DCF Output.xlsx")


def Automate_DCF(ticker):
    DCF_Data.update(get_income_statement(ticker=ticker))
    DCF_Data.update(get_cashflow_statements(ticker=ticker))
    DCF_Data.update(get_balance_sheet(ticker=ticker))
    # for key in DCF_Data:
    #     print "key: ", key, "       ", DCF_Data[key][0]


    populate_DCF(DCF_Data)




Automate_DCF(ticker)