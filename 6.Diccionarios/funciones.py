#Funciones del menu

# listinTelefonico es un diccionario global
listinTelefonico = {
}

def listadoTelefonos():
    """Imprime el listín en el orden actual del diccionario (inserción)."""
    if not listinTelefonico:
        print("El listín está vacío.")
        return
    for nombre, telefono in listinTelefonico.items():
        print(f"{nombre}: {telefono}")

def listadoTelefonosAlfabetico():
    """Imprime el listín ordenado alfabéticamente por nombre (case-insensitive)."""
    if not listinTelefonico:
        print("El listín está vacío.")
        return
    for nombre in sorted(listinTelefonico.keys(), key=lambda s: s.lower()):
        print(f"{nombre}: {listinTelefonico[nombre]}")

def anadirContacto():
    """Añade un nuevo contacto al listín."""
    nombre = input("Ingrese el nombre del contacto: ")
    if nombre in listinTelefonico:
        print("El contacto ya existe.")
        return
    telefono = input("Ingrese el número de teléfono: ")
    listinTelefonico[nombre] = telefono
    print(f"Contacto {nombre} añadido.")

def modificarTelefono():
    """Modifica el número de teléfono de un contacto existente."""
    nombre = input("Ingrese el nombre del contacto a modificar: ")
    if nombre not in listinTelefonico:
        print("El contacto no existe.")
        return
    nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
    listinTelefonico[nombre] = nuevo_telefono
    print(f"Número de teléfono de {nombre} modificado.")

def buscarNumeroTelefono():
    """Busca y muestra el número de teléfono de un contacto."""
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in listinTelefonico:
        print(f"El número de teléfono de {nombre} es {listinTelefonico[nombre]}.")
    else:
        print("El contacto no existe.")

def eliminarContacto():
    """Elimina un contacto del listín."""
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in listinTelefonico:
        del listinTelefonico[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print("El contacto no existe.")

def borrarListinTelefonico():
    """Borra todos los contactos del listín."""
    listinTelefonico.clear()
    print("Listín telefónico borrado.")