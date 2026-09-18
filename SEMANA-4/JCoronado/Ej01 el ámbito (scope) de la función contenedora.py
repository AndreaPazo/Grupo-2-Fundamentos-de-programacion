def generador_id(): #Comentario: Valor inicial del contador
    ultimo_id = 0
    def nuevo_id():
        nonlocal ultimo_id   #indica el uso de variable externa
        ultimo_id += 1   #incrementa el contador
        return f"ID-{ultimo_id:04d}"

    return nuevo_id
#creacion de la instancia del generador
gen = generador_id()
#llamadas y salidas esperadas
print(gen()) # ID-0001
print(gen()) # ID-0002
