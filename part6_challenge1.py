import pandas as pd
import numpy as np

data = pd.read_csv('1.supermarket.csv')

print(data.head())
print('\nShape of dataset:', data.shape)
print(data.info())


print(data.columns)

x = data.groupby('item_name')
x = x.sum()
print(x.head(1))