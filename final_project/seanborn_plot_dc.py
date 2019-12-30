import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn

df = pd.read_csv('./DC.csv')
Ld = df.to_numpy()
print(df.columns)   # show the columns name

'''Normalizing'''
# df['t1'] = (df['t1'] - df['t1'].min()) / (df['t1'].max() - df['t1'].min())
# df['t2'] = (df['t2'] - df['t2'].min()) / (df['t2'].max() - df['t2'].min())
# df['hum'] = df['hum'] / df['hum'].max()
# df['wind_speed'] = df['wind_speed'] / df['wind_speed'].max()

'''Change timestamp to readable datetime'''
# df['mnth'] = pd.to_datetime(df['mnth'])
# df['yr'] = pd.to_datetime(df['yr'])
# df.drop(columns =['timestamp'], inplace = True)

'''add year/month/day'''
# df['month'] = df['date'].dt.month
# df['year'] = df['date'].dt.year
# df['hr'] = df['date'].dt.hour
df = df[['yr', 'mnth', 'hr', 'cnt', 'temp', 'atemp', 'hum', 'windspeed', 'weathersit', 'holiday', 'workingday', 'season']]

'''Grading Level(/500)'''
# print(df['cnt'].max()) # 7860
# for i in range(16):
#     df.loc[(i*500 < df['cnt']) & (df['cnt'] <= (i+1)*500), 'cnt'] = i+1

# print(df)
# df.to_csv('normalize-addtime-grade.csv', index=False)

# print(df[df['month'] == 2]['cnt'].sum())
# print([df[df['month'] == (i+1)]['cnt'].sum() for i in range(12)])
# print(df[df['hr']>'19:00:00'])

'''Hour Count Distribution'''
# ax = sn.boxplot(x='hr', y='cnt', data=df)
# ax = sn.boxenplot(x='hr', y='cnt', data=df)
# plt.show()

'''Monthly Count Distribution'''
# ax = sn.violinplot(x='mnth', y='cnt', data=df)
# plt.show()

'''Year Count Distribution'''
ax = sn.boxplot(x='yr', y='cnt', data=df)
plt.show()

'''Correlation'''
# sn.set(color_codes=True)
# fig, axs = plt.subplots(2, 3)
# name = ['t1', 't2', 'hum', 'wind_speed', 'weather_code', 'season']
# for i in range(2):
#     for j in range(3):
#         chart = sn.regplot(name[2*i+j], 'cnt', df, scatter_kws={'s': 5, 'alpha':0.3}, line_kws={'color': 'red'}, ax=axs[i, j])
# plt.show()
