#Funcion de fibonacci
def sucesionFibonacci():
    n = int(input("Ingrese la cantidad de numeros de la sucesion de Fibonacci que desea ver: "))
    a, b = 0, 1
    print("Sucesion de Fibonacci:")
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()
