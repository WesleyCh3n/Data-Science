import pandas as pd
import numpy as np


df = pd.read_csv('/Users/YoChen/Documents/GitHub/Data-Science/totalStock.csv')
df = df.iloc[:,1:9].copy()

df_np = df.to_numpy()

df_npNew = np.c_[df_np[:,1].astype(int),\
abs(df_np[:,6].astype(np.float64)-df_np[:,3].astype(np.float64)),\
abs(df_np[:,4].astype(np.float64)-df_np[:,5].astype(np.float64))]
avg = np.average(df_npNew, axis=0)
std = np.std(df_npNew, axis=0)
df_npNorm = (df_npNew-avg)/std

avg = np.average(df_npNorm, axis=0)

df_npL2 = ((df_npNorm-avg)**2).sum(axis=1)
df_npL2 = np.sqrt(df_npL2)
date = df_npL2.argsort()[-5:]
print(df.loc[[date[4],date[3],date[2],date[1],date[0]], 'Date'])