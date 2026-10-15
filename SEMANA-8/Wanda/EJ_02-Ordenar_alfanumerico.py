#EJERCICIO 2 - Ordenamiento alfanumérico de nombres

print("\n" + "=" * 60)
print("EJERCICIO 2 - Ordenamiento de nombres")
print("=" * 60)
 
lista_nombres = ['Carlos', 'ana', 'Beatriz', 'david', 'Elena']
print("1) Original:", lista_nombres)
 
# .sort() ordena de la A a la Z directamente
lista_nombres.sort()
print("2) Ordenado A-Z:", lista_nombres)
 
# sorted(..., reverse=True) crea una copia de la Z a la A
descendente = sorted(lista_nombres, reverse=True)
print("3) Descendente Z-A:", descendente)
