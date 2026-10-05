# VALIDAR Y FORMATEAR CORRE ELECTRÓNICO:
# Escribe una función que reciba un email, lo limpie (strip+lower), 
# verifique que contiene '@' y '.' y retorne el dominio.

def validar_email(email):
    email = email.strip().lower()

    if "@" in email and "." in email:
        dominio = email.split("@")[1]
        return dominio
    else:
        return "Correo inválido"

correo = input("Ingrese su correo: ")

resultado = validar_email(correo)

print("Dominio:", resultado)