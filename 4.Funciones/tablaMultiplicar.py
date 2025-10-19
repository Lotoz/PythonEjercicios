#Se pide un numero y se muestra su tabla de multiplicar por pantalla.
def tablaMultiplicar():
    numero = int(input("Dime un numero: "))
    print(f"Tabla de multiplicar del ", numero, "del 1 al 10:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
