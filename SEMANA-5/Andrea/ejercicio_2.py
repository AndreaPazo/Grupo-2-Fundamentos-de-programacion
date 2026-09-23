# Operaciones CRUD en Agenda de Contactos
# Tienes la agenda: ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]
# Realiza: (1) Agregar "Pedro Ruiz", (2) Buscar "Carlos Díaz" y mostrar posición, (3) 
# Modificar "Luis Torres" por "Luis Mendoza", (4) Eliminar "Ana García"

agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]

# 1. Agregar "Pedro Ruiz"
agenda.append("Pedro Ruiz")

# 2. Buscar "Carlos Díaz" y mostrar su posición
pos = agenda.index("Carlos Díaz")
print("Carlos Díaz está en la posición:", pos)

# 3. Modificar "Luis Torres" por "Luis Mendoza"
agenda[1] = "Luis Mendoza"

# 4. Eliminar "Ana García"
agenda.remove("Ana García")

# Mostrar agenda final
print("Agenda final:", agenda)