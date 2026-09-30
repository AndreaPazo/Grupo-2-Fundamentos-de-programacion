# EJERCICIO 2 – SISTEMA DE HISTORIAL DE NAVEGACIÓN (Pila)
# Simula el historial de un navegador web usando una Pila (Stack). El usuario visita páginas y puede retroceder.
# a) Implementar visitar(url) → agrega la página a la pila y muestra la pila actual.
# b) Implementar retroceder() → quita la última página y muestra a dónde regresó.
# c) Implementar pagina_actual() → muestra la página actual sin quitarla.
# d) Probar con: Google → YouTube → GitHub → retroceder → retroceder.

# Pila (Stack) — LIFO para almacenar las páginas visitadas
historial = []


# a) Implementar visitar(url)
def visitar(url):
    historial.append(url)
    print("Visitando:", url)
    print("Pila actual:", historial)
    print("--------------")


# b) Implementar retroceder()
def retroceder():
    if len(historial) > 1:
        historial.pop()  # elimina la última página visitada
        print("Retrocediendo...")
        print("Regresó a:", historial[-1]) # consulta la última página
        print("Pila actual:", historial)
    else:
        print("No se puede retroceder.")

    print("--------------")
# c) Implementar pagina_actual()
def pagina_actual():
    if len(historial) > 0:
        print("Página actual:", historial[-1]) # consulta la última página
    else:
        print("No hay ninguna página abierta.")
    print("--------------")


# d) Probar con: Google → YouTube → GitHub → retroceder → retroceder.

visitar("Google")
visitar("YouTube")
visitar("GitHub")

pagina_actual()

retroceder()
retroceder()

pagina_actual()