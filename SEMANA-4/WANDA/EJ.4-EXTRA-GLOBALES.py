notas = []
 
def agregar_nota(n):
    #aca NO hace falta "global": solo se muta la lista (append),
    #no se le asigna un valor nuevo con "=",solo se obliga cuando se reasigna una variable locl
    notas.append(n)
 
 
agregar_nota(95)
print(notas)  # [95]
 
#checar que con EJ.3-INVENTARIO-GLOBALES.py: mismo patron, con o sin "global"
#el resultado es identico porque ambos casos solo mutan la lista
