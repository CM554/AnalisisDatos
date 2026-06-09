import pandas as pd
# Ejemplo 1: Crear un DataFrame desde un diccionario
datos = {
    'Producto': ['Laptop', 'Mouse', 'Monitor'],
    'Precio': [1200, 25, 300],
    'Stock': [10, 50, 15]
}
df = pd.DataFrame(datos)
print(df)

# Ejemplo 2: Filtrar filas de un DataFrame
caros = df[df['Precio'] > 100]
print(caros)