
# Archivo: main.py
import matematicas_utils as mu

def reporte_geometrico(radios):
    print(f"{'Radio':<10} | {'Área':<12} | {'Perímetro':<12}")
    print("-" * 40)

    for r in radios:
        area = mu.area_circulo(r)
        perimetro = mu.perimetro_circulo(r)
        print(f"{r:<10.2f} | {area:<12.2f} | {perimetro:<12.2f}")

radios = [1, 3, 5, 10]
reporte_geometrico(radios)