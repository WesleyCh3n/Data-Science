import pandas as pd
import mysql.connector 
from sqlalchemy import create_engine


pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 1000)
db = create_engine("mysql+mysqlconnector://root:wesley7536951@localhost/test")
conn = db.connect()
# mydbcon = mysql.connector.connect(host="localhost", user="root", passwd="wesley7536951", database="test")
# mycursor = mydbcon.cursor()
# mycursor.execute("select * from student")

# for i in mycursor:
#     print(i)
dflist = []
dflist.append(pd.read_csv('/Users/YoChen/Documents/GitHub/Data-Science/STOCK_DAY_06.csv',thousands=','))
dflist.append(pd.read_csv('/Users/YoChen/Documents/GitHub/Data-Science/STOCK_DAY_07.csv',thousands=','))
dflist.append(pd.read_csv('/Users/YoChen/Documents/GitHub/Data-Science/STOCK_DAY_08.csv',thousands=','))
dflist.append(pd.read_csv('/Users/YoChen/Documents/GitHub/Data-Science/STOCK_DAY_09.csv',thousands=','))
dflist.append(pd.read_csv('/Users/YoChen/Documents/GitHub/Data-Science/STOCK_DAY_10.csv',thousands=','))
dflist[0] = dflist[0].iloc[:,0:8].copy()

for i in range(len(dflist)-1):
	dflist[i+1] = dflist[i+1].iloc[:,0:8].copy()
	dflist[0] = dflist[0].append(dflist[i+1], ignore_index=True)

df = dflist[0]
df.iloc[:,1:3].astype('int')
print(df)
print(df.head())
print(df.describe())

# df.to_csv(r'/Users/YoChen/Documents/GitHub/Data-Science/totalStock.csv')
# print(df.describe())
# print(df)
# df.to_sql('stockdata', db)
# s = text("select avg(Trade_Volume) from stockdata")
# result = conn.execute("select avg(Trade_Volume) from stockdata")
# for i in result:
# 	print(str(i))