# SISTEMA DE ATENCIÓN AL CLIENTE (COLA)
from collections import deque # Importar deque para crear una cola

# Crear la cola vacía
cola = deque() # Inicializar la cola como un deque vacío

# Función: tomar_turno(cliente)
# Agrega un cliente al final de la cola
def tomar_turno(cliente): # Agregar un cliente a la cola
    cola.append(cliente) # Agregar el cliente al final de la cola
    print(f"\n{cliente} tomó un turno.") # Mostrar mensaje indicando que el cliente tomó un turno

# Función: atender()
# Atiende al primer cliente de la cola
def atender(): # Atender al primer cliente de la cola
    if len(cola) > 0: # Verificar si hay clientes en la cola
        cliente = cola.popleft() # Eliminar y obtener el primer cliente de la cola
        print(f"Atendiendo a: {cliente}") # Mostrar mensaje indicando que se está atendiendo al cliente
    else:
        print("No hay clientes en espera.") # Mostrar mensaje indicando que no hay clientes en espera
# Función: mostrar_cola()
# Muestra cuántos clientes esperan
def mostrar_cola(): # Muestra la cantidad de clientes esperando y la cola actual
    print("\nClientes esperando:", len(cola)) # Mostrar la cantidad de clientes esperando
    print("Cola actual:", list(cola)) # Mostrar la cola actual como una lista

# SIMULACIÓN DEL EJERCICIO

# Entran 4 clientes
tomar_turno("Juan")
tomar_turno("María")
tomar_turno("Pedro")
tomar_turno("Lucía")

mostrar_cola() # Muestra la cantidad de clientes esperando y la cola actual

# Se atienden 2 clientes
atender()
atender()

mostrar_cola() # Muestra la cantidad de clientes esperando y la cola actual

# Entra 1 cliente más
tomar_turno("Carlos")

mostrar_cola() # Muestra la cantidad de clientes esperando y la cola actual

# Se atienden todos los clientes restantes
while len(cola) > 0:
    atender()

mostrar_cola() # Muestra la cantidad de clientes esperando y la cola actual