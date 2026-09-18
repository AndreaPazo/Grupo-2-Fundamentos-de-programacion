#utiliza clausuara closure con la palabra clave simula imteruptor toggle que conmuta estado entre encendido y apagado en cada llamada.
def crear_interruptor():
    estado = False  #Inicializa la variable booleana que representa el estado del interruptor (comienza apagado).

    def cambiar():  #modifique directamente la variable
        nonlocal estado   #Permite que la función interna
        estado = not estado #Invierte el valor actual (de False a True, de True a False, etc.).
        return "ON" if estado else "OFF"  #Retorna la cadena on si el estado es verdadero o "OFF" si es falso mediante un operador ternario.

    return cambiar


# Uso del interruptor
switch = crear_interruptor()  #definida en la función externa

print(switch())  # Salida: ON  1mera llamada false pasa a imprime on
print(switch())  # Salida: OFF 2da llamada true pasa a false imprime off
print(switch())  # Salida: ON  3era llamada false pasa a imprime on