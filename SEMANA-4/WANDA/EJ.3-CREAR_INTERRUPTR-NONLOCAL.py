def crear_interruptor():
    estado = False
 
    def cambiar():
        nonlocal estado
        estado = not estado
        return "ON" if estado else "OFF"
 
    return cambiar
 
switch = crear_interruptor()
print(switch())  # ON
print(switch())  # OFF
print(switch())  # ON
 
#sigue mismo patron que EJ.1 y EJ.2 al ser una funcion interna que modifica una
#variable de la funcion que la envuelve,ya q se usa nonlocl
 
