import pandas as pd
import mysql.connector 

# mydbcon = mysql.connector.connect(host="localhost", user="debian-sys-maint", passwd="l6KEBLJ7nuBSaZ0U", database="test")
# mycursor = mydbcon.cursor()
# mycursor.execute("select * from student")

# # Then you can consume your data in a for loop
# for i in mycursor:
#     print(i)

df = pd.read_csv('/media/y0ch3n/Data/School/Data Science/HW02/STOCK_DAY_06.csv')
df1 = df.iloc[:,0:8]
print(df1)
# print(df.loc[datas[1:3]])

