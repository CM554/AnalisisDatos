import numpy as np

def crear_matriz():
    print("\n--- Configuración de la Matriz ---")
    try:
        filas = int(input("Ingrese el número de filas: "))
        columnas = int(input("Ingrese el número de columnas: "))
        
        elementos = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = float(input(f"Elemento [{i+1}][{j+1}]: "))
                fila.append(valor)
            elementos.append(fila)
        
        return np.array(elementos)
    except ValueError:
        print("Error: Ingrese solo números válidos.")
        return None

def mostrar_menu():
    print("\n--- MENÚ DE OPERACIONES (linalg) ---")
    print("1. Calcular Determinante (det)")
    print("2. Calcular la Transpuesta (T)")
    print("3. Calcular la Norma de la matriz (norm)")
    print("4. Calcular Rango de la matriz (matrix_rank) ")
    print("5. Calcular Autovalores y Autovectores (eig)")
    print("6. Crear una nueva matriz")
    print("7. Salir")
    return input("Seleccione una opción: ")

def ejecutar():
    matriz = crear_matriz()
    
    if matriz is None:
        return

    while True:
        print("\nMatriz actual:")
        print(matriz)
        
        opcion = mostrar_menu()
        
        try:
            if opcion == '1':
                if matriz.shape[0] == matriz.shape[1]:
                    resultado = np.linalg.det(matriz)
                    print(f"\n> Determinante: {resultado:.4f}")
                else:
                    print("\n[Error] El determinante solo existe para matrices cuadradas.")
            elif opcion == '2':
                print("\n> Matriz Transpuesta:\n", matriz.T)

            elif opcion == '3':
                resultado = np.linalg.norm(matriz)
                print(f"\n> Norma de la matriz: {resultado:.4f}")

            elif opcion == '4':
                resultado = np.linalg.matrix_rank(matriz)
                print(f"\n> Rango de la matriz: {resultado}")

            elif opcion == '5':
                if matriz.shape[0] == matriz.shape[1]:
                    vals, vecs = np.linalg.eig(matriz)
                    print("\n> Autovalores:\n", vals)
                    print("> Autovectores:\n", vecs)
                else:
                    print("\n[Error] Requiere matriz cuadrada.")

            elif opcion == '6':
                matriz = crear_matriz()

            elif opcion == '7':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")
                
        except np.linalg.LinAlgError as e:
            print(f"\n[Error Matemático] {e}")

if __name__ == "__main__":
    ejecutar()