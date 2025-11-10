#Menu general de la aplicacion
#Estoy probando una nueva version alternativas de las otras

#Import de funciones
#Importa directamente las funciones necesarias
# Y no haria falta poner el prefijo funciones.
from funciones import listadoTelefonos


#Imprime los titulos en mayuscula
def ImprimeTitulos():
    #Array de titulos
    titulos = []
    #Pincha el ancho de titulos para generar una linea mas prolija
    ancho = max(len(t) for t in titulos)
    print("-" * ancho)
    #Recorre la lista e imprime los titulos en mayuscula
    for i in titulos:
        #En caso de no querer mayuscula solo poner i
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
            case 'a': selectorOpciones() #Meter funciones asi de manera tranqui
            #case '@': etc
            case 'h': 
                salir() 
                flag = False
            case _: 
                print("Opción no válida. Por favor, seleccione una opción del menú.")

#Inicia el menu
menu()