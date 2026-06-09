import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

datos = {
    'ID_Activo': ['A001', 'A002', 'A003', 'A004', 'A005'],
    'Departamento': ['Sistemas', 'Sistemas', 'Sindicatura', 'Tesorería', 'Sistemas'],
    'Tipo_Equipo': ['Laptop', 'Servidor', 'Laptop', 'Impresora', 'Switch'],
    'Valor_MXN': [25000, 85000, 18000, 6000, 12000],
    'Meses_Uso': [24, 48, 12, 60, np.nan] # Un dato nulo intencional simulando falta de registro
}

df_inventario = pd.DataFrame(datos)

print("--- Primeros registros ---")
print(df_inventario.head())

print("\n--- Información del DataFrame y detección de nulos ---")
df_inventario.info()

print("\n--- Estadísticas Descriptivas ---")
print(df_inventario.describe())

sns.set_theme(style="whitegrid")
plt.figure(figsize=(8, 5))

sns.barplot(x='Departamento', y='Valor_MXN', data=df_inventario, estimator=sum, errorbar=None, hue='Departamento')

plt.title('Valor Total de Activos por Departamento')
plt.ylabel('Valor en MXN')
plt.xlabel('Departamento')
plt.show()