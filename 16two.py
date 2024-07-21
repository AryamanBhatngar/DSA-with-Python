import pandas as pd

data1 = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'], 'Age': [27, 24, 22, 32],

'Address': ['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 'Qualification': ['Msc', 'MA', 'MCA', 'Phd']}

df = pd.DataFrame (data1, index=[0, 1, 2,3])

print(df)
gk df.groupby('Age')
gk.first()