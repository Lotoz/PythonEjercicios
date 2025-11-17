
numero = int(input("Dame un numero impar:"))
while (numero % 2 == 0):
    numero = int(input("Dame un numero impar:"))
for i in range(1, numero + 1, 2):
    espacios = (numero - i) // 2
    print(" " * espacios + "*" * i )