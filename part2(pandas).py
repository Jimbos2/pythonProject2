import pandas as pd
import numpy as np

x = [23, 48, 19]
my_first_series = pd.Series(x)
print(my_first_series)

data = {
    "students": ['Emma', 'John', 'Bob'],
    "grades": [12, 18, 17]
}
first_data_frame = pd.DataFrame(data)
print(first_data_frame)
print(first_data_frame['students'])

first_data_frame = pd.DataFrame(data, index=["a", "b", "c"])
first_row = first_data_frame.loc["a"]
print(first_row)

second_row = first_data_frame.iloc[1]
print(second_row)

data = {
    "students": ['Emma', 'John', np.nan, 'Bob'],
    "grades": [12, np.nan, 18, 17]
}
first_data_frame = pd.DataFrame(data, index=["a", "b", "c", "d"])
print(first_data_frame.isnull())

first_data_frame["students"].fillna('No Name', inplace = True)
first_data_frame["grades"].fillna('No Grade', inplace = True)
print(first_data_frame)

df2 = first_data_frame.replace(to_replace='Bob', value='Alice')
print(df2)

data = {
    "students": ['Emma', 'John', "Mary", 'Bob'],
    "grades": [12, np.nan, 18, np.nan]
}
first_data_frame = pd.DataFrame(data, index=["a", "b", "c", "d"])
df = first_data_frame.interpolate(method='linear', limit_direction='forward')
print(df)

first_data_frame.dropna(inplace= True)
print(first_data_frame)

s = pd.Series(['workearly', 'e-learning', 'python'])
for index, value in s.items():
    print(f"Index:{index}, Value : {value}")

data = {
    "students": ['Emma', 'John'],
     "grades": [12, 19.8]
}
firstdf = pd.DataFrame(data, index= ['a', 'b'])
for i,j in firstdf.iterrows():
    print(i, j)
    print()

columns = list(firstdf)
for i in columns:
    print(firstdf[i][1])

