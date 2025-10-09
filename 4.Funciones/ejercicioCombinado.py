import rombo
import adivina
import ecucacion 
import tablaDeNumeros
import fibonacci
import tablaMultiplicar
import factorial

def imprimeError():
    print("La opcion es incorrecta")

def imprimeMenu():
    menu = [
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
                imprimeMenu()
            case 'b':
                adivina.adivinaNumero()
                imprimeMenu()
            case 'c':
                ecucacion.resuelveEcuacion()
                imprimeMenu()
            case 'd':
                tablaDeNumeros.tablaNumeros()
                imprimeMenu()
            case 'e':
                factorial.calculoFactorial()
                imprimeMenu()
            case 'f':
                fibonacci.sucesionFibonacci()
                imprimeMenu()
            case 'g':
                tablaMultiplicar.tablaMultiplicar()
                imprimeMenu()
            case 'h':
                flag = True
            case _:
                imprimeError()
                imprimeMenu()
   


menu()
