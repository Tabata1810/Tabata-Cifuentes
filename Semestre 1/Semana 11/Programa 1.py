# Crear una matriz bidimensional (3x3)
matriz = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Búsqueda de un valor específico en la matriz
valor_buscado = int(input("Introduce el valor a buscar en la matriz: "))
if any(valor_buscado in fila for fila in matriz):
    print(f"Se encontró {valor_buscado} en la matriz.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")

# Inicializar variables para rastrear la posición del valor
fila_encontrada = -1
columna_encontrada = -1

# Recorrer la matriz para buscar el valor
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break
    if fila_encontrada != -1:
        break

    # Verificar si se encontró el valor y mostrar la posición en la que se encuentra
if fila_encontrada != -1:
    print(f"El valor {valor_buscado} está en la fila {fila_encontrada} y columna {columna_encontrada}.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")
