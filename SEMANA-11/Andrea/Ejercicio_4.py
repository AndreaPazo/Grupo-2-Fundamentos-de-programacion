# Contador de vocales
# Función contar_vocales(texto) que cuente cuántas vocales (a,e,i,o,u
# incluyendo tildes) contiene el texto, sin importar mayúsculas

def contar_vocales(texto):
    vocales = "aeiouáéíóú"
    contador = 0

    texto = texto.lower()

    for letra in texto:
        if letra in vocales:
            contador += 1

    return contador


# Ejemplos de uso
print(contar_vocales("Hola Andrea"))
print(contar_vocales("PROGRAMACIÓN"))
print(contar_vocales("Fundamentos"))