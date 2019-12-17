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
df = pd.read_csv('./london.csv')
df2 = pd.read_csv('./DC.csv')
Ld = df.to_numpy()
DC = df2.to_numpy()
print(df.columns)   # show the columns name
print(f'Total {Ld.shape[0]} data')

# preprocessing data / normalize
Ld_cnt = Ld[:, 1].flatten().astype(float)
Ld_t1 = Ld[:, 2].flatten().astype(float)
Ld_t1 = (Ld_t1 - Ld_t1.min()) / (Ld_t1.max() - Ld_t1.min())
Ld_t2 = Ld[:, 3].flatten().astype(float)
Ld_t2 = (Ld_t2 - Ld_t2.min()) / (Ld_t2.max() - Ld_t2.min())
Ld_hum = Ld[:, 4].flatten().astype(float)
Ld_hum = Ld_hum/Ld_hum.max()
Ld_wind = Ld[:, 5].flatten().astype(float)
Ld_wind = Ld_wind/Ld_wind.max()
Ld_weather = Ld[:, 6].flatten().astype(int)
Ld_holiday = Ld[:,7].flatten().astype(int)
Ld_weekend = Ld[:,8].flatten().astype(int)
Ld_season = Ld[:,9].flatten().astype(int)

# Show plot
name = ['Temperature', 'Feeling Temperature', 'Humidity', 'Wind Speed', 'Weather', 'Season']
color = ['#2af423', '#ff7400', '#e300ff', '#1eb5ff', '#94b1ee', '#660066']
Ld_data = [Ld_t1, Ld_t2, Ld_hum, Ld_wind, Ld_weather, Ld_season]
fig = plt.figure(figsize=[12.5, 7])
for i in range(6):
    trend_line, text = reg(Ld_data[i], Ld_cnt)
    ax = fig.add_subplot(2, 3, i+1)
    ax.scatter(Ld_data[i], Ld_cnt, c = color[i], s = 2, alpha = 0.3)    # plot data
    ax.scatter(Ld_data[i], trend_line, c = 'r', s = 2, alpha = 1)       # plot line
    ax.text(0.03, 0.95, text, fontname = 'Arial', fontsize = 10, weight='bold', transform=ax.transAxes, va='top')
    ax.set_title(name[i])
plt.show()
