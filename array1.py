import numpy as np

def mostrar_menu():
    while True:
        print("\n" + "="*45)
        print("   MENÚ DE OPERACIONES CON ARREGLOS (NUMPY)")
        print("="*45)
        print("1) Crear vector (arreglo unidimensional)")
        print("2) Crear matriz (arreglo multidimensional)")
        print("3) Operaciones Básicas (+, -, *, //)")
        print("4) Operaciones Especiales (Pi, Trigonométricas, Ln)")
        print("5) Crear Matriz de ceros")
        print("6) Crear Matriz de unos")
        print("7) Crear Matriz Identidad")
        print("8) Salir")
        print("="*45)
        
        opcion = input("Elige una opción (1-8): ")
        
        if opcion == '1':
            n = int(input("¿Cuántos elementos tendrá el vector?: "))
            elementos = []
            for i in range(n):
                val = float(input(f"Ingresa el elemento {i+1}: "))
                elementos.append(val)
            vector = np.array(elementos)
            print("\nVector creado:")
            print(vector)
            print("Dimensión:", vector.shape)

        elif opcion == '2':
            filas = int(input("¿Cuántos renglones (filas) tendrá la matriz?: "))
            cols = int(input("¿Cuántos elementos por renglón (columnas)?: "))
            matriz = []
            for i in range(filas):
                fila = []
                print(f"--- Renglón {i+1} ---")
                for j in range(cols):
                    val = float(input(f"Elemento [{i+1},{j+1}]: "))
                    fila.append(val)
                matriz.append(fila)
            arreglo_multi = np.array(matriz)
            print("\nMatriz creada:")
            print(arreglo_multi)
            print("Dimensión:", arreglo_multi.shape)

        elif opcion == '3':
            print("\n--- Operaciones Básicas ---")
            print("Crearemos un vector rápido para la demostración.")
            n = int(input("Tamaño del vector: "))
            vec = np.array([float(input(f"Elemento {i+1}: ")) for i in range(n)])
            
            print("Operaciones disponibles: 1) Suma 2) Resta 3) Multiplicación 4) División entera")
            op_basica = input("Elige la operación: ")
            escalar = float(input("Ingresa el número (escalar) para operar con el vector: "))
            
            if op_basica == '1':
                print(f"\nResultado (Suma):\n{vec + escalar}")
            elif op_basica == '2':
                print(f"\nResultado (Resta):\n{vec - escalar}")
            elif op_basica == '3':
                print(f"\nResultado (Multiplicación):\n{vec * escalar}")
            elif op_basica == '4':
                print(f"\nResultado (División entera):\n{vec // escalar}")
            else:
                print("Operación no válida.")

        elif opcion == '4':
            print("\n--- Operaciones Especiales ---")
            print("Crearemos un vector rápido para la demostración.")
            n = int(input("Tamaño del vector: "))
            vec = np.array([float(input(f"Elemento {i+1}: ")) for i in range(n)])
            
            print("\nOpciones: 1) Multiplicar por Pi 2) Seno 3) Coseno 4) Logaritmo Natural (Ln)")
            op_esp = input("Elige la operación: ")
            
            if op_esp == '1':
                print(f"\nVector * Pi:\n{vec * np.pi}")
            elif op_esp == '2':
                print(f"\nSeno (rad):\n{np.sin(vec)}")
            elif op_esp == '3':
                print(f"\nCoseno (rad):\n{np.cos(vec)}")
            elif op_esp == '4':
                # Evitar logaritmo de 0 o números negativos para no generar advertencias de NumPy
                if np.any(vec <= 0):
                    print("\nAdvertencia: El logaritmo natural solo está definido para números positivos.")
                else:
                    print(f"\nLogaritmo Natural (Ln):\n{np.log(vec)}")
            else:
                print("Operación no válida.")

        elif opcion == '5':
            filas = int(input("Número de renglones: "))
            cols = int(input("Número de columnas: "))
            matriz_ceros = np.zeros((filas, cols))
            print("\nMatriz de ceros:")
            print(matriz_ceros)

        elif opcion == '6':
            filas = int(input("Número de renglones: "))
            cols = int(input("Número de columnas: "))
            matriz_unos = np.ones((filas, cols))
            print("\nMatriz de unos:")
            print(matriz_unos)

        elif opcion == '7':
            n = int(input("Tamaño de la matriz identidad (es cuadrada, ingresa un solo número n x n): "))
            matriz_identidad = np.eye(n)
            print("\nMatriz Identidad:")
            print(matriz_identidad)

        elif opcion == '8':
            print("Saliendo del programa...")
            break
            
        else:
            print("Opción no reconocida. Por favor, intenta de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    mostrar_menu()