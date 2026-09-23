# EJ02: OPERACIONES CRUD EN AGENDA DE CONTACTOS
# PASO 1: Crear la agenda inicial
agenda = ["Ana García", "Luis Torres", "Carlos Díaz", "María López"]

# Mostrar la agenda inicial
print("Agenda inicial:")
print(agenda)

# PASO 2: AGREGAR UN CONTACTO

# Agregar "Pedro Ruiz" al final de la lista
agenda.append("Pedro Ruiz")

# Mostrar la agenda después de agregar
print("\n1. Después de agregar Pedro Ruiz:")
print(agenda)

# PASO 3: BUSCAR UN CONTACTO

# Nombre que queremos buscar
contacto_buscar = "Carlos Díaz"

# Verificar si el contacto existe en la agenda
if contacto_buscar in agenda:

    # Obtener la posición del contacto
    posicion = agenda.index(contacto_buscar)

    # Mostrar la posición
    # Se suma 1 porque las listas comienzan en posición 0
    print("\n2. Contacto encontrado:")
    print("Carlos Díaz está en la posición", posicion + 1)

else:

    # Mostrar mensaje si no se encuentra
    print("\n2. Contacto no encontrado")

# PASO 4: MODIFICAR UN CONTACTO

# Nombre que queremos modificar
contacto_antiguo = "Luis Torres"

# Nuevo nombre
contacto_nuevo = "Luis Mendoza"

# Verificar si el contacto antiguo existe
if contacto_antiguo in agenda:

    # Obtener la posición del contacto
    posicion = agenda.index(contacto_antiguo)

    # Reemplazar el contacto antiguo por el nuevo
    agenda[posicion] = contacto_nuevo

    # Mostrar mensaje de modificación
    print("\n3. Contacto modificado:")
    print("Luis Torres -> Luis Mendoza")

else:

    # Mostrar mensaje si no existe
    print("\n3. Contacto no encontrado")

# PASO 5: ELIMINAR UN CONTACTO
# Nombre del contacto que queremos eliminar
contacto_eliminar = "Ana García"

# Verificar si el contacto existe
if contacto_eliminar in agenda:

    # Eliminar el contacto utilizando remove()
    agenda.remove(contacto_eliminar)

    # Mostrar mensaje de eliminación
    print("\n4. Contacto eliminado:")
    print("Ana García")

else:

    # Mostrar mensaje si no existe
    print("\n4. Contacto no encontrado")

# PASO 6: MOSTRAR LA AGENDA FINAL
print("\nAgenda final:")
print(agenda)