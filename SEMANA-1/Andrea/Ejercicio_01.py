# Área del Rectángulo
# Escribe un programa que solicite la base y altura de un rectángulo y calcule su área 
# (A = base × altura) y su perímetro (P = 2×(base+altura)). Muestra los resultados formateados.

base = int(input("Ingrese la base de un rectangulo: "))
altura = int(input("Ingrese la altura de un rectangulo: "))

A = base * altura
P = 2*(base+altura)

print(f"El area del rectangulo es: {A}")
print(f"El perimetro del rectangulo es: {P}")