
# EJERCICIO 2 - HISTORIAL DE NAVEGACIÓN
# La pila se representa con una lista
historial = [] # Inicializar el historial como una lista vacía

# Función visitar
def visitar(url): # Agregar una nueva página al historial
    historial.append(url) # Agregar la URL a la pila
    print(f"\nVisitando: {url}") # Mostrar la página visitada
    print("Historial:", historial) # Mostrar el historial actualizado

# Función retroceder
def retroceder():
    if len(historial) > 1:  # Verificar si hay más de una página en el historial
        pagina_eliminada = historial.pop() # Eliminar la última página visitada
        print(f"\nSe cerró: {pagina_eliminada}") # Mostrar la página eliminada
        print("Historial:", historial) # Mostrar el historial actualizado
        print("Regresó a:", historial[-1]) # Mostrar la página actual después de retroceder
    elif len(historial) == 1: # Verificar si hay solo una página en el historial
        historial.pop() # Eliminar la última página visitada
        print("\nSolo hay una página abierta.") # Mostrar un mensaje indicando que solo hay una página abierta
    else:
        print("\nNo hay páginas.") # Mostrar un mensaje indicando que no hay páginas abiertas
# Función página actual
def pagina_actual(): # Mostrar la página actual
    if historial:    # Verificar si hay páginas en el historial
        print("\nPágina actual:", historial[-1]) # Mostrar la última página visitada
    else:
        print("\nNo hay páginas abiertas.") # Si no hay páginas abiertas, mostrar un mensaje indicando que no hay páginas abiertas.

# PRUEBA DEL EJERCICIO

visitar("Google")  # Visitar Google
visitar("Facebook")  # Visitar Facebook
visitar("YouTube")  # Visitar YouTube
visitar("GitHub")  # Visitar GitHub
# Mostrar la página actual
pagina_actual()
# Realizar retroceso de dos páginas
retroceder() # Retroceder a YouTube
retroceder() # Retroceder a Facebook
# Mostrar la página actual
pagina_actual()