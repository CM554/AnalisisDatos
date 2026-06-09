
import pandas as pd
import numpy as np

def corregir_nulos(df):
    df_clean = df.copy()
    df_clean['Género'] = df_clean['Género'].fillna('Desconocido')
    df_clean['Ciudad'] = df_clean['Ciudad'].fillna('Desconocido')
    df_clean['Nivel_Educación'] = df_clean['Nivel_Educación'].fillna('None')
    return df_clean

def corregir_atipicos(df):
    df_clean = df.copy()
    mediana_edad = df_clean['Edad'].median()
    df_clean.loc[(df_clean['Edad'] < 0) | (df_clean['Edad'] > 110), 'Edad'] = mediana_edad
    df_clean.loc[df_clean['Ingresos'] < 0, 'Ingresos'] = 0
    df_clean.loc[df_clean['Hijos'] < 0, 'Hijos'] = 0
    return df_clean

def estandarizar_categorias(df):
    df_clean = df.copy()
    mapping = {
        'Bachelors': 'Bachelor',
        'mastre': 'Master',
        'pHd': 'PhD',
        'no education': 'None'
    }
    df_clean['Nivel_Educación'] = df_clean['Nivel_Educación'].replace(mapping)
    return df_clean

if __name__ == "__main__":
    df = pd.read_csv('pipol_datos.csv')
    df_cleaned = corregir_nulos(df)
    df_cleaned = corregir_atipicos(df_cleaned)
    df_cleaned = estandarizar_categorias(df_cleaned)
    df_cleaned.to_csv('pipol_datos_limpios.csv', index=False)
    print("Limpieza completada. Archivo 'pipol_datos_limpios.csv' generado.")
