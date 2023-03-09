import pandas as pd

# task 1

L = [5, 10, 15, 20, 25]
ds = pd.Series(L)
print(ds)

# task 2

d = {
    'col1': [1, 2, 3, 4, 7, 11],
    'col2': [4, 5, 6, 9, 5, 0],
    'col3': [7, 5, 8, 12, 1, 11]
}
ds = pd.DataFrame(d)
s1 = ds.iloc[:, 0]
print('1st column as a Series')
print(s1)
print(type(s1))

# task 3

dp = pd.read_csv('data.csv')
print(dp.head(20))

# task 4

for i,j in dp.iterrows():
    print(i,j)