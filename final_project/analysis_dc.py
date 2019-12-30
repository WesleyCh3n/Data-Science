import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# regression
def reg(x, y):
    coeff = np.polyfit(x, y, 1)
    arg1, arg2 = coeff
    line = x * arg1 + arg2
    return line, f'y = {int(arg1)}x + {int(arg2)}'

# import data
df = pd.read_csv('./DC.csv')
dc = df.to_numpy()
print(df.columns)   # show the columns name
print(f'Total {dc.shape[0]} data')

# preprocessing data / normalize
# ['instant', 'dteday', 'season', 'yr', 'mnth', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']
dc_cnt = dc[:, 16].flatten().astype(float)
dc_t1 = dc[:, 10].flatten().astype(float)
dc_t1 = (dc_t1 - dc_t1.min()) / (dc_t1.max() - dc_t1.min())
dc_t2 = dc[:, 11].flatten().astype(float)
dc_t2 = (dc_t2 - dc_t2.min()) / (dc_t2.max() - dc_t2.min())
dc_hum = dc[:, 12].flatten().astype(float)
dc_hum = dc_hum/dc_hum.max()
dc_wind = dc[:, 13].flatten().astype(float)
dc_wind = dc_wind/dc_wind.max()
dc_weather = dc[:, 9].flatten().astype(int)
dc_holiday = dc[:,6].flatten().astype(int)
dc_weekend = dc[:,8].flatten().astype(int)
dc_season = dc[:,2].flatten().astype(int)

normData = np.c_[dc_cnt, dc_t1, dc_t2, dc_hum, dc_wind, dc_weather, dc_holiday, dc_weekend, dc_season]
print(normData.shape)
# np.savetxt('norm.csv', normData, delimiter=',')

# Show plot
name = ['Temperature', 'Feeling Temperature', 'Humidity', 'Wind Speed', 'Weather', 'Season']
color = ['#2af423', '#ff7400', '#e300ff', '#1eb5ff', '#94b1ee', '#660066']
dc_data = [dc_t1, dc_t2, dc_hum, dc_wind, dc_weather, dc_season]
fig = plt.figure(figsize=[12.5, 7])
for i in range(6):
    trend_line, text = reg(dc_data[i], dc_cnt)
    ax = fig.add_subplot(2, 3, i+1)
    ax.scatter(dc_data[i], dc_cnt, c = color[i], s = 2, alpha = 0.3)    # plot data
    ax.scatter(dc_data[i], trend_line, c = 'r', s = 2, alpha = 1)       # plot line
    ax.text(0.03, 0.95, text, fontname = 'Arial', fontsize = 10, weight='bold', transform=ax.transAxes, va='top')
    ax.set_title(name[i])
plt.show()
