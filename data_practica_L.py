import pandas as pd
import sqlite3

df = pd.read_csv('members (1).csv')

conexion = sqlite3.connect('database_iniciales.db')

df.to_sql('members', conexion, if_exists='replace', index=False)

cursor = conexion.cursor()
cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='members';")
esquema = cursor.fetchone()[0]

print("=== ESQUEMA DE SQL (SCHEMA) ===")
print(esquema)

conexion.close()