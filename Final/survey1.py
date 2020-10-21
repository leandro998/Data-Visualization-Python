import numpy as np
import pandas as pd

df = pd.read_csv('/Users/leandro998/Downloads/Topic_Survey_Assignment.csv')
df.set_index('Unnamed: 0', inplace=True)
pd.set_option('display.width', 320)  # extends the standard size of 80
pd.set_option('display.max_columns', 100)  # extends the standard number of columns
print(df.head())
