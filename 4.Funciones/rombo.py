def mostrarRombo():
    numero = int(input("Dame un numero: "))
    for i in range(1, numero + 1, 2):
        espacios = (numero - i) // 2
        print(" " * espacios +"*" * i)
        
            