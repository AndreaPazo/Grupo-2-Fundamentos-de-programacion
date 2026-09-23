agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
 
#se uso append porque no es relevante aún la posición de la data
agenda.append("Pedro Ruiz")
 
#acá si definimos posición con index
posicion = agenda.index("Carlos Díaz")
print(f"'Carlos Díaz' esta en la posicion {posicion}")
 
#sobreescribrimos el valor
i = agenda.index("Luis Torres")
agenda[i] = "Luis Mendoza"
 
#borro por VALOR (no por indice) encuentro coindicendia y remuevo
agenda.remove("Ana García")
 
print(agenda)
# ['Luis Mendoza', 'Carlos Díaz', 'María López', 'Pedro Ruiz']
 
