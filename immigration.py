from __future__ import print_function
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

df_can = pd.read_excel(
    '/Users/leandro998/Downloads/Data Visualization with Python - IBM/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2
)

pd.set_option('display.width', 320) # extends the standard size of 80
pd.set_option('display.max_columns', 100) # extends the standard number of columns
# print(df_can.head())

# define a style:
matplotlib.style.use(['ggplot'])

df_can['Total'] = df_can.sum(axis=1)
# set column OdName as index:
df_can.rename(columns={'OdName': 'Country'}, inplace=True)
df_can.set_index('Country', inplace=True)
# convert the columns into string:
df_can.columns = list(map(str, df_can.columns))
years = list(map(str, range(1980, 2014)))
# create a filter of the country:
# haiti = df_can.loc['Haiti', years]
# print(haiti)
# haiti.plot() # >> automatic plotting

# let's change the index values of Haiti to type integer for plotting
# haiti.index = haiti.index.map(int)
# haiti.plot(kind='line')
# plt.title('Immigration from Haiti')
# plt.ylabel('Number of immigrants')
# plt.xlabel('Years')
# plt.text(2000, 6000, '2010 Earthquake') # see note on the figure
# plt.legend()
# plt.show()

# Top 5:
# df_top5 = df_can.sort_values(by='Total', ascending=False, axis=0).head(5)
# df_top5 = df_top5[years].transpose()
# df_top5.plot(kind='line')
# plt.show()

# Bar chart, do not transpose:
# top5_countries = df_top5.head(5)
# bar: ascending=False; barh: ascending=True
# top5_countries = top5_countries.sort_values(by='Total', ascending=True, axis=0)
# top5_countries['Total'].plot(kind='barh')
# plt.show()
# print(top5_countries)

# Histogram:
# df_sort = df_can.sort_values(by='Total', ascending=False, axis=0)
# df_sort = df_sort['Total']
# df_sort.plot(kind='hist')
# plt.show()

# box for boxplot
# df_brazil = df_can.loc[['Brazil'], years].transpose()
# df_brazil.plot(kind='box')
# plt.title('Box plot of Brazilian Immigrants from 1980 - 2013')
# plt.ylabel('Number of Immigrants')
# plt.show()

# area for area plots
# df_top5 = df_can.sort_values(by='Total', ascending=False, axis=0).head(5)
# df_top5 = df_top5[years].transpose()
# df_top5.plot(kind='area')
# plt.show()

# Pie for pie plots
# colors_list = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgreen', 'pink']
# explode_list = [0.1, 0, 0, 0, 0.1, 0.1] # ratio for each continent with which to offset each wedge.
# df_continents = df_can.groupby('AreaName', axis=0).sum()
# df_continents['Total'].plot(kind='pie',
#                             autopct='%1.1f%%',
#                             startangle=90,
#                             shadow=False, # false is default
#                             labels=None,
#                             pctdistance=1.12, # removes the values from the inside to the outside chart
#                             colors=colors_list,
#                             explode=explode_list)
# plt.title('Immigration to Canada by Continent [1980 - 2013]', y=1.12)
# plt.axis('equal') # Sets the pie chart to look like a circle.
# plt.legend(labels=df_continents.index, loc='upper left')
# plt.show()

# scatter for scatter plots
# df_total = pd.DataFrame(df_can[years].sum(axis=0))
# df_total.index = map(int, df_total.index)
# df_total.reset_index(inplace=True)
# df_total.columns = ['year', 'total']
# df_total.plot(kind='scatter',
#               x='year',
#               y='total',
#               figsize=(10, 6),
#               color='darkblue')
# input a tendency line:
# plt.title('Total Immigration to Canada from 1980 - 2013')
# plt.xlabel('Year')
# plt.ylabel('Number of Immigrants')
# x = df_total['year']
# y = df_total['total']
# fit = np.polyfit(x, y, deg=1)
# plt.plot(x, fit[0] * x + fit[1], color='red') # recall that x is the Years
# plt.annotate('y={0:.0f} x + {1:.0f}'.format(fit[0], fit[1]), xy=(2000, 150000)) # text
# plt.show()
# print('No. Immigrants = {0:.0f} * Year + {1:.0f}'.format(fit[0], fit[1])) # print to console

# Bubble Plots (scatter plot + 1 variable)
# df_can_t = df_can[years].transpose()
# df_can_t.index = map(int, df_can_t.index)
# df_can_t.index.name = 'Year'
# df_can_t.reset_index(inplace=True)
# # normalize Brazil data
# norm_brazil = (df_can_t['Brazil'] - df_can_t['Brazil'].min()) \
#               / (df_can_t['Brazil'].max() - df_can_t['Brazil'].min())
# # normalize Argentina data
# norm_argentina = (df_can_t['Argentina'] - df_can_t['Argentina'].min()) \
#                  / (df_can_t['Argentina'].max() - df_can_t['Argentina'].min())
# # Brazil
# ax0 = df_can_t.plot(kind='scatter',
#                     x='Year',
#                     y='Brazil',
#                     figsize=(14, 8),
#                     alpha=0.5,  # transparency
#                     color='green',
#                     s=norm_brazil * 2000 + 10,  # pass in weights
#                     xlim=(1975, 2015)
#                    )
#
# # Argentina
# ax1 = df_can_t.plot(kind='scatter',
#                     x='Year',
#                     y='Argentina',
#                     alpha=0.5,
#                     color="blue",
#                     s=norm_argentina * 2000 + 10,
#                     ax=ax0
#                    )
# ax0.set_ylabel('Number of Immigrants')
# ax0.set_title('Immigration from Brazil and Argentina from 1980 - 2013')
# ax0.legend(['Brazil', 'Argentina'], loc='upper left', fontsize='x-large')
# plt.show()

# hexbin for hexbin plot

# kde or density for density plots
