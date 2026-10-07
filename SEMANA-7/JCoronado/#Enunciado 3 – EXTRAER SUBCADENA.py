# Definición de la cadena base
texto = "Análisis de Datos con Python"

# Extrae la palabra 'Datos' indicando el rango de índices [12:17] mediante slicing
palabra_datos = texto[12:17]

# Extrae la palabra 'Python' usando slicing desde la posición 22 hasta el final [22:]
palabra_python = texto[22:]

# Muestra los resultados obtenidos del rebanado de cadena
print(f"Primera palabra extraída: {palabra_datos}")
print(f"Segunda palabra extraída: {palabra_python}")