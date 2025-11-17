def diasDeLaSemana(numero):
    match numero:
        case 1:
            imprimir("Lunes")
        case 2:
            imprimir("Martes")
        case 3:
            imprimir("Miercoles")
        case 4:
            imprimir("Jueves")
        case 5:
            imprimir("Viernes")
        case 6:
            imprimir("Sabado")
        case 7:
            imprimir("Domingo")
        case _:
            print("Dia incorrecto")

def imprimir(dia):
    print(f"El dia de la semana escogido es {dia}")

numero = int(input("Introduce un dia de la semana: "))

diasDeLaSemana(numero)