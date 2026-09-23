notas = [15, 18, 12, 9, 17, 14, 20, 11, 16, 13]
 
# sum()/len() evito usar for porque contaría a mano lit
promedio = sum(notas) / len(notas)
 
#max()/min() recorre la lista una sola vez cada uno y devuelve
#el valor mas alto/bajo
maximo = max(notas)
minimo = min(notas)
 
#la lista se arma con la notas que cumple condition
#(>=11) y se mide su longitud
aprobados = len([n for n in notas if n >= 11])
 
print(f"Promedio: {promedio} | Max: {maximo} | Min: {minimo} | Aprobados: {aprobados}")
#Promedio: 14.5 | Max: 20 | Min: 9 | Aprobados: 9
