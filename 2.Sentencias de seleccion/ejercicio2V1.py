dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

def recorreLista(numero):
    if numero < 8:
        print("El dia es: " + dias[numero-1])
    else:
        print("Numero no valido.")

numero = int(input("Ingresa un numero: "))

recorreLista(numero)
