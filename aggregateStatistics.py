import pandas as pd

df = pd.read_csv('modified.csv')

df.groupby(['Type 1']).mean()
print(df)