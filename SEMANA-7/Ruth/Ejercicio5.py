

# VALIDAR Y FORMATEAR CORRE ELECTRÓNICO:
# Escribe una función que reciba un email, lo limpie (strip+lower), verifique que contiene '@' y '.' y retorne el dominio.

# Función para validar y formatear el correo electrónico
def validar_email(email):
    # Limpiar el correo electrónico
    email_limpio = email.strip().lower()
    
    # Verificar que contiene '@' y '.'
    if '@' in email_limpio and '.' in email_limpio:
        # Extraer el dominio (parte después del '@')
        dominio = email_limpio.split('@')[1]
        return dominio
    else:
        return "Correo electrónico inválido"

# Solicitar al usuario que ingrese su correo electrónico
correo = input("Por favor, ingresa tu correo electrónico: ")

# Llamar a la función y mostrar el resultado
dominio = validar_email(correo)
if dominio != "Correo electrónico inválido":
    print(f"El dominio del correo electrónico es: {dominio}")
