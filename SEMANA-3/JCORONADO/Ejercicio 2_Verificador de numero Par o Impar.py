#Crea una función es_par(numero) que retorne True si el número es par o False si es impar.
# Función 1: Devuelve un valor booleano (True/False)
def es_par(numero):
    # El operador % 2 == 0 evalúa directamente a True si es par o False si es impar
    return numero % 2 == 0

# Función 2: Función sin return (void) que utiliza la función es_par
def mostrar_paridad(numero):
    # Composición: llamamos a es_par internamente dentro del condicional
    if es_par(numero):
        print(f"El número {numero} es PAR.")
    else:
        print(f"El número {numero} es IMPAR.")

# --- PRUEBA Y EJECUCIÓN DEL EJERCICIO 2 ---
lista_numeros = [10, 15, 22, 33, 40]

# Iteramos la lista aplicando la función void
for num in lista_numeros:
    mostrar_paridad(num)