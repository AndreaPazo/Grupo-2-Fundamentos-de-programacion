


# PARSEAR DATOS CSV MANUALMENTE:
# Dadas varias líneas CSV con formato 'nombre,nota,ciudad', extrae la información y muestra un reporte formateado.


# Ejemplo de líneas CSV
lineas_csv = [
    "Juan,85,Madrid",
    "María,90,Barcelona",
    "Pedro,75,Valencia"
]

# Parsear los datos y mostrar el reporte
for linea in lineas_csv:
    nombre, nota, ciudad = linea.split(',')
    print(f"Nombre: {nombre}, Nota: {nota}, Ciudad: {ciudad}")

    