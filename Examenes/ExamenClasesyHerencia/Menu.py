from Funciones import *

def ImprimeTitulos():
    #Array de titulos
    titulos = [
        "---Menu Biblioteca---",
        "a) Agregar Material.", 
        "b) Listar Materiales.", 
        "c) Buscar Material por ID.", 
        "d) Eliminar Material.",
        "e) Generar Estadísticas.", 
        "f) Salir." ]
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
            case 'a': agregarUnMaterial() #Agrega o revista o libro darle eleccion al usuario
            case 'b': listarMateriales() # Lista todos los materiales del dic
            case 'c': buscarMaterialPorID() # Busca un material por ID
            case 'd': eliminarMaterialPorId() # Elimina un material existente por la ID en dic
            case 'e': generarEstadisticas() # Genera las estadiscticas
            case 'f': 
                salir() 
                flag = False
            case _: 
                print("Opción no válida. Por favor, seleccione una opción del menú.")

#Inicia el menu
menu()