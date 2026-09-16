
#Escribe un programa que solicite la base y altura de un rectángulo y calcule su área:
# (A = base × altura) y su perímetro (P =2×(base+altura)). Muestra los resultados formateados


# Solicitar la base y altura del rectángulo al usuario
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

# Calcular el área y el perímetro del rectángulo
area = base * altura
perimetro = 2 * (base + altura)

# Mostrar los resultados formateados
print(f"El área del rectángulo es: {area:.2f}")
print(f"El perímetro del rectángulo es: {perimetro:.2f}")  
