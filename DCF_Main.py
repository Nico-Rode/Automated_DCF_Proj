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



#**************************Income statement metrics************************
Revenue = functions.revenue(ticker=ticker,time=5)
COGS = functions.cost_of_goods(ticker=ticker, frequency="A", time= 5)
SG_A = functions.sales_administrative_expense(ticker=ticker, frequency="A", time=5)
Income_before_taxes = functions.income_before_taxed(ticker=ticker,frequency="A", time=5)
Provision_for_income_expense = functions.provision_for_income_expense(ticker=ticker, frequency="A", time=5)
Other_income_expense = functions.other_income_expense(ticker=ticker, frequency="A", time=5)
#***************************************************************************


#**************************BASE CASE ROWS & COLUMNS************************
Base_Case_Excel_Rows = ['4','5','7','9','10','11'] #Relevant rows that need inputs on Base Case sheet
Base_Case_Excel_Col = ['F','E','D','C','B'] #Relevant columns that need inputs on Base Case sheet
#**************************************************************************


#**************************Income statement metrics for DCF************************
#array of current financial metrics, right now only contains Income statement elements
DCF_Data = [Revenue,COGS,SG_A,Income_before_taxes,Provision_for_income_expense,Other_income_expense]
#***********************************************************************************



#**************************INPUTTING DATA FOR INCOME STATMENT ON BASECASE************************
DCF_file = openpyxl.load_workbook(filename="WSIG DCF Template.xlsx")
Base_Case_sheet = DCF_file.get_sheet_by_name("Base Case")

for data in range(0, len(DCF_Data)): #For how every many financial metrics you have
    counter = 0
    for col in Base_Case_Excel_Col: #Go through the 5 columns
        Base_Case_sheet[col + Base_Case_Excel_Rows[data]] = DCF_Data[data][counter] #Insert the corresponding year-metric to each year column
        counter = counter + 1 #Makes sure that the DCF data gets all 5 of the entries for the metric

DCF_file.save("WSIG DCF Output.xlsx")

#*****************************************************************************************************






