# Matriz bidimensional 3x3
matriz = [
    [5, 12, 7],
    [9, 15, 2],
    [3, 8, 10]
]

# Función de ordenación por Bubble Sort
def ordenar_fila(matriz, fila):
    for i in range(len(matriz[fila])):
        for j in range(0, len(matriz[fila]) - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Solicitar la fila a ordenar
fila = int(input("Ingresa el número de la fila (0-2) a ordenar: "))
ordenar_fila(matriz, fila)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
