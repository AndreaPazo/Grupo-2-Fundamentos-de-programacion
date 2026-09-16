inventario = []
 
def agregar(producto):
    #aca "global" es opcional: el append() no reemplaza la lista,
    #solo lo modifica por dentro (la lista se puede alterar sin
    #reasignarla). Se deja igual para dejar fijo que se esta
    #usando la lista de afuera
    global inventario
    inventario.append(producto)
 
 
def mostrar():
    for p in inventario:
        print(f" - {p}")
 
 
agregar("Laptop")
agregar("Mouse")
mostrar()
# -Laptop
# -Mouse
 
