#Ej.01 registrar_visita que modifique una variable global para llevar el conteo acumulativo de las visitas cada vez que sea llamada.
visitas = 0  # Variable global

def registrar_visita():
    global visitas
    visitas += 1
    print(f"Visita #{visitas} registrada")

# Pruebas de la función
registrar_visita()  # Imprime: Visita #1 registrada
registrar_visita()  # Imprime: Visita #2 registrada
print(f"Total: {visitas}")  # Imprime: Total: 2