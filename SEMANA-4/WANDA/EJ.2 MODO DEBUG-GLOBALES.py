MODO_DEBUG = True
 
def procesar(dato):
    #solo se LEE la variable global, no reasignamos, asi que
    #aca no hace falta la palabra global
    if MODO_DEBUG:
        print(f"[DEBUG] Procesando: {dato}")
    return dato.upper()
 
 
print(procesar("hola"))  # [DEBUG] Procesando: hola \n HOLA
 
