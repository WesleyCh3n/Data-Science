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

df['date'] = pd.to_datetime(df['timestamp'])
df.drop(columns =['timestamp'], inplace = True)
df = df[['date', 'cnt', 't1', 't2', 'hum', 'wind_speed', 'weather_code', 'is_holiday', 'is_weekend', 'season']]
print(df)

'''add year/month/day'''
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year
df['hr'] = df['date'].dt.hour
print(df)

# print(df[df['month'] == 2]['cnt'].sum())
# print([df[df['month'] == (i+1)]['cnt'].sum() for i in range(12)])
# print(df[df['hr']>'19:00:00'])

'''Hour Count Distribution'''
# ax = sn.boxplot(x='hr', y='cnt', data=df)
ax = sn.boxenplot(x='hr', y='cnt', data=df)
plt.show()

'''Monthly Count Distribution'''
# ax = sn.violinplot(x='month', y='cnt', data=df)
# plt.show()

'''Year Count Distribution'''
# ax = sn.boxplot(x='year', y='cnt', data=df)
# plt.show()



# sn.set(color_codes=True)
# fig, axs = plt.subplots(2, 3)
# name = ['t1', 't2', 'hum', 'wind_speed', 'weather_code', 'season']
# for i in range(2):
#     for j in range(3):
#         chart = sn.regplot(name[2*i+j], 'cnt', df, scatter_kws={'s': 5, 'alpha':0.3}, line_kws={'color': 'red'}, ax=axs[i, j])
# plt.show()
