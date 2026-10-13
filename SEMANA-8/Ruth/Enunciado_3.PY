

# Tienes la lista: emails = ['ana@gmail.com','luis@outlook.com','mia@gmail.com','juan@yahoo.com']
# 1) Imprime cuántos emails son de Gmail.
# 2) Muestra solo los emails que terminan en '.com'.
# 3) Verifica si 'luis@outlook.com' está en la lista (usa 'in')

print("=" * 45)
print(f"{'LISTA DE EMAILS':^45}")
print("=" * 45)

    # Lista de emails dada
emails = ['ana@gmail.com', 'luis@outlook.com', 'mia@gmail.com', 'juan@yahoo.com']

# 1) Imprimir cuántos emails son de Gmail
# Contamos cuántas veces aparece '@gmail.com' en la lista
gmail = sum(1 for email in emails if '@gmail.com' in email)
print(f"1) Cantidad de emails de Gmail: {gmail}")
print("=" * 45)

# 2) Mostrar solo los emails que terminan en '.com'
print("2) Emails que terminan en '.com':")
for email in emails:
    if email.endswith('.com'):
        print(f"   - {email}")
print("=" * 45)

# 3) Verificar si 'luis@outlook.com' está en la lista (usando 'in')
esta_luis = 'luis@outlook.com' in emails
print(f"3) ¿'luis@outlook.com' está en la lista?: {esta_luis}")
print("=" * 45)