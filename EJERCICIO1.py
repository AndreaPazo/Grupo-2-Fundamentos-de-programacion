#=======================================================.
#EJERCICIO01 - CALCULAR ÁREA Y PERÍMETRO DE UN RECTÁNGULO
#Estructura secuencial (lectura, un proceso, escritura)
#=======================================================

#Se pide datos al user
#float() convertir los datos a num decimales
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))

#Hace los cálculos
#Área = base x altura
area = base * altura

#Perímetro = 2 x (base + altura)
perimetro = 2 * (base + altura)

#Resultado
print("*****************************************")
print("RESULTADOS")
print("**************************************")
print(f"Base:      {base:.2f}")
print(f"Altura:    {altura:.2f}")
print(f"Área:      {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")