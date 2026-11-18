#Necesita matematicas_utils.py en la misma carpeta
import matematicas_utils as mu #importa el archivo local y le da un alias corto 'mu'


def reporte_geometrico(radios):
    #muestra una tabla formateada con área y perímetro de cada círculo
    print(f"{'Radio':>8} | {'Área':>10} | {'Perímetro':>10}") #f-string con :>8 alinea el texto a la derecha en 8 espacios
    print("-" * 34)
    for r in radios:
        #llama a las funciones del módulo importado usando el alias mu
        print(f"{r:>8} | {mu.area_circulo(r):>10.2f} | {mu.perimetro_circulo(r):>10.2f}")


if __name__ == "__main__": #__name__ var que indica si se ejecuta este script directamente
    reporte_geometrico([1, 2.5, 5, 10])
