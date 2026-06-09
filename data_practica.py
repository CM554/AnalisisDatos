import pandas as pd
import sqlite3

df = pd.read_csv("members.csv")

def extraer_cp(dataframe, col_origen, col_destino, pattern):
    dataframe[col_destino] = dataframe[col_origen].str.extract(pattern)
    return dataframe

df = extraer_cp(df, 'address', 'codigo_postal', r'(\d{5})')

def limpiar_telefono(dataframe, col):
    # Patrón: Busca los símbolos '+', '(' y ')'
    patron = r'[\+\(\)]'
    dataframe[col] = dataframe[col].astype(str).str.replace(patron, '', regex=True)
    return dataframe

df = limpiar_telefono(df, 'phone_number')

def formatear_y_calcular_edades(dataframe):

    dataframe['birth_date_dt'] = pd.to_datetime(dataframe['birth_date'])
    dataframe['fecha_nacimiento_fmt'] = dataframe['birth_date_dt'].dt.strftime('%d-%m-%Y')
    
    dataframe['register_time_dt'] = pd.to_datetime(dataframe['register_time'], unit='s')
    
    dataframe['edad_al_registro'] = dataframe['register_time_dt'].dt.year - dataframe['birth_date_dt'].dt.year
    
    return dataframe

df = formatear_y_calcular_edades(df)

conn = sqlite3.connect('mlearning_database.db')
df.to_sql('members_cleaned', conn, if_exists='replace', index=False)
conn.close()

df.to_csv('members_cleaned.csv', index=False)