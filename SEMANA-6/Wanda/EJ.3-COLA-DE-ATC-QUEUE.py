#Cola con "deque"  librería collections, usando dos operaciones:
#append()   = el cliente entra al final de la cola (enqueue)
#popleft()  = sale el PRIMER cliente de la cola (dequeue)
#FIFO = First In, First Out (el primero que llega, el primero que sale)

from collections import deque
#"cola" vacía al inicio (nadie está esperando)
cola_clientes = deque()


#funcion tomar_turno(cliente)
#El cliente entra al final de la cola (enqueue)
def tomar_turno(cliente):
    cola_clientes.append(cliente)  # se agrega al final de la cola
    print(cliente, "tomó un turno y entró a la cola.")


#funcion atender()
#Se atiende y sale el PRIMER cliente de la cola (dequeue)
def atender():
    if len(cola_clientes) == 0:
        print("No hay clientes esperando.")
    else:
        cliente_atendido = cola_clientes.popleft()  # quita y devuelve el primero
        print("Atendiendo a:", cliente_atendido)


#funcion mostrar_cola()
#Muestra cuántos clientes esperan y sus nombres, sin sacarlos
def mostrar_cola():
    print("Clientes esperando:", len(cola_clientes))
    # Recorremos la cola uno por uno para mostrar cada nombre
    for cliente in cola_clientes:
        print(" -", cliente)


#Ejemplo 4 clientes entran, se atienden 2, entra 1 más, se atienden todos
print("==*- SIMULACIÓN DE LA COLA -*==")

#Entran 4 clientes
tomar_turno("Ana")
tomar_turno("Luis")
tomar_turno("Carlos")
tomar_turno("María")
mostrar_cola()
print("***")

#Se atienden 2 clientes (los primeros en llegar: Ana y Luis)
atender()
atender()
mostrar_cola()
print("**")

#Entra 1 cliente más
tomar_turno("Pedro")
mostrar_cola()
print("**")

#Se atienden todos los que quedan
print("Atendiendo a todos los que faltan...")
while len(cola_clientes) > 0:   #repito mientras aún haya gente en la cola
    atender()

mostrar_cola()  #al final debe salir una cola vacía (0 clientes)
