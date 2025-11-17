from funciones import listadoOrdenado
from funciones import agregarUnContacto 
from funciones import modificarContacto
from funciones import buscarTel
from funciones import eliminarContacto 

#Imprime los titulos en mayuscula
def ImprimeTitulos():
    #Array de titulos
    titulos = [
        'Menu de Opciones'.upper(),
        'a) Listado de contactos por orden alfabético.',
        'b) Añadir un nuevo contacto.',
        'c) Modificar un contacto.',
        'd) Buscar un número de teléfono.',
        'e) Eliminar un contacto.',
        'f) Salir'
    ]
    #Pincha el ancho de titulos para generar una linea mas prolija
    ancho = max(len(t) for t in titulos)
    print("-" * ancho)
    #Recorre la lista e imprime los titulos en mayuscula
    for i in titulos:
        #En caso de no querer mayuscula solo poner i
        print(i)

#Funcion general de menu
def selectorOpciones():
    ImprimeTitulos()
    opcion = input("Seleccione una opción: ").lower()
    return opcion

#Para salir del menu
def salir():
    print("Saliendo del programa...")

#Funcion del menu
def menu():
    flag = True
    while flag:
        match(selectorOpciones()):
            case 'a': listadoOrdenado()
            case 'b': agregarUnContacto()
            case 'c': modificarContacto()
            case 'd': buscarTel()
            case 'e': eliminarContacto()
            case 'f': 
                salir() 
                flag = False
            case _: 
                print("Opción no válida. Por favor, seleccione una opción del menú.")

#Inicia el menu
menu()