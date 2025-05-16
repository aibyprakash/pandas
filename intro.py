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


#print(df.iloc[2,1])

'''  SORTING / DESCRIBING DATA '''
#min, max, mean, std dev

#print(df.describe())

#Sort values by name

#print(df.sort_values('Name',ascending=False))

#print(df.sort_values(['Type 1','HP'],ascending=True))
#print(df.sort_values(['Type 1','HP'],ascending=[1,0]))

'''  Making changes to the data   '''

#df['Total'] = df['HP']+df['Attack']+df['Defense']+df['Sp. Atk']+df['Sp. Def']+df['Speed']

#df = df.drop(columns=['Total'])

#df['Total'] = df.iloc[:,4:10].sum(axis=1)

cols = list(df.columns.values)
df = df[cols[0:4]+[cols[-1]]+cols[4:12]]

#df=df[['Total','HP','Defense']]

print(df.head(5))


''' Save data into csv '''

'''' df to csv '''
#df.to_csv('modified.csv',index=False)
''' df to excel file'''
#df.to_excel('modified.xlsx',index=False)
''' df to tab indented txt file'''
df.to_csv('modified.txt',index=False,sep='\t')
