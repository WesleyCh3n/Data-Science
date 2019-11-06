import pandas as pd
import mysql.connector 

# mydbcon = mysql.connector.connect(host="localhost", user="debian-sys-maint", passwd="l6KEBLJ7nuBSaZ0U", database="test")
# mycursor = mydbcon.cursor()
# mycursor.execute("select * from student")

# # Then you can consume your data in a for loop
# for i in mycursor:
#     print(i)
dflist = []
dflist.append(pd.read_csv('/media/y0ch3n/Data/School/Data Science/HW02/STOCK_DAY_06.csv'))
dflist.append(pd.read_csv('/media/y0ch3n/Data/School/Data Science/HW02/STOCK_DAY_07.csv'))
dflist.append(pd.read_csv('/media/y0ch3n/Data/School/Data Science/HW02/STOCK_DAY_08.csv'))
dflist.append(pd.read_csv('/media/y0ch3n/Data/School/Data Science/HW02/STOCK_DAY_09.csv'))
dflist.append(pd.read_csv('/media/y0ch3n/Data/School/Data Science/HW02/STOCK_DAY_10.csv'))
dflist[0] = dflist[0].iloc[:,0:8].copy()

for i in range(len(dflist)-1):
	dflist[i+1] = dflist[i+1].iloc[:,0:8].copy()
	dflist[0] = dflist[0].append(dflist[i+1], ignore_index=True)

df = dflist[0]
print(df)