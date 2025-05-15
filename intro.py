import pandas as pd

df = pd.read_csv('pokemon_data.csv')
# print(df.head(3))

df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(3))

df_txt = pd.read_csv('pokemon_data.txt',delimiter='\t')

#print(df_txt.head(3))

#Read Headers of the file

print(df.columns)


