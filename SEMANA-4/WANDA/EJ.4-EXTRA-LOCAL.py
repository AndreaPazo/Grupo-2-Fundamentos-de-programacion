def funcion_a():
    valor = 100
    return valor
 
 
def funcion_b():
    valor = 200
    return valor
 
#ambas funciones usan el nombre "valor",pero no se cruzan entre
#si: cada una tiene su propia copia, aislada una de la otra
print(funcion_a(), funcion_b())  #100 200
