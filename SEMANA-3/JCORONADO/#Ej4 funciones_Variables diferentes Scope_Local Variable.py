#Ej.4 Escribe dos funciones independientes en Python (funcion_a y funcion_b) que utilicen una variable local con el mismo nombre (valor) pero asignándole diferentes datos, para demostrar cómo funciona el alcance (scope) local de las variables.
def funcion_a():
    valor = 100  # Variable local a funcion_a
    return valor

def funcion_b():
    valor = 200  # Variable local a funcion_b (independiente)
    return valor

# Prueba de las funciones
print(funcion_a(), funcion_b())  # Imprime: 100 200