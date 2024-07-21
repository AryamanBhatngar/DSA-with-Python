import pandas as pd
data = {
'Category': ['A', 'A', 'B', 'B', 'C', 'C', 'A', 'B', 'C', 'c'],
    'Outcome': ['Success', 'Failure', 'Success', 'Failure', 'Success', 'Failure', 'Success', 'Success', 'Failure', 'Failure']
}
df = pd.DataFrame(data)
crosstab_result = pd.crosstab(df['Category'], df['Outcome'], normalize='index') 
print(crosstab_result)