import pandas as pd
import re 
df = pd.read_csv("pokemon_data.csv")
#df_mega=df.loc[df['Name'].str.contains('Mega')] #Fetch data with name Mega
#dfNoMega=df.loc[~df['Name'].str.contains('Mega')] #Fetch all names not include Mega


type1=df.loc[df['Type 1'].str.contains('Fire|Grass',flags=re.I,regex = True)] #Fetch data with name Mega
#print(df)
names_starts_w_pi=df.loc[df['Name'].str.contains('^pi[a-z]*',flags=re.I,regex = True)] #Fetch data with name Mega
#print(names_starts_w_pi)

#Conditional changes

#df.loc[df['Type 1']=='Flamer','Type 1'] = 'Fire'
#print(df)

#df.loc[df['Type 1'] == 'Fire','Legendary'] = True

''' Load modified data '''
df = pd.read_csv('modified.csv')
df.loc[df['Total'] > 500,['Generation','Legendary']]=['Test1','Test2']
df.to_csv('modified.csv')
print(df)