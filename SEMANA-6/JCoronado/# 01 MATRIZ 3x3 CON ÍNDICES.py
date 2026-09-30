# ==================================
# MATRIZ 3x3 TRABAJANDO CON ÍNDICES
# ==================================

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]                              # Crear una matriz 3x3 con valores del 1 al 9

print("Matriz:") # Mostrar la matriz completa

for fila in matriz:  # Recorrer cada fila de la matriz y mostrarla
    print(fila)      # Mostrar la fila

print("\nAccediendo con índices:")      # Acceder a elementos específicos de la matriz usando índices
print("matriz[0][0] =", matriz[0][0])   # Mostrar el elemento en la primera fila y primera columna
print("matriz[1][1] =", matriz[1][1])   # Mostrar el elemento en la segunda fila y segunda columna
print("matriz[2][2] =", matriz[2][2])   # Mostrar el elemento en la tercera fila y tercera columna

print("\nRecorrido completo:")

for i in range(len(matriz)):            # Recorrer las filas de la matriz usando índices
    for j in range(len(matriz[i])):     # Recorrer las columnas de la matriz usando índices
        print(f"matriz[{i}][{j}] = {matriz[i][j]}")    # Mostrar cada elemento de la matriz con sus índices correspondientes


# ELIMINAR ELEMENTO REPETIDO (uva) DE UNA LISTA

fruta = ["uva", "pera", "uva", "naranja"] # Lista original con elementos repetidos

print("\nLista original:") # Mostrar la lista original
print(fruta) # Mostrar la lista original

# Eliminar la segunda aparición de "uva"
fruta.pop(2) # Eliminar el elemento en el índice 2 (segunda aparición de "uva")

print("\nLista final:") # Mostrar la lista final después de eliminar el elemento repetido
print(fruta)            # Mostrar la lista final después de eliminar el elemento repetido