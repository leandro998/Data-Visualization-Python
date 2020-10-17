import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.patches as mpatches  # needed for waffle Charts
import seaborn as sns
from PIL import Image  # converting images into arrays

df_can = pd.read_excel(
    '/Users/leandro998/Downloads/Data Visualization with Python - IBM/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2
)

pd.set_option('display.width', 320) # extends the standard size of 80
pd.set_option('display.max_columns', 100) # extends the standard number of columns
# define a style:
matplotlib.style.use(['ggplot'])
# Data organization:
df_can.drop(['AREA', 'REG', 'DEV', 'Type', 'Coverage'], axis=1, inplace=True)
df_can.rename(columns={'OdName': 'Country',
                       'AreaName': 'Continent',
                       'RegName': 'Region'},
              inplace=True)
df_can.set_index('Country', inplace=True)
df_can['Total'] = df_can.sum(axis=1)
df_can.columns = list(map(str, df_can.columns))
years = list(map(str, range(1980, 2014)))

# Waffle chart:
df_dsn = df_can.loc[['Denmark', 'Norway', 'Sweden'], :]
total_values = sum(df_dsn['Total'])
category_proportions = [(float(value) / total_values) for value in df_dsn['Total']]
# Check category_proportions:
# for i, proportion in enumerate(category_proportions):
#     print(df_dsn.index.values[i] + ': ' + str(proportion))
width = 40  # width of chart
height = 10  # height of chart
total_num_tiles = width * height  # total number of tiles
tiles_per_category = [round(proportion * total_num_tiles) for proportion in category_proportions]
# Check number of squares in each country:
# for i, tiles in enumerate(tiles_per_category):
#     print(df_dsn.index.values[i] + ': ' + str(tiles))
# Create the chart:
waffle_chart = np.zeros((height, width))
category_index = 0
tile_index = 0
# populate the waffle chart
for col in range(width):
    for row in range(height):
        tile_index += 1

        # if the number of tiles populated for the current category is equal to its corresponding allocated tiles...
        if tile_index > sum(tiles_per_category[0:category_index]):
            # ...proceed to the next category
            category_index += 1

            # set the class value to an integer, which increases with class
        waffle_chart[row, col] = category_index
# print(waffle_chart)  # An array of numbers
# Create the visuals:
fig = plt.figure()
colormap = plt.cm.coolwarm
plt.matshow(waffle_chart, cmap=colormap)
plt.colorbar()
ax = plt.gca()
ax.set_xticks(np.arange(-.5, width, 1), minor=True)
ax.set_yticks(np.arange(-.5, height, 1), minor=True)
# add gridlines based on minor ticks
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
plt.xticks([])
plt.yticks([])
# compute cumulative sum of individual categories to match color schemes between chart and legend
values_cumsum = np.cumsum(df_dsn['Total'])
total_values = values_cumsum[len(values_cumsum) - 1]
# create legend
legend_handles = []
for i, category in enumerate(df_dsn.index.values):
    label_str = category + ' (' + str(df_dsn['Total'][i]) + ')'
    color_val = colormap(float(values_cumsum[i])/total_values)
    legend_handles.append(mpatches.Patch(color=color_val, label=label_str))

# add legend to chart
plt.legend(handles=legend_handles,
           loc='lower center',
           ncol=len(df_dsn.index.values),
           bbox_to_anchor=(0., -0.2, 0.95, .1)
          )
