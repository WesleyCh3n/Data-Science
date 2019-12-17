import pandas as pd
import numpy as np

df = pd.read_csv('./london_merged.csv')
print(df.describe())
print(df.iloc[:,2])
print(df)
