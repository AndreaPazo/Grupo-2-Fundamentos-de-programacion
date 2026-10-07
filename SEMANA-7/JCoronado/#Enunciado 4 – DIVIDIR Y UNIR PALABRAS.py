# Cadena inicial con elementos separados por comas
colores_csv = "rojo,verde,azul,amarillo"

# Convierte la cadena en una lista dividiéndola por cada coma usando .split(',')
lista_colores = colores_csv.split(",")

# Convierte cada elemento de la lista a mayúsculas usando una lista por comprensión y .upper()
colores_mayus = [color.upper() for color in lista_colores]

# Une los elementos de la lista en un único texto utilizando ' | ' con el método .join()
resultado_final = " | ".join(colores_mayus)

# Muestra el resultado formateado
print(f"Resultado: {resultado_final}")