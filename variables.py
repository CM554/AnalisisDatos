# Variables iniciales
x = 5
y = -9
pi = 3.1416
e = 2.7182

while True:
    print("\n=== Menú Actualizado ===")
    print("E - Mostrar números enteros")
    print("F - Mostrar valores de pi y e")
    print("D - Capturar y mostrar mis datos")
    print("S - Salir")

    opcion = input("Elige una opción: ").upper()

    if opcion == "E":
        print(f"Enteros: {x}, {y}")
        
    elif opcion == "F":
        print(f"Flotantes: pi={pi}, e={e}")
        
    elif opcion == "D":
        # Captura de datos
        nombre = input("Ingresa tu nombre: ")
        apellido = input("Ingresa tu apellido: ")
        
        # Uso de float para estatura y int para edad (conversión de tipos)
        estatura = float(input("Ingresa tu estatura (ej. 1.75): "))
        edad = int(input("Ingresa tu edad: "))
        
        # Mostrar datos capturados
        print("\n--- Datos Registrados ---")
        print(f"Nombre completo: {nombre} {apellido}")
        print(f"Estatura: {estatura} m")
        print(f"Edad: {edad} años")
        
        # Verificación de mayoría de edad
        if edad >= 18:
            print("Resultado: Eres mayor de edad.")
        else:
            print("Resultado: Eres menor de edad.")
            
    elif opcion == "S":
        print("Saliendo del programa...")
        break
        
    else:
        print("Opción no válida, intenta de nuevo.")