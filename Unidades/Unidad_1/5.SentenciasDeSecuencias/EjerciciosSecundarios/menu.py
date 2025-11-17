#imports
import ejercicio1
import ejercicio2
import ejercicio3
import ejercicio4
import ejercicio5
import ejercicio6
import ejercicio7
import ejercicio8
import ejercicio9
import ejercicio10
import ejercicio11

#funciones
def imprimeMenu():
    menu = [
        "-"*15,
        "A) Ejercicio 1",
        "B) Ejercicio 2",
        "C) Ejercicio 3",
        "D) Ejercicio 4",
        "E) Ejercicio 5",
        "F) Ejercicio 6",
        "G) Ejercicio 7",
        "H) Ejercicio 8",
        "I) Ejercicio 9",
        "J) Ejercicio 10",
        "K) Ejercicio 11",
        "L) Salir"
    ]
    for i in(menu):
        print(i)

def imprimeError(opcion):
    print(f'La {opcion} es incorrecta. Ingresa una valida.')

def menu():
    flag = True
    while(flag == True):
        imprimeMenu()
        opcion = input("Ingresa una opcion")
        opcion = opcion.upper()
        match opcion:
            case "A":
                ejercicio1.app()
            case "B":
                ejercicio2.app()
            case "C":
                ejercicio3.app()
            case "D":
                ejercicio4.app()
            case "E":
                ejercicio5.app()
            case "F":
                ejercicio6.app()
            case "G":
                ejercicio7.app()
            case "H":
                ejercicio8.app()
            case "I":
                ejercicio9.app()
            case "J":
                ejercicio10.app()
            case "K":
                ejercicio11.app()
            case "L":
                flag = False
            case _: 
                imprimeError(opcion)

menu()