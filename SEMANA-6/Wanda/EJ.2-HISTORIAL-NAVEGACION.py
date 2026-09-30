#Solo se usa dos operaciones,agregar y retirar
#append() = "push")
# pop()  = saca ultimo elemento 
#LIFO = Last In, First Out (el último que entra, es el primero que sale)

#Creamos nuestra "pila" como una lista vacía al inicio
historial = []

#Agrega una nueva página al final de la lista (tope de la pila)
def visitar(url):
    historial.append(url)  #push
    print("Visitando:", url)
    print("Pila actual:", historial)
    print("*****")

#Quita la página actual (la del final) y muestra la página a la q regresamos

def retroceder():
    # Si la pila está vacía, no hay a dónde retroceder
    if len(historial) == 0:
        print("No hay más páginas en el historial.")
    else:
        pagina_que_sale = historial.pop()  # pop -> quita y devuelve el último
        print("Retrocediendo desde:", pagina_que_sale)

        # Después de quitar, vemos cuál quedó como página actual
        if len(historial) > 0:
            ultima_posicion = len(historial) - 1
            print("Ahora estás en:", historial[ultima_posicion])
        else:
            print("Ya no hay páginas anteriores.")
    print("****")


#Función pagina_actual()
#Muestra la página en la que estamos,sin quitar de la pila
def pagina_actual():
    if len(historial) == 0:
        print("No hay ninguna página abierta.")
    else:
        ultima_posicion = len(historial) - 1
        print("Página actual:", historial[ultima_posicion])


#PRUEBAS: Google --> YouTube --> GitHub --> retroceder --> retroceder
print("=== SIMULACIÓN DEL HISTORIAL ===")
visitar("Google")
visitar("YouTube")
visitar("GitHub")

pagina_actual()   #debería mostrar GitHub
print("*****")

retroceder()       #sale GitHub, queda YouTube
retroceder()       #sale YouTube, queda Google

pagina_actual()    #debería mostrar Google
