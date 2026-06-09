import numpy as np

# --- Configuración Inicial ---
array_1d = np.arange(9)
print("Arreglo original:")
print(array_1d)
print("-" * 30)

# --- Ejercicio 1: Transformar a dos dimensiones ---
# Se usa reshape() para cambiar las dimensiones a una matriz de 3x3
array_2d = array_1d.reshape(3, 3)

print("1) Arreglo en dos dimensiones:")
print(array_2d)
print("-" * 30)

array_restaurado = array_2d.flatten()

print("2) Arreglo en su forma original:")
print(array_restaurado)
print("-" * 30)

arreglo_A = np.array([[1, 2], 
                      [3, 4]])

arreglo_B = np.array([[5, 6], 
                      [7, 8]])

concat_vertical = np.vstack((arreglo_A, arreglo_B))
print("3) Concatenación vertical (vstack):")
print(concat_vertical)
print()

concat_horizontal = np.hstack((arreglo_A, arreglo_B))
print("3) Concatenación horizontal (hstack):")
print(concat_horizontal)