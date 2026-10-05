# PARSEAR DATOS CSV MANUALMENTE:
# Dadas varias líneas CSV con formato 'nombre,nota,ciudad', 
# extrae la información y muestra un reporte formateado.

datos = [
    "Andrea,18,Lima",
    "Carlos,15,Trujillo",
    "María,19,Arequipa"
]

for linea in datos:
    nombre, nota, ciudad = linea.split(",")

    print(f"Nombre: {nombre}")
    print(f"Nota: {nota}")
    print(f"Ciudad: {ciudad}")
    print("----------------")