import pandas as pd
import sqlite3
import re

df = pd.read_csv("members.csv")


patron_mas62 = r'\+62'

patron_corchetes_guion = r'^\[.*?\]-'

patron_espacios = r'\s'

df['contiene_mas62'] = df['phone_number'].str.contains(patron_mas62, regex=True, na=False)

df['telefono_sin_espacios'] = df['phone_number'].str.replace(patron_espacios, '', regex=True)

df['inicia_corchetes_guion'] = df['phone_number'].str.contains(patron_corchetes_guion, regex=True, na=False)

print("Guardando base de datos SQLite3...")
conexion = sqlite3.connect("mlearning_database.db")
df.to_sql("members_regex", conexion, if_exists="replace", index=False)
conexion.close()

print("Proceso completado con éxito.")