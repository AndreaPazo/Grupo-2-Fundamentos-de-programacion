import matematicas_utils as mu

radios = [1, 2, 3, 5]

reporte = mu.reporte_geometrico(radios)

print("REPORTE GEOMÉTRICO")

for fila in reporte:

    print("Radio:", fila["radio"])
    print("Área:", round(fila["area"], 2))
    print("Perímetro:", round(fila["perimetro"], 2))
    print("----------------------")