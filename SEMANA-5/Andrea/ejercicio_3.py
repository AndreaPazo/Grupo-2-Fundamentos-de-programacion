# Suma de Filas y Columnas de una Matriz
# Dada la matriz 3×3: [[1,2,3],[4,5,6],[7,8,9]] — Calcular y mostrar la 
# suma de cada fila y la suma de cada columna.

# Declaración de matriz 3x3
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Suma de cada fila
for i in range(3):
    print(f"Suma de fila {i}: {sum(matriz[i])}")

# Suma de cada columna
for j in range(3):
    suma = 0
    for i in range(3):
        suma += matriz[i][j]
    print(f"Suma de columna {j}: {suma}")