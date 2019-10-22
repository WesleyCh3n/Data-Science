import pandas as pd
import numpy as np

df = pd.read_csv('/Users/YoChen/Documents/GitHub/Data-Science/totalStock.csv')
dfClosingPirce = df.iloc[:,1:9].set_index('Date').loc[:,'Closing_Price'].copy()
dfSort = dfClosingPirce.sort_values()
dfMax = dfSort[(len(dfSort)-5):]
dfMin = dfSort[0:5]
print("Top 5 set is: \n\
Sell day:",dfMax.index[4],"Buy day:",dfMin.index[0],"Price Difference:",dfMax[4]-dfMin[0])
print("Sell day:",dfMax.index[4],"Buy day:",dfMin.index[1],"Price Difference:",dfMax[4]-dfMin[1])
print("Sell day:",dfMax.index[4],"Buy day:",dfMin.index[2],"Price Difference:",dfMax[4]-dfMin[2])
print("Sell day:",dfMax.index[4],"Buy day:",dfMin.index[3],"Price Difference:",dfMax[4]-dfMin[3])
print("Sell day:",dfMax.index[4],"Buy day:",dfMin.index[4],"Price Difference:",dfMax[4]-dfMin[4])


