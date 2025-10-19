import rombo
import adivina
import ecucacion 
import tablaDeNumeros
import fibonacci
import tablaMultiplicar
import factorial

def imprimeError(opcion):
    print(f"La {opcion} no es una opcion valida, por favor ingrese una opcion correcta")

def imprimeMenu():
    menu = [
        "_"*15,
       "MENU DE OPCIONES",
        "a)Mostrar Rombo",
        "b)Adivinar un numero",
        "c)Resolver una ecuacion de segundo grado",
        "d)Tabla de numeros",
        "e)Calculo del numero factorial de un numero",
        "f)Calculo de un numero de la sucesion de Fibonacci",
        "g)Tabla de multiplicar",
        "h)Salir"
        ]
    for i in (menu):
        print(i)

def menu():
    flag = False
    while(flag == False):
        imprimeMenu()
        opcion = input("")
        opcion.lower
        match opcion:
            case 'a':
                rombo.mostrarRombo()
            case 'b':
                adivina.adivinaNumero()
            case 'c':
                ecucacion.resuelveEcuacion()
            case 'd':
                tablaDeNumeros.tablaNumeros()
            case 'e':
                factorial.calculoFactorial()
            case 'f':
                fibonacci.sucesionFibonacci()
            case 'g':
                tablaMultiplicar.tablaMultiplicar()
            case 'h':
                flag = True
            case _:
                imprimeError(opcion)
   


menu()
