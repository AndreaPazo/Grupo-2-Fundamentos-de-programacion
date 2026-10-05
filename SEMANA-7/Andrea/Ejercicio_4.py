# DIVIDIR Y UNIR PALABRAS:
# Dada la cadena 'rojo,verde,azul,amarillo', separa los colores, 
# ponlos en mayúsculas y únelos con ' | ' como separador.

colores = "rojo,verde,azul,amarillo"

colores = colores.split(",")
print(colores)

colores_mayus = []
for color in colores:
    colores_mayus.append(color.upper())

union = " | ".join(colores_mayus)

print(union)