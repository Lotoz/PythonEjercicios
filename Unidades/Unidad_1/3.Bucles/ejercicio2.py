#Calcular el factorial de un número pedido al usuario
num = int(input("Introduce un número para calcular su factorial: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i

print("El factorial de", num, "es", factorial)