#Ej.3 una lista de números como parámetro y devuelva su promedio numérico, asegurándote de retornar 0 si la lista está vacía para evitar un error de división por cero.
def promedio(numeros):
    total = sum(numeros)  # Variable local
    n = len(numeros)      # Variable local
    return total / n if n else 0

# Prueba de la función
print(promedio([10, 20, 30]))  # Imprime: 20.0
print(promedio([]))            # Imprime: 0 (lista vacía, evita error)