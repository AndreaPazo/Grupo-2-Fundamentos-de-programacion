# Búsqueda Simple en una Lista de Emails
# Tienes la lista: emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']
# 1) Imprime cuántos emails son de Gmail.
# 2) Muestra solo los emails que terminan en '.com'.
# 3) Verifica si 'luis@outlook.com' está en la lista (usa 'in')

emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']

# 1) Imprime cuántos emails son de Gmail.
contador = 0

for email in emails:
    if email.endswith('@gmail.com'):
        contador += 1

print("1. Cantidad de emails de Gmail:", contador)

# 2) Muestra solo los emails que terminan en '.com'.
print("\n2. Emails que terminan en '.com':")

for email in emails:
    if email.endswith('.com'):
        print(email)

# 3) Verifica si 'luis@outlook.com' está en la lista (usa 'in')
print("\n3. Verificar si luis@outlook.com está en la lista:")
print('luis@outlook.com' in emails)
