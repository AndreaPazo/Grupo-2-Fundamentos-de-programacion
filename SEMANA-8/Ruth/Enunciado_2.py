

# Ordenamiento Alfanumérico de Nombres
# Dada la lista de nombres: ['Carlos','ana','Beatriz','david','Elena']
# 1) Imprímela sin modificar.
# 2) Ordénala alfabéticamente ignorando mayúsculas con sort().
# 3) Crea una nueva lista ordenada en orden descendente usando sorted().
# 4) Muestra los resultados de cada paso.


nombres = ['Carlos','ana','Beatriz','david','Elena']

# 1) Imprímela sin modificar
print("Lista original:")
print(nombres)

# 2) Ordénala alfabéticamente ignorando mayúsculas con sort()
nombres.sort(key=str.lower)
print("\nLista ordenada (ignorando mayúsculas):")
print(nombres)

# 3) Crea una nueva lista ordenada en orden descendente usando sorted()
nombres_descendente = sorted(nombres, key=str.lower, reverse=True)
print("\nLista ordenada en orden descendente:")
print(nombres_descendente)

# 4) Muestra los resultados de cada paso
print("\nResultados finales:")
print("Lista original:", nombres)
print("Lista ordenada (ignorando mayúsculas):", nombres)
print("Lista ordenada en orden descendente:", nombres_descendente)
    