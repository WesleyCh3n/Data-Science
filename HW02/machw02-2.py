import pandas as pd
import mysql.connector 
from sqlalchemy import create_engine

db = create_engine("mysql+mysqlconnector://root:wesley7536951@localhost/test")
conn = db.connect()

result = conn.execute("select sum(Trade_Value) from stockdata")
for i in result:
	print("Total Trade value is ",str(i))
result = conn.execute("select avg(Trade_Value) from stockdata")
for i in result:
	print("Average Trade value is ",str(i))
result = conn.execute("select sum(Trade_Volume) from stockdata")
for i in result:
	print("Total Trade volume is ",str(i))
result = conn.execute("select avg(Trade_Volume) from stockdata")
for i in result:
	print("Average Trade volume is ",str(i))
