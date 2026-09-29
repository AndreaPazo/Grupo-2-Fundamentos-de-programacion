# EJERCICIO 1 – ORDENAR NOTAS ESTUDIANTILES
# Un profesor tiene las notas de 6 estudiantes en una lista desordenada:
# [85, 42, 93, 67, 28, 75]
# Se pide:
# a) Ordenar la lista usando
# Bubble Sort e imprimir el resultado.
# b) Ordenar usando
# Selection Sort e imprimir el resultado.
# c) Mostrar la nota mínima, máxima y el promedio.

notas = [85, 42, 93, 67, 28, 75]

# a) Bubble Sort
def bubble_sort(lista):

    n = len(lista) # n = total de elementos
    for i in range(n): # i = pasada actual (0 a n-1)
        intercambiado = False # optimización: detectar lista ya ordenada
        for j in range(0, n-i-1): # j recorre hasta el último no colocado
            if lista[j] > lista[j+1]: # ¿elemento actual mayor que el siguiente?
                # Si sí, se intercambian (swap)
                lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambiado = True # hubo al menos 1 cambio
        if not intercambiado: # si no hubo cambios → lista ordenada
            break # ¡salir antes! (optimización)

print("a) Bubble Sort:")
bubble_sort(notas)
print(notas)
   


# b) Selection Sort
def selection_sort(lista):

    n = len(lista) # cantidad de elementos
    for i in range(n - 1): # i = inicio sublista sin ordenar
        # Asumir que el mínimo es el primero de la sublista
        idx_min = i # guarda índice del mínimo actual
        for j in range(i + 1, n): # buscar mínimo en el resto
            if lista[j] < lista[idx_min]: # ¿encontré algo menor?
                idx_min = j # actualizo el índice del mínimo
        # Solo intercambiar si el mínimo no era ya el primero
        if idx_min != i:
            lista[i], lista[idx_min] = lista[idx_min], lista[i] # swap

# ── Ejemplo de uso ──────────────────────────────────────────
print("a) Selection Sort:")
selection_sort(notas)
print(notas)


# c) Nota mínima, máxima y promedio
minima = min(notas)
maxima = max(notas)
promedio = sum(notas) / len(notas)

print("\nc) Resultados:")
print("Nota mínima:", minima)
print("Nota máxima:", maxima)
print("Promedio:", promedio)