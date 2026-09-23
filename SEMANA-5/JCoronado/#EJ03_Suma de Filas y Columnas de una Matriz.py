# EJ 03: SUMA DE FILAS Y COLUMNAS DE UNA MATRIZ
# PASO 1: Crear la matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# PASO 2: Mostrar la matriz
print("Matriz 3x3:")
for fila in matriz:
    print(fila)

# PASO 3: SUMAR LAS FILAS
print("\nSuma de cada fila:")

# Recorrer cada fila de la matriz
for i in range(len(matriz)):

    # Crear una variable para acumular la suma
    suma_fila = 0

    # Recorrer los elementos de la fila
    for j in range(len(matriz[i])):

        # Acumular el valor de cada elemento
        suma_fila = suma_fila + matriz[i][j]

    # Mostrar la suma de la fila
    print("Suma fila", i, ":", suma_fila)

# PASO 4: SUMAR LAS COLUMNAS
print("\nSuma de cada columna:")

# Recorrer las columnas
for j in range(len(matriz[0])):

    # Crear una variable para acumular la suma
    suma_columna = 0

    # Recorrer las filas
    for i in range(len(matriz)):

        # Acumular el valor de cada elemento de la columna
        suma_columna = suma_columna + matriz[i][j]

    # Mostrar la suma de la columna
    print("Suma columna", j, ":", suma_columna)