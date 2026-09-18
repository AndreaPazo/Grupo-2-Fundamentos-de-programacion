def validar_email(email):
    # Comprueba que el correo contenga tanto el carácter '@' como el punto '.'
    return "@" in email and "." in email


def validar_password(pwd):
    # Verifica que la contraseña tenga una longitud mínima de 8 caracteres
    return len(pwd) >= 8


def validar_formulario(email, pwd):
    # COMPOSICIÓN: Reutiliza las validaciones individuales mediante el operador lógico 'and'.
    # Retorna True solo si AMBAS condiciones son verdaderas.
    return validar_email(email) and validar_password(pwd)

# Ejemplos de uso / Pruebas

print(validar_formulario("usuario@dominio.com", "12345678"))  # Imprime: True
print(validar_formulario("usuario@dominio.com", "1234"))      # Imprime: False (pwd corta)
print(validar_formulario("usuariodominio.com", "12345678"))   # Imprime: False (email sin '@')