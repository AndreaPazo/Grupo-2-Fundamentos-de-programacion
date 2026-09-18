def crear_acumulador(): #Inicializa la variable
    total = 0 #devuelve la función interna acumular.
    
    def acumular(valor):
        nonlocal total #indica que utilice variable
        total += valor
        return total
        
    return acumular

# Uso del acumulador
suma = crear_acumulador()   #acumulador reteniendo el estado
#Suman el nuevo valor al total acumulado
#y devuelven el resultado progresivo.
print(suma(10))  # Salida: 10   
print(suma(5))   # Salida: 15