#Quitar los espacios y contar cuántos carácteres hay 

texto = "   Python es divertido   "
clean = texto.strip()        #método strip() quitamos " " inicio/fin
cantidad = len(clean)         #función len() contamos

print("Cadena:", clean)
print("Cantidad de caracteres:", cantidad)   
