import pandas as pd

d1 = {'Name': ['Pankaj', 'Meghna', 'Lisa'], 'Country': ['India', 'India', 'USA'], 'Role': ['CEO', 'CTO', 'CTO']}

df1 =pd.DataFrame(d1)

print('DataFrame 1:\n', df1)

df2 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Pankaj', 'Anupam', 'Amit']})

print('DataFrame 2:\n', df2)

df_merged = df1.merge(df2) 
print('Result:\n', df_merged)

