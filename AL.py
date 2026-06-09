import numpy as np

def crear_matriz(filas, columnas, automatica=True):
    if automatica:
        # Genera números aleatorios entre 0 y 10
        return np.random.randint(0, 11, size=(filas, columnas))
    else:
        print(f"Ingrese los elementos para una matriz de {filas}x{columnas}:")
        elementos = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                val = float(input(f"Elemento [{i+1}][{j+1}]: "))
                fila.append(val)
            elementos.append(fila)
        return np.array(elementos)

def menu():
    print("\n--- CALCULADORA DE MATRICES ---")
    f = int(input("Número de filas: "))
    c = int(input("Número de columnas: "))

    modo = input("¿Generar matrices automáticamente? (s/n): ").lower()
    auto = True if modo == 's' else False

    print("\nGenerando Matriz A...")
    A = crear_matriz(f, c, auto)
    print("Generando Matriz B...")
    B = crear_matriz(f, c, auto)

    print("\nMatriz A:\n", A)
    print("Matriz B:\n", B)

    while True:
        print("\n--- OPERACIONES ---")
        print("1. Sumar (A + B)")
        print("2. Restar (A - B)")
        print("3. Multiplicar (Elemento por elemento)")
        print("4. Producto Punto (Dot Product)")
        print("5. Transpuesta de A")
        print("6. Determinante de A (Solo si es cuadrada)")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            print("\nResultado Suma:\n", np.add(A, B))
        elif opcion == '2':
            print("\nResultado Resta:\n", np.subtract(A, B))
        elif opcion == '3':
            print("\nResultado Multiplicación Elemento a Elemento:\n", np.multiply(A, B))
        elif opcion == '4':
            if A.shape[1] == B.shape[0]:
                print("\nResultado Producto Punto:\n", np.dot(A, B))
            else:
                print("\nError: Columnas de A deben coincidir con filas de B.")
        elif opcion == '5':
            print("\nTranspuesta de A:\n", A.T)
        elif opcion == '6':
            if f == c:
                det = np.linalg.det(A)
                print(f"\nDeterminante de A: {det:.2f}")
            else:
                print("\nError: La matriz debe ser cuadrada.")
        elif opcion == '7':
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()