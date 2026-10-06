#Reemplazar cada palabra prohibida por asteriscos del mismo largo


texto = "El proyecto es tedioso y el profe es exigente"
p_prohibidas = ["tedioso", "exigente"]          #lista de palabras prohibidas

txt_censurado = texto
for palabra in p_prohibidas:
    asteriscos = "*" * len(palabra)        # "*" * 4 -> "****" (el * repite)
    txt_censurado = txt_censurado.replace(palabra, asteriscos)  # replace() cambia todas las apariciones

print(txt_censurado)   #El proyecto es ******* y el profe es ********
