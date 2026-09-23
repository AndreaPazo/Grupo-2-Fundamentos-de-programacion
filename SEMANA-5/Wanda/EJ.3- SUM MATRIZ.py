matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
 
filas = len(matriz)        #cantidad de listas internas (filas)
columnas = len(matriz[0])  #cantidad de elementos en la primera fila
 
#Sum por fila,list ind, asi que sum() la suma no necesita otro bucle
sumas_filas = []
for i in range(filas):
    sumas_filas.append(sum(matriz [i]))
 
#Sum columnas,al no ser lista propia,se reparte esta columna por filas[fila][col]
#patron de "ciclo anidado"
sumas_columnas = []
for j in range(columnas):
    total_columna = 0
    for i in range(filas):
        total_columna += matriz [i][j]
    sumas_columnas.append(total_columna)
 
#Text de salida a mano, con un for y +=
texto_filas = ""
for i in range(filas):
    if i > 0:
        texto_filas += " | "
    texto_filas += f"fila {i}: {sumas_filas[i]}"
 
texto_columnas = ""
for j in range(columnas):
    if j > 0:
        texto_columnas += " | "
    texto_columnas += f"col {j}: {sumas_columnas[j]}"
 
print(f"Suma {texto_filas} || Suma {texto_columnas}")
#debe quedar asi
#Sum fila 0: 6 | fila 1: 15 | fila 2: 24 || Suma col 0: 12 | col 1: 15 | col 2: 18
