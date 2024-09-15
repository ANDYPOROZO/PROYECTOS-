# Matriz bidimensional 3x3
matriz = [
    [5, 12, 7],
    [9, 15, 2],
    [3, 8, 10]
]

# Función de búsqueda
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado."

# Solicita al usuario un valor para buscar
valor = int(input("Ingresa el valor a buscar: "))
resultado = buscar_valor(matriz, valor)
print(resultado)
