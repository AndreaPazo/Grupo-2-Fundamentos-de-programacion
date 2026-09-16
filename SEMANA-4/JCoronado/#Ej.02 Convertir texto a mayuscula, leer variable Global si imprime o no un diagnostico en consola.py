#Ej.02 Si MODO_DEBUG es verdadero (True), muestra la alerta en pantalla y luego retorna el texto modificado.
MODO_DEBUG = True  # Variable global (usada como configuración/constante)

def procesar(dato):
    if MODO_DEBUG:  # Lectura directa sin necesidad de usar la palabra 'global'
        print(f"[DEBUG] Procesando: {dato}")
    return dato.upper()

# Prueba de la función
resultado = procesar("hola")  # Imprime: [DEBUG] Procesando: hola
print(resultado)              # Imprime: HOLA