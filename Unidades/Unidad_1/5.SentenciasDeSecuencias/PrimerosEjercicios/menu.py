#Import de los diferentes ejercicios
import ejercicio1
import ejercicio2
import ejercicio3
import ejercicio4

#Funciones del menu
def imprimeMenu():
    menuOpciones = [
        "-"*15,
        "A) Ejercicio 1",
        "B) Ejercicio 2",
        "C) Ejercicio 3",
        "D) Ejercicio 4",
        "H) Salir."
    ]
    for i in (menuOpciones):
        print(i)

def mostrarError(opcion):
    print(f"La {opcion} es incorrecta. Seleccione una opcion correcta del menu.")

def menu():
    flag = True
    while (flag == True):
        imprimeMenu()
        opcion = input("Elige una opcion del menu \n")
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
            case "H":
                flag = False
            case _:
                mostrarError(opcion)

menu()