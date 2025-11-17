def calificacion(numero):
    match numero:
        case 5 :
            imprimir("suficiente")
        case 6:
            imprimir("bien")
        case 7 | 8:
            imprimir("notable")
        case 9:
            imprimir("sobresaliente")
        case 10:
            imprimir("matricula de honor")
        case _:
            print("Calificacion incorrecta.")

def imprimir(calificacion):
    print(f"Su calificacion es {calificacion}")

numero = int(input("Introduce la calificacion: "))
calificacion(numero)