import pandas as pd

d1 = {
    'Name': ['Mary','John', 'Alice', 'Bob'],
    'Age': [27, 24, 22, 32],
    'Position': ['Data Analyst', 'Trainee', 'QA Tester', 'IT']
}
d2 = {
    'Name': ['Steve', 'Tom', 'Jenny', 'Nick'],
    'Age': [37, 25, 24, 52],
    'Position': ['IT', 'Data Analyst', 'Consultant', 'IT']
}

df1 = pd.DataFrame(d1,index=[0,1,2,3])
df2 = pd.DataFrame(d2,index=[4,5,6,7])
result = pd.concat([df1, df2])
print(result)

d1 = {
    'key': ['a', 'b', 'c', 'd'],
    'Name': ['Mary', 'John', 'Alice', 'Bob']
}
d2 = {
    'key': ['a', 'b', 'c', 'd'],
    'Age': [27, 24, 22, 32]
}
df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)
result = pd.merge(df1, df2, on='key')
print(result)

d1 = {
    'Name': ['Mary', 'John', 'Alice', 'Bob'],
    'Age': [27, 24, 42, 32]
}
d2 = {
    'Position': ['Data Analyst', 'Trainee', 'QA Tester', 'IT'],
    'Years_of_experience':[5, 1, 10, 3]
}
df1 = pd.DataFrame(d1, index=[0, 1, 2, 3])
df2 = pd.DataFrame(d2, index=[0, 2, 3, 4])
result = df1.join(df2, how='inner')
print(result)