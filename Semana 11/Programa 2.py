# Crear una matriz bidimensional (3x3)
matriz = [
    [1, 9, 5],
    [2, 7, 6],
    [3, 8, 4]
]

# Función para ordenar una fila de manera ascendente utilizando Bubble Sort
def bubble_sort_fila_desendente(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] < fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Mostrar la matriz original
print("Matriz Original:")
mostrar_matriz(matriz)

# Ordenar cada fila de la matriz utilizando Bubble Sort
for fila in matriz:
    bubble_sort_fila_desendente(fila)

# Mostrar la matriz ordenada
print("\nMatriz Ordenada por Filas:")
mostrar_matriz(matriz)