from persona import Persona 
#! Asi se importan clases

# listinTelefonico es un diccionario global
listinTelefonico = {
}

def listadoOrdenado():
    """Imprime el listín ordenado alfabéticamente por nombre (case-insensitive)."""
    if not listinTelefonico:
        print("El listín está vacío.")
        return
    for nombre in sorted(listinTelefonico.keys(), key=lambda s: s.lower()):
        print(f"{obtienePersona(nombre)}")

def obtienePersona(name):
    for nombre,persona in listinTelefonico.items():
        if nombre == name:
            return persona.mostrarPersona()
            
def agregarUnContacto():
    """Añade un nuevo contacto al listín."""
    #! Con los datos pedidos, en vez de meterlo, crearemos una persona
    nombre = input("Ingrese el nombre del contacto: ")
    if nombre in listinTelefonico:
        print("El contacto ya existe.")
        return
    dirrecion = input('Ingrese la dirrecion: ')
    telefono = input("Ingrese el número de teléfono: ")
    persona = Persona(nombre,dirrecion, telefono)
    listinTelefonico[nombre] = persona
    print(f"Contacto {nombre} añadido.")

def modificarContacto():
    """Modifica el número de teléfono de un contacto existente."""
    nombre = input("Ingrese el nombre del contacto a modificar: ")
    if buscaExistencia(nombre):
        print("El contacto no existe.")
        return    
    nuevo_dirrecion = input('Ingrese la dirrecion: ')
    nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
    for persona in listinTelefonico.values():
        if persona.get_name() == nombre:
            persona.set_tel(nuevo_telefono)
            persona.set_dirrecion(nuevo_dirrecion)
            #break #! Para que no siga recorriendo habilitar si todo va bien para mejor optimizacion
    print(f"Número de teléfono de {nombre} modificado.")

def buscaExistencia(nombre):
    for name in listinTelefonico.keys():
        if nombre.lower() == name.lower():
            return False
    return True
    
def buscarTel():
    """Busca y muestra el número de teléfono de un contacto."""
    nombre = input("Ingrese el nombre del contacto a buscar: ")
    if nombre in listinTelefonico:
        for persona in listinTelefonico.value():
            if persona.get_name() == nombre:
                persona.mostrarPersona()
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