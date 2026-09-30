

#-----------– SISTEMA DE HISTORIAL DE NAVEGACIÓN (Pila)-----------------
# Simula el historial de un navegador web usando una Pila (Stack). El usuario visita páginas y puede retroceder.
# a) Implementar visitar(url) → agrega la página a la pila y muestra la pila actual.
# b) Implementar retroceder() → quita la última página y muestra a dónde regresó.
# c) Implementar pagina_actual() → muestra la página actual sin quitarla.
# d) Probar con: Google → YouTube → GitHub → retroceder → retroceder.

# Pila (Stack) — LIFO para almacenar las páginas visitadas



historial = []

# a) Implementar visitar(url) → agrega la página a la pila y muestra la pila actual.

def visitar(url):
    historial.append(url)
    print("Página visitada:", url)
    print("Historial actual:", historial)


# b) Implementar retroceder() → quita la última página y muestra a dónde regresó.

def retroceder():
    if historial:
        pagina_actual = historial.pop()
        print("Regresando desde:", pagina_actual)
        if historial:
            print("Página actual después de retroceder:", historial[-1])
        else:
            print("No hay más páginas en el historial.")
    else:
        print("No hay páginas para retroceder.")

# c) Implementar pagina_actual() → muestra la página actual sin quitarla.

def pagina_actual():
    if historial:
        print("Página actual:", historial[-1])
    else:
        print("No hay páginas en el historial.")

# d) Probar con: Google → YouTube → GitHub → retroceder → retroceder.
visitar("Google")
visitar("YouTube")
visitar("GitHub")
pagina_actual()

pagina_actual()

retroceder()
retroceder()

pagina_actual()