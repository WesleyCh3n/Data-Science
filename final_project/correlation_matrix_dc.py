import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

# import data
df = pd.read_csv('./london.csv')
df2 = pd.read_csv('./DC.csv')
Ld = df.to_numpy()
DC = df2.to_numpy()
print(df.columns)   # show the columns name
print(f'Total {Ld.shape[0]} data')

sel = df2.iloc[:,1:]
coeffs = sel.corr().to_numpy()
print(coeffs.shape)
matrix = sel.corr()
chart = sn.heatmap(matrix, annot=True, cmap='seismic')
chart.set_xticklabels(sel.columns, rotation=40)
# pd.plotting.scatter_matrix(sel)
plt.show()
