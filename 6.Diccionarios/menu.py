#Menu general de la aplicacion
#Estoy probando una nueva version alternativas de las otras

#Titulos del ejercicio
titulos = [
    "A) Listado de teléfonos, usando el orden por defecto",
    "b) Listado de teléfonos por orden alfabético.", 
    "c) Añadir un nuevo contacto.", 
    "d) Modificar el teléfono de un contacto.",
    "e) Buscar un número de teléfono.", 
    "f) Eliminar un contacto.", 
    "g) Borrar el listín telefónico.", 
    "h) Salir"
]
#Titulos en ingles
titles = [
    "A) Listado de teléfonos, usando el orden por defecto",
    "b) Listado de teléfonos por orden alfabético.", 
    "c) Añadir un nuevo contacto.", 
    "d) Modificar el teléfono de un contacto.",
    "e) Buscar un número de teléfono.", 
    "f) Eliminar un contacto.", 
    "g) Borrar el listín telefónico.", 
    "h) Salir"
]

#Traduce los ejercicios a ingles
def traduce():

#Imprime los titulos en mayuscula
def ImprimeTitulos(titulos):
    print("-"*titulos.lenght())
    for i in titulos:
        i = i.upper
        print(i)

#Funcion general de menu
def menu():