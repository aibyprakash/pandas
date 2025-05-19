import pandas as pd
import re

df = pd.read_csv('modified.csv')

dfg=df.groupby(['Type 1']).mean(numeric_only=True).sort_values('Attack',ascending=False)
dfSum = df.groupby(['Type 1']).sum()
df['count']= 1
#dfcount = df.groupby(['Type 1']).count()['count']
dfcount = df.groupby(['Type 1','Type 2']).count()['count']
print(dfcount)


# Working with largeamounts of data
new_df = pd.DataFrame(columns=df.columns)
for df in pd.read_csv('modified.csv',chunksize=5):
    results = df.groupby(['Type 1']).count()

    new_df = pd.concat([new_df,results])