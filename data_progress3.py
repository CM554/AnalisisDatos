import pandas as pd
df = pd.read_csv('pipol_dataset (2).csv')
df['birthday'] = pd.to_datetime(df['birthday'], format='%d/%m/%Y', errors='coerce')
df['age'] = (pd.to_datetime('today') - df['birthday']).dt.days // 365

grupos_multinivel = df.groupby(['country', 'city'])
mexico_dusty = grupos_multinivel.get_group(('Mexico', 'Dusty City'))
print("--- Personas en Dusty City, Mexico ---")
print(mexico_dusty[['name', 'last_name', 'country', 'city', 'age']].head())
promedio_agg = df.groupby('country').agg({'age': 'mean'})
promedio_directo = df.groupby('country')['age'].mean()
print("\n--- Edad promedio por país usando .agg() ---")
print(promedio_agg)