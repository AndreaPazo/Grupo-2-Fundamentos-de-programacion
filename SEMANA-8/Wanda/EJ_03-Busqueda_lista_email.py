print("\n" + "=" * 20)
print("EJERCICIO 3 - Búsqueda en emails")
print("=" * 20)

emails = ['ana@gmail.com', 'luis@outlook.com', 'mia@gmail.com', 'juan@yahoo.com']
 
#Contar cuántos son de Gmail
cont_gmail = 0
for email in emails:
    if 'gmail' in email:
        cont_gmail += 1
print("1) Emails de Gmail:", cont_gmail)
 
#Mostrar los que terminan en '.com'
print("2) Emails que terminan en '.com':")
for email in emails:
    if email.endswith('.com'): #metodo para aer en que sufijo termina - bool
        print("  -", email)
 
#Verificar si Luis está en la lista
if 'luis@outlook.com' in emails:
    print("3) 'luis@outlook.com' SÍ está en la lista")
else:
    print("3) 'luis@outlook.com' NO está en la lista")
