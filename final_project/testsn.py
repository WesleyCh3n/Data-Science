import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv('./london.csv')
Ld = df.to_numpy()
print(df.columns)   # show the columns name
print(f'Total {Ld.shape[0]} data')

df['t1'] = (df['t1'] - df['t1'].min()) / (df['t1'].max() - df['t1'].min())
df['t2'] = (df['t2'] - df['t2'].min()) / (df['t2'].max() - df['t2'].min())
df['hum'] = df['hum'] / df['hum'].max()
df['wind_speed'] = df['wind_speed'] / df['wind_speed'].max()
df.to_csv('normal.csv', index=False)

sn.set(color_codes=True)
fig, axs = plt.subplots(2, 3)
name = ['t1', 't2', 'hum', 'wind_speed', 'weather_code', 'season']
for i in range(2):
    for j in range(3):
        chart = sn.regplot(name[2*i+j], 'cnt', df, scatter_kws={'s': 5, 'alpha':0.3}, line_kws={'color': 'red'}, ax=axs[i, j])
plt.show()
