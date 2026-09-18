

#Dada la matriz 3×3: [[1,2,3],[4,5,6],[7,8,9]] — Calcular y mostrar la suma de cada fila y la suma de cada columna.

matriz = [[1,2,3],[4,5,6],[7,8,9]]

# Calcular la suma de cada fila
sumas_filas = [sum(fila) for fila in matriz]

# Calcular la suma de cada columna
sumas_columnas = [sum(matriz[i][j] for i in range(3)) for j in range(3)]

print("Suma de cada fila:", sumas_filas)
print("Suma de cada columna:", sumas_columnas)

