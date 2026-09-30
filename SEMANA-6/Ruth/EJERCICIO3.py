
# Simula el sistema de turnos de un banco usando una Cola (Queue). Los clientes esperan en orden de
# llegada.

cola = []

#a) Implementar tomar_turno(cliente) → cliente entra a la cola.
 
def tomar_turno(cliente):
    cola.append(cliente)
    print("Cliente en la cola:", cliente)
    mostrar_cola()

# b) Implementar atender() → el primer cliente de la cola es atendido (sale).
def atender():
    if cola:
        cliente_atendido = cola.pop(0)
        print("Atendiendo al cliente:", cliente_atendido)
    else:
        print("No hay clientes en la cola.")

# c) Implementar mostrar_cola() → mostrar cuántos esperan y sus nombres.
def mostrar_cola():
    print("Clientes en la cola:", len(cola))
    for i, cliente in enumerate(cola, start=1):
        print(f"{i}. {cliente}")

# d) Simular: 4 clientes entran, se atienden 2, entra 1 más, se atienden todos
tomar_turno("Cliente 1")
tomar_turno("Cliente 2")
tomar_turno("Cliente 3")
tomar_turno("Cliente 4")
atender()
atender()
tomar_turno("Cliente 5")
atender()
atender()
atender()


