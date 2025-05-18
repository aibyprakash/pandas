import pandas as pd
df = pd.read_csv("pokemon_data.csv")
df_mega=df.loc[df['Name'].str.contains('Mega')] #Fetch data with name Mega
dfNoMega=df.loc[~df['Name'].str.contains('Mega')] #Fetch all names not include Mega
print(dfNoMega)