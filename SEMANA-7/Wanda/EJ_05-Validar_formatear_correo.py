#función que reciba un email, lo limpie (strip+lower), 
#verifique '@' y '.' y retorne el dominio

def validar_email(correo):                  #'correo' es lo que recibe la función
    correo = correo.strip().lower()          #limpia espacios y pasa a minúsculas

    if "@" in correo and "." in correo:      #'in' pregunta si está dentro del texto
        dominio = correo.split("@")[1]      #lo que va DESPUÉS del @
        return dominio                     #devuelve el resultado
    else:
        return "Email no válido"

#Llama a la función con ejemplos
print(validar_email("   Juan.Perez@gmail.com  "))   # gmail.com
print(validar_email("correo_sin_arroba.com"))       # Email no válido
