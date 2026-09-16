#Ej.03 Dos funciones que utilicen una lista global llamada inventario para añadir elementos y mostrar el contenido actual de la lista línea por línea.
inventario = []  # Lista global inicializada vacía

def agregar(producto):
    global inventario
    inventario.append(producto)

def mostrar():
    for p in inventario:
        print(f" - {p}")

# Pruebas del programa
agregar("Laptop")
agregar("Mouse")
agregar("Teclado")
mostrar()
# Imprime:
#  - Laptop
#  - Mouse
#  - Teclado
