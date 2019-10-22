import pandas as pd
import numpy as np

df = pd.read_csv('/Users/YoChen/Documents/GitHub/Data-Science/totalStock.csv')
dfClosingPirce = df.iloc[:,1:9].set_index('Date').loc[:,'Closing_Price'].copy()
dfSort = dfClosingPirce.sort_values()
dfMax = dfSort[(len(dfSort)-5):]
dfMin = dfSort[0:5]
dfDiff = pd.DataFrame(np.zeros((25,1)),dtype=float)
diff = []
for i in range(5):
	for j in range(5):
		dfDiff.iat[i*5+j,0] = dfMax[i]-dfMin[j]
		diff.append([dfMax.index[i],dfMin.index[j]])
dfDiff['Index'] = diff
dfDiff = dfDiff.sort_values(by=0,ascending=False).reset_index(drop=True)
Ans = dfDiff.reset_index(drop=True).loc[:4,"Index"]

print("Top 5 set is: \n\
Sell day:",Ans[0][0],"Buy day:",Ans[0][1],"Price Difference:",dfDiff.loc[:4,0][0])
print("Sell day:",Ans[1][0],"Buy day:",Ans[1][1],"Price Difference:",dfDiff.loc[:4,0][1])
print("Sell day:",Ans[2][0],"Buy day:",Ans[2][1],"Price Difference:",dfDiff.loc[:4,0][2])
print("Sell day:",Ans[3][0],"Buy day:",Ans[3][1],"Price Difference:",dfDiff.loc[:4,0][3])
print("Sell day:",Ans[4][0],"Buy day:",Ans[4][1],"Price Difference:",dfDiff.loc[:4,0][4])
