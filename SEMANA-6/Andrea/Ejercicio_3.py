# Simula el sistema de turnos de un banco usando una Cola (Queue). Los clientes esperan en orden de
# llegada.
# a) Implementar tomar_turno(cliente) → cliente entra a la cola.
# b) Implementar atender() → el primer cliente de la cola es atendido (sale).
# c) Implementar mostrar_cola() → mostrar cuántos esperan y sus nombres.
# d) Simular: 4 clientes entran, se atienden 2, entra 1 más, se atienden todos

# Cola de clientes
cola = []


# a) Implementar tomar_turno(cliente)
def tomar_turno(cliente):
    cola.append(cliente)
    print("Cliente", cliente, "tomó su turno.")
    print("--------------")


# b) Implementar atender()
def atender():
    if len(cola) > 0:
        cliente = cola.pop(0)
        print("Atendiendo a:", cliente)
    else:
        print("No hay clientes en espera.")
        print("--------------")


# c) Implementar mostrar_cola()
def mostrar_cola():
    print("Clientes en espera:", len(cola))
    print("Cola:", cola)
    print("--------------")


# d) Simulación

# Entran 4 clientes
tomar_turno("Ana")
tomar_turno("Luis")
tomar_turno("Carlos")
tomar_turno("María")

mostrar_cola()

# Se atienden 2
atender()
atender()

mostrar_cola()

# Entra 1 cliente más
tomar_turno("Pedro")

mostrar_cola()

# Se atienden todos
atender()
atender()
atender()

mostrar_cola()