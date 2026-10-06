#Lineas 'nombre,nota,ciudad' = reporte formateado

lineas_csv = ["Ana,18,Lima",
    "Luis,15,Trujillo",
    "Marta,20,Arequipa",
]
print("NOMBRE".ljust(10) + "NOTA".ljust(6) + "CIUDAD")   # ljust() alinea a la izquierda
print("-" * 28) #linea separa

#recorre c/linea lista
for linea in lineas_csv:
    nombre, nota, ciudad = linea.split(",") #spli separa datos cuando ve una coma
    print(nombre.ljust(10) + nota.ljust(6) + ciudad)

