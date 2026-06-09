import pandas as pd
# Ejemplo 1: Crear una Series con un índice personalizado
edades = pd.Series([25, 30, 35], index=['Ana', 'Beto', 'Carla'])
print(edades)
# Ejemplo 2: Operaciones matemáticas directas
proximo_anio = edades + 1
print(proximo_anio)