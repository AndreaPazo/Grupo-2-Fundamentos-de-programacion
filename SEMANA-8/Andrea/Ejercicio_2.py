# Ordenamiento Alfanumérico de Nombres
# Dada la lista de nombres: ['Carlos','ana','Beatriz','david','Elena']
# 1) Imprímela sin modificar.
# 2) Ordénala alfabéticamente ignorando mayúsculas con sort().
# 3) Crea una nueva lista ordenada en orden descendente usando sorted().
# 4) Muestra los resultados de cada paso

nombres = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']

# 1. Imprimir la lista original
print("1. Lista original:")
print(nombres)

# 2. Ordenar alfabéticamente ignorando mayúsculas con sort()
nombres.sort(key=str.lower)
print("\n2. Lista ordenada ascendentemente:")
print(nombres)

# 3. Crear una nueva lista ordenada descendentemente con sorted()
nombres_descendentes = sorted(nombres, key=str.lower, reverse=True)
print("\n3. Lista ordenada descendentemente:")
print(nombres_descendentes)
