 #Generamos una funcion que calcule el factorial de un numero

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def calculoFactorial():
    numero = int(input("Introduce un numero para calcular su factorial: "))
    resultado = factorial(numero)
    print(f"El factorial de {numero} es {resultado}")
