import pandas as pd
import re

df = pd.read_csv('modified.csv')

dfg=df.groupby(['Type 1']).mean(numeric_only=True).sort_values('Defense',ascending=False)
print(dfg)