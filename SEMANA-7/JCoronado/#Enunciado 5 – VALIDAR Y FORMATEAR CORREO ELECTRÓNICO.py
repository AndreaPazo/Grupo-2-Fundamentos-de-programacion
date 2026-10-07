def procesar_email(email):
    # Elimina espacios extras en bordes con .strip() y pasa todo a minúsculas con .lower()
    email_limpio = email.strip().lower()
    
    # Verifica que el correo contenga tanto el carácter '@' como el punto '.'
    if "@" in email_limpio and "." in email_limpio:
        # Divide la cadena en nombre de usuario y dominio tomando el carácter '@' como corte
        partes = email_limpio.split("@")
        
        # Retorna la segunda parte (índice 1), la cual corresponde al dominio del correo
        return partes[1]
    else:
        # Retorna un mensaje indicando que el formato de correo no es válido
        return "Correo electrónico no válido"

# Ejemplo de prueba de la función
correo_ejemplo = "   Usuario_Ejemplo@Sitioweb.com  "
print(f"Dominio extraído: {procesar_email(correo_ejemplo)}")