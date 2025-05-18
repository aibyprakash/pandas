import pandas as pd

#Import pokemone dataset
df = pd.read_csv("pokemon_data.csv")

new_df = df.loc[(df['Type 1']=='Grass' ) & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
#print(new_df.head(2))
#new_df.to_csv('filterd.csv')

#reset index in dataframe
#new_df=new_df.reset_index(drop=True)

#Use inplace to save memmory if inplca true ,it save changes in the df

new_df.reset_index(drop=True,inplace=True)


print(new_df)
