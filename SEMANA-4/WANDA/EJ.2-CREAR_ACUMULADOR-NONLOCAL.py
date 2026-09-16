def crear_acumulador():
    total = 0
 
    def acumular(valor):
        nonlocal total
        total += valor
        return total
 
    return acumular
 
 
suma = crear_acumulador()
print(suma(10))  # 10
print(suma(5))   # 15
 
#cada llamada a suma() suma sobre el total anterior, no reinicia
#desde cero,ya que solo es posible porque nonlocal mantiene viva la
#variable "total" entre una llamada y la siguiente
 
