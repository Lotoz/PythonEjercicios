import datetime 

def mesesPorDia(numero):
    match numero:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12 :
            print(f"El mes {numero} tiene 31 dias.")
        case 4 | 6 | 9 | 11:
            print(f"El mes {numero} tiene 30 dias.")
        case 2:
            anyoBisiesto(numero)
        case _:
            print("Mes no valido.")

def anyoBisiesto(numero):
    fecha = datetime.datetime.now()
    anyo = fecha.year
    if anyo % 4 == 0 :
        if anyo % 100 == 0:
            if anyo % 400 == 0:
                print(f"El {numero} el mes tiene 29 dias.")
            else: 
              print(f"El {numero} el mes tiene 28 dias.")  
        else:
           print(f"El {numero} el mes tiene 29 dias.")
    else:
        print(f"El {numero} el mes tiene 28 dias.")

numero = int(input("Introduce el mes: "))
mesesPorDia(numero)