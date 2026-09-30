
#--------- ORDENAR NOTAS ESTUDIANTILES------------

# Un profesor tiene las notas de 6 estudiantes en una lista desordenada:
# [85, 42, 93, 67, 28, 75]

# Se pide:
# a) Ordenar la lista usando
# Bubble Sort e imprimir el resultado.
# b) Ordenar usando
# Selection Sort e imprimir el resultado.
# c) Mostrar la nota mínima, máxima y el promedio.




# a) Ordenar la lista usando
# Bubble Sort
notas_bubble = [85, 42, 93, 67, 28, 75]

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

notas_bubble_ordenadas = bubble_sort(notas_bubble)

print("Notas ordenadas con Bubble Sort:", notas_bubble_ordenadas)

# b) Ordenar la lista usando
# Selection Sort
notas_selection = [85, 42, 93, 67, 28, 75]

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

notas_selection_ordenadas = selection_sort(notas_selection)

print("Notas ordenadas con Selection Sort:", notas_selection_ordenadas)

# c) Calcular la nota mínima, máxima y promedio
def calcular_estadisticas(lista):
    nota_minima = min(lista)
    nota_maxima = max(lista)
    promedio = sum(lista) / len(lista)
    return nota_minima, nota_maxima, promedio

nota_minima, nota_maxima, promedio = calcular_estadisticas(notas_bubble_ordenadas)

print("Nota mínima:", nota_minima)
print("Nota máxima:", nota_maxima)
print("Promedio:", promedio)

