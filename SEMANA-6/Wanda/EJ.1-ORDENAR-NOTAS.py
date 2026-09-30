#Compara elementos juntos y los intercambia si están desordenados.

def bubble_sort(lista):
    n = len(lista)  # n = cantidad total de elementos

    for i in range(n):  # i = número de pasada (num vuelta) que da
        intercambiado = False  #todavía no hemos hecho ningún cambio en la vuelt

        #Recorre hasta el último elemento que aún no está colocado
        for j in range(0, n - i - 1):

            #checa si elemento actual es mayor que el siguiente, están desordenados
            if lista[j] > lista[j + 1]:
                # Los intercambiamos (swap)
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambiado = True  # hubo al menos un cambio en esta vuelta

        # Si no hubo cambios esa la lista ya está ordenada
        if not intercambiado:
            break

    return lista

#aca la vuelta busca el elemento MÁS PEQUE de lo que falta ordenar
#y lo coloca al inicio de esa parte.
def selection_sort(lista):
    n = len(lista)

    for i in range(n - 1):  #i = posición donde vamos a colocar el min

        idx_min = i  #el mínimo está en la posición i

        #Buscar si hay algo más peque en la lista
        for j in range(i + 1, n):
            if lista[j] < lista[idx_min]:
                idx_min = j  #asegurar su posición

        #solo intercambiamos si el mínimo no era ya el primero
        if idx_min != i:
            lista[i], lista[idx_min] = lista[idx_min], lista[i]

    return lista


#Reparto la misma lista pero en diferentes types de funciones
notas_originales = [85, 42, 93, 67, 28, 75]
notas_bubble = [85, 42, 93, 67, 28, 75]
notas_selection = [85, 42, 93, 67, 28, 75]

#Type 1
bubble_sort(notas_bubble)
print("1) Ordenado con Bubble Sort:   ", notas_bubble)

#Type 2
selection_sort(notas_selection)
print("2) Ordenado con Selection Sort:", notas_selection)

#Calculamos nota max y min
nota_maxima = notas_originales[0]
nota_minima = notas_originales[0]
suma_notas = 0  # aquí iremos acumulando la suma de todas las notas

#se recorre list con for para comparar notas
for nota in notas_originales:

    if nota > nota_maxima:
        nota_maxima = nota

    if nota < nota_minima:
        nota_minima = nota

    suma_notas = suma_notas + nota

promedio = suma_notas / len(notas_originales)

print("----------------------------------------")
print("   Nota mínima: ", nota_minima)
print("   Nota máxima: ", nota_maxima)
print("   Promedio:    ", promedio)
