
# Función contar_vocales(texto) que cuente cuántas vocales (a,e,i,o,u
# incluyendo tildes) contiene el texto, sin importar mayúsculas.
# Tip: convierte a lower() y recorre con in

def contar_vocales(texto):
  vocales = "aeiouáéíóú"
  contador = 0
  for letra in texto.lower():
    if letra in vocales:
      contador += 1
  return contador


# Ejemplos de uso:
print(contar_vocales("Hola Mundo"))  # 4
print(contar_vocales("Programación"))  # 5
print(contar_vocales("MURCIÉLAGO"))  # 5