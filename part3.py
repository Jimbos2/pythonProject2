import pandas as pd
import numpy as np

df = pd.read_csv('finance_liquor_sales.csv')
""""
#print(df.head())  # top 5 rows
#print(df.tail())  # last 5 rows
#print(df.info())
#print(df.shape)  # number of rows and columns
"""
mean = df.mean(numeric_only=True)
print(mean)

median = df.median(numeric_only=True)
print(median)

max_v = df.max(numeric_only=True)
print(max_v)

summary = df.describe()
print(summary)

cn = df.groupby('category_name')
print(cn.first())

cnc = df.groupby(['category_name','city'])
print(cnc.first())

sdf = df.groupby('category_name')
print(sdf.aggregate(np.sum))

sdf2 = df.groupby(['category_name', 'city'])
print(cnc.agg({'bottles_sold':'sum', 'sale_dollars':'mean'}))

ng = df.groupby('vendor_name')
print(ng.filter(lambda x: len(x) >= 20))
