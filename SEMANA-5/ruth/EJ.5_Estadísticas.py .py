
#Dado el siguiente arreglo de notas: [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
#Escribir un programa que calcule: promedio, nota más alta, nota más baja y cuántos aprobaron (nota ≥ 11).

notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]

promedio = sum(notas) / len(notas)
nota_alta = max(notas)
nota_baja = min(notas)

aprobados = 0

for nota in notas:
    if nota >= 11:
        aprobados += 1

print("Promedio:", promedio)
print("Nota más alta:", nota_alta)
print("Nota más baja:", nota_baja)
print("Cantidad de aprobados:", aprobados)