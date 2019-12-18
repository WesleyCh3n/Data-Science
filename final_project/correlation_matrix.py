import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import data
df = pd.read_csv('./london.csv')
df2 = pd.read_csv('./DC.csv')
Ld = df.to_numpy()
DC = df2.to_numpy()
print(df.columns)   # show the columns name
print(f'Total {Ld.shape[0]} data')

sel = df.iloc[:,1:]
coeffs = sel.corr().to_numpy()
print(coeffs.shape)
# pd.plotting.scatter_matrix(sel)
plt.matshow(sel.corr(), cmap='seismic')
plt.xticks(range(len(sel.columns)), sel.columns, rotation = 45, ha="left", va="center",rotation_mode="anchor")
plt.yticks(range(len(sel.columns)), sel.columns)#, ha="center", va="center",rotation_mode="anchor")
for (i, j), value in np.ndenumerate(coeffs):
    plt.text(i, j, f'{value:.2f}', ha='center', va='center')
extent = [0.5 , 10, 0.5, 10]
plt.colorbar()
plt.show()
