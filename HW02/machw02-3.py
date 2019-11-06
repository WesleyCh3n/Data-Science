import pandas as pd
import numpy as np
import mysql.connector 
from sqlalchemy import create_engine
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_colwidth', 1000)
df = pd.read_csv('/Users/YoChen/Documents/GitHub/Data-Science/totalStock.csv')
df = df.iloc[:,1:9].copy()
df1 = df.iloc[:,4]
df2 = df.iloc[:,1]
x = 0
x2 = 0
y = 0
y2 = 0
for i in range(len(df1.index)):
	if i <= (len(df1.index)-2):
		if abs(df1[i+1]-df1[i]) > x:
			x = abs(df1[i+1]-df1[i])
			index = i+1
		if abs(df2[i+1]-df2[i]) > x2:
			x2 = abs(df2[i+1]-df2[i])
			index2 = i+1
		if abs(df1[i+1]-df1[i])/df1[i] > y:
			y = abs(df1[i+1]-df1[i])/df1[i]
			index3 = i+1
		if abs(df2[i+1]-df2[i])/df2[i] > y2:
			y2 = abs(df2[i+1]-df2[i])/df2[i]
			index4 = i+1
		else: continue
print("By absolute amount, the biggest daily change of Highest daily price is",df.iloc[index,0],", which is",x)
print("By absolute amount, the biggest daily change of Daily trade volume is",df.iloc[index2,0],", which is",x2)
print("By percentage, the biggest daily change of Highest daily price is",df.iloc[index3,0],", which is",y)
print("By percentage, the biggest daily change of Daily trade volume is",df.iloc[index4,0],", which is",y2)

