#Creacion del diccionario todo en uno

menuDeOpciones = [
    "-"*15,
    "Menu de opciones",
    "a)Listado de telefonos, usando el orden por defecto.",
    "b)Listado de telefonos por orden alfabetico",
    "c)Añadir un nuevo contacto",
    "d)Modificar el teléfono de un contacto.", 
    "e)Buscar un número de teléfono.", 
    "f)Eliminar un contacto.",
    "g)Borrar el listín telefónico.", 
    "h)Salir"
]

#Creamos el listin con el que se trabajara
listinTelefonico = {}
#Esta funcion imprime menu
def imprimeMenu():
    for i in menuDeOpciones:
        print(i)

#Listar los telefonos por default
def ordenarListin():
    if not listinTelefonico:
        print('No existen datos en el listin telefonico.')
    else:
        for nombre, telefono in listinTelefonico.items():
            print(f"{nombre}: {telefono}")

#Listar los telefonos por orden alfabetico
def ordenarListinAlfabetico():
    if not listinTelefonico:
        print('No existen datos en el listin telefonico.')
    else:
        for nombre, telefono in sorted(listinTelefonico.items(), key=lambda x: x[0].lower()):
            print(f"{nombre} : {telefono}")

#Agregar un nuevo contacto
def agregarContacto():
    nombre = input('Nombre a agregar: ')
    if nombre in listinTelefonico:
        print("El contacto ya existe.")
    else:   
        telefono = input('Telefono a agregar: ')
        listinTelefonico[nombre] = telefono
        print(f"Contacto {nombre} añadido.")

#Modificar el telefono de un contacto
def modificarContacto():
    if not listinTelefonico:
        print('No existen datos en el listin telefonico.')
    else:
        nombre = input("Ingrese el nombre del contacto a modificar: ")
        if nombre not in listinTelefonico:
            print("El contacto no existe.")
        else:
            nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
            listinTelefonico[nombre] = nuevo_telefono
            print(f"Número de teléfono de {nombre} modificado.")
        

#Buscar un numero de telefono
def buscarNumero():
    if not listinTelefonico:
        print('No existen datos en el listin telefonico.')
    else:
        nombre = input('Busca por nombre(telefono): ')
        if nombre not in listinTelefonico:
            print("El contacto no existe.")
        else:
            print(f"El nombre del teléfono de {nombre} es {listinTelefonico[nombre]}.")
    
#Eliminar un contacto
def borrarUnContacto():
    if not listinTelefonico:
        print('No existen datos en el listin telefonico.')
    else:
        nombre = input('Contacto a borrar(nombre): ')
        if nombre in listinTelefonico:
            del listinTelefonico[nombre]
            print(f"Contacto {nombre} eliminado.")
        else:
            print("El contacto no existe.")

#Borrar todo
def borrarTodo():
    if not listinTelefonico:
        print('No existen datos en el listin telefonico.')
    else:
        print('Seguro de tu eleccion? es irreversible. s/n')
        eleccion = input('(Ingresa s para si y n para no, si no coincide la operacion finaliza igual.)')
        eleccion = eleccion.lower()
        match eleccion:
            case 's': listinTelefonico.clear()
            case 'n': print('operacion cancelada.')
            case _: print('operacion cancelada por opcion incorrecta.')

#Funcion general de menu
def menu():
    flag = True
    while flag:
        imprimeMenu()
        opcion = input('Elige una opcion del menu: ')
        opcion = opcion.lower()
        match opcion:
            case 'a': ordenarListin()
            case 'b': ordenarListinAlfabetico()
            case 'c': agregarContacto()
            case 'd': modificarContacto()
            case 'e': buscarNumero()
            case 'f': borrarUnContacto()
            case 'g': borrarTodo()
            case 'h':
                print('Finalizando programa.')
                flag = False
            case _:
                print('Elige una opcion valida.')
        
menu()