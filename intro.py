import pandas as pd

df = pd.read_csv('pokemon_data.csv')
# print(df.head(3))

df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx.head(3))

df_txt = pd.read_csv('pokemon_data.txt',delimiter='\t')

#print(df_txt.head(3))

#Read Headers of the file

#print(df.columns)

#Read Each Column for example select names of the pokemon

#print(df['Name','Type1','HP'])
#print(df.Name)


'''READ EACH ROW'''
#print(df.head(4))
#print(df.iloc[1])
#print(df.iloc[0:4])
'''
for index,row in df.iterrows():
    print(index,row['Name'])

'''
#print(df.loc[df['Type 1'] == 'Fire'])

'''Read a specific location (R,C)'''


print(df.iloc[2,1])






