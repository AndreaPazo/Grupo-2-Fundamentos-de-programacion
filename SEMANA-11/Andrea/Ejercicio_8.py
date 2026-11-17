# Importar módulo propio
# Importa matematicas_utils con alias mu y crea reporte_geometrico(radios) que muestre área y perímetro de cada círculo en una tabla.

import matematicas_utils as mu

def reporte_geometrico(radios):
    print("REPORTE GEOMÉTRICO")
    print("---------------------------------------")
    print("Radio\tÁrea\t\tPerímetro")
    print("---------------------------------------")

    for r in radios:
        area = mu.area_circulo(r)
        perimetro = mu.perimetro_circulo(r)

        print(f"{r}\t{area:.2f}\t\t{perimetro:.2f}")


# Ejemplo de uso
reporte_geometrico([2, 4, 6, 8])