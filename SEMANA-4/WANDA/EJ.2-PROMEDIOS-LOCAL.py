def promedio(numeros):
    total = sum(numeros)
    n = len(numeros)
    #el "if n else 0" evita ZeroDivisionError al intentar div un num u operacion si la lista llega vacia
    return total / n if n else 0
 
print(promedio([10, 20, 30]))  # 20.0
 
#el total y n solo viven mientras se ejecuta promedio(); en otra
#llamada a otra funcion se pueden reusar esos mismos names
#sin que se choquen entre si
 
