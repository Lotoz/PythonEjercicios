#Menu general de la aplicacion
#Estoy probando una nueva version alternativas de las otras

#Import de funciones
#Importa directamente las funciones necesarias
# Y no haria falta poner el prefijo funciones.
from funciones import listadoTelefonos
from funciones import listadoTelefonosAlfabetico
from funciones import anadirContacto
from funciones import modificarTelefono
from funciones import buscarNumeroTelefono
from funciones import eliminarContacto
from funciones import borrarListinTelefonico

#Imprime los titulos en mayuscula
def ImprimeTitulos():
    titulos = [
    "Menu de opciones:",
    "A) Listado de teléfonos, usando el orden por defecto",
    "b) Listado de teléfonos por orden alfabético.", 
    "c) Añadir un nuevo contacto.", 
    "d) Modificar el teléfono de un contacto.",
    "e) Buscar un número de teléfono.", 
    "f) Eliminar un contacto.", 
    "g) Borrar el listín telefónico.", 
    "h) Salir"
    ]
    #Recorre la lista e imprime los titulos en mayuscula
    #La funcion max obtiene el ancho del titulo mas largo
    # para imprimir una linea de guiones debajo
    ancho = max(len(t) for t in titulos)
    print("-" * ancho)
    for i in titulos:
        print(i.upper())

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
            case 'a': listadoTelefonos()
            case 'b': listadoTelefonosAlfabetico()
            case 'c': anadirContacto()
            case 'd': modificarTelefono()
            case 'e': buscarNumeroTelefono()
            case 'f': eliminarContacto()
            case 'g': borrarListinTelefonico()
            case 'h': 
                salir() 
                flag = False
            case _: 
                print("Opción no válida. Por favor, seleccione una opción del menú.")

menu()