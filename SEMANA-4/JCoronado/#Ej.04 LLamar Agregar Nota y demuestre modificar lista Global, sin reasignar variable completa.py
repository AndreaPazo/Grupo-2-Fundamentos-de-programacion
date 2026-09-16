#Ej.04 llamada agregar_nota que demuestre cómo es posible modificar (mutar) el contenido de una lista global sin necesidad de utilizar la palabra clave global, siempre y cuando no se reasigne la variable completa.
# Las listas/dicts se MUTAN sin 'global'
# (porque no se reasigna la referencia)
notas = []

def agregar_nota(n):
    notas.append(n) # ← Modifica la lista directamente sin usar 'global'

# Prueba de la función
agregar_nota(95)
print(notas) # Imprime: [95]