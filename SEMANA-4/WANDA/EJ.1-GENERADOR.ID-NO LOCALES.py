def generador_id():
    ultimo_id = 0
 
    def nuevo_id():
        #ultimo_id no es global (vive dentro de generador_id) ni
        #local a nuevo_id (viene de la funcion que la contiene):
        #nonlocal permite modificarla sin crear una copia local
        nonlocal ultimo_id
        ultimo_id += 1
        return f"ID-{ultimo_id:04d}"
 
    return nuevo_id
 
gen = generador_id()
print(gen())  #ID-0002
print(gen())  #ID-0003
 
#gen "recuerda" el valor de ultimo_id entre llamada y llamada,
#aunque generador_id() ya termino de ejecutarse hace rato
 
