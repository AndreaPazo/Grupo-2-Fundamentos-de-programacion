#Una matriz es una "lista de listas" (filas dentro de una lista).
#Ejemplo, la matriz con num de 1 al 9:
#   [1, 3, 4]
#   [5, 8, 9]
#   [2, 6, 7]

#Bubble Sort compara elementos VECINOS en UNA SOLA línea (una sola lista).
#Como la matriz tiene filas y columnas, el truco es:
##Aplanar matriz  pasar todos números a una sola lista larga
# [1,3,4, 5,8,9, 2,6,7]
##Ordenar esa lista con el mismoBubble Sort 
##Reconstruir" la matriz ya ordenada 3x3
#      [1, 2, 3]
#      [4, 5, 6]
#      [7, 8, 9]

#Aplanar la matriz en una lista simpl
def aplanar_matriz(matriz):
    lista_plana = []  #guarda los num en una sola list

    for fila in matriz:        #recorre cada fila de la matriz
        for numero in fila:    #recorre cada número dentro de esa fila
            lista_plana.append(numero)  #grega a la lista plana

    return lista_plana


#Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # swap
                intercambiado = True
        if not intercambiado:
            break
    return lista


#Reconstruir la matriz ya ordenada
#Convierte la lista plana ordenada otra vez en filas de "columnas" elementos
def reconstruir_matriz(lista_ordenada, filas, columnas):
    matriz_nueva = []
    indice = 0  #este índice recorre la lista_ordenada

    for i in range(filas):
        fila_actual = []
        for j in range(columnas):
            fila_actual.append(lista_ordenada[indice])
            indice = indice + 1  #avanza al siguiente num de la lista
        matriz_nueva.append(fila_actual)  #agrega la fila completa a la matriz

    return matriz_nueva


#Matriz original 3x3 
matriz = [
    [1, 3, 4],
    [5, 8, 9],
    [2, 6, 7]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

#Aplano la matriz
numeros = aplanar_matriz(matriz)
print()
print("Lista aplanada (sin ordenar):", numeros)

#Ordeno la lista con Bubble Sort
bubble_sort(numeros)
print("Lista aplanada (ordenada ascendente):", numeros)

#Reconstruir la matriz ya ordenada (3 filas x 3 columnas)
matriz_ordenada = reconstruir_matriz(numeros, 3, 3)

print()
print("Matriz ordenada Asc:")
for fila in matriz_ordenada:
    print(fila)
