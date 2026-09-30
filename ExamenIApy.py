def crear_matriz(arr):
    """Toma el arreglo estático de 1D y lo almacena en una matriz de 2x3 usando ciclos."""
    matriz = []
    indice = 0
    for i in range(2):      # Ciclo para filas
        fila = []
        for j in range(3):  # Ciclo para columnas
            fila.append(arr[indice])
            indice += 1
        matriz.append(fila)
    return matriz

def crear_pila(arr):
    """Almacena los valores iniciales y agrega dos valores adicionales a la pila."""
    pila = list(arr)        # Copiamos los 6 elementos iniciales
    
    # Agregamos dos valores adicionales al final (tope de la pila)
    pila.append("Fire Force")
    pila.append("KonoSuba")
    return pila

def mostrar_resultados(matriz, pila):
    """Imprime en pantalla de forma clara y ordenada la matriz y la pila."""
    print("\n" + "-" * 40)
    print("          RESULTADOS FINALES")
    print("-" * 40)
    
    # Imprimir Matriz 2x3
    print("Matriz de Series (2x3):")
    for fila in matriz:
        print("  [", end=" ")
        for elemento in fila:
            print(f"{elemento:<16}", end=" ")
        print("]")
        
    print("\n" + "-" * 40)
    
    # Imprimir Pila (mostrando desde el tope hasta la base)
    print(f"Pila de Series (Total: {len(pila)} elementos):")
    print("  (Tope de la pila)")
    for i in range(len(pila) - 1, -1, -1):
        print(f"  | {pila[i]:<16} |")
    print("  +--------------------+")
    print("  (Base de la pila)")

def main():
    # Arreglo estático con 6 valores de series predefinidos
    series = [
        "Death Note", 
        "Jujutsu Kaisen", 
        "Re:Zero", 
        "Breaking Bad", 
        "The Boys", 
        "One Punch Man"
    ]
    
    datos_procesados = False
    matriz_2x3 = []
    pila_series = []
    
    # Ciclo continuo del menú usando while True
    while True:
        print("\n========================================")
        print("       MENU PRINCIPAL - ESTRUCTURAS     ")
        print("========================================")
        print("1. Procesar datos (Crear Matriz y Pila)")
        print("2. Mostrar Resultados (Matriz y Pila)")
        print("3. Salir")
        
        opcion_str = input("Seleccione una opcion: ").strip()
        
        # Validación con condicionales y control de excepciones
        if not opcion_str.isdigit():
            print("\n[Error] Por favor, ingrese un numero valido.")
            continue
            
        opcion = int(opcion_str)
        
        if opcion == 1:
            matriz_2x3 = crear_matriz(series)
            pila_series = crear_pila(series)
            datos_procesados = True
            print("\n[Exito] Matriz y Pila generadas correctamente.")
            
        elif opcion == 2:
            if datos_procesados:
                mostrar_resultados(matriz_2x3, pila_series)
            else:
                print("\n[Aviso] Primero debe procesar los datos (Opncion 1).")
                
        elif opcion == 3:
            print("\nSaliendo del programa. ¡Hasta luego!")
            break
            
        else:
            print("\n[Error] Opcion invalida. Intente de nuevo.")

if __name__ == "__main__":
    main()
