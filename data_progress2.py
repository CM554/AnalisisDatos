import pandas as pd
import datetime

df = pd.read_csv('pipol_dataset.csv')

df['birthday'] = pd.to_datetime(df['birthday'], dayfirst=True)

df['age'] = 2026 - df['birthday'].dt.year

print(df[['name', 'birthday', 'age']].head())

group_country = df.groupby('country')
 
promedio_edades = group_country['age'].mean()

print("Edad promedio por país:")
print(promedio_edades)