import datetime 

def saludaBot(hora, nombre):
    if hora > 7 and hora <= 12:
        print(f"Buenos dias {nombre}!")
    elif hora > 12 and hora <= 20:
        print(f"Buenos tardes {nombre}!")
    else:
        print(f"Buenos noches {nombre}!")

hora = datetime.datetime.now()
nombre = input("Dime tu nombre: ")
saludaBot(hora.hour, nombre)