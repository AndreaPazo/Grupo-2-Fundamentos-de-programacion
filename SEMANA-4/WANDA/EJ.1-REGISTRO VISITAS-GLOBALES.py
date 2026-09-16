visitas = 0
 
def registrar_visita():
    #sin "global" aqui, Python crearia una variable local nueva
    #llamada visitas y el += fallaria (se leeria antes de existir)
    global visitas
    visitas += 1
    print(f"Visita #{visitas} registrada")
 
 
registrar_visita()  # Visita #1
registrar_visita()  # Visita #2
print(f"Total: {visitas}")  # Total: 2
 
