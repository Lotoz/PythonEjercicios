def mostrarRombo():
    numero = int(input("Dame un numero: "))
    for i in range(numero):
        print(" " * (numero - i - 1) + "*" * (2 * i + 1))
    for i in range(numero - 2, -1, -1):
        print(" " * (numero - i - 1) + "*" * (2 * i + 1))       
