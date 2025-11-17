import random
def tablaNumeros():
    filas = int(input("Ingrese el numero de filas: "))
    columnas = int(input("Ingrese el numero de columnas: "))
    
    for i in range(filas):
        for j in range(columnas):
            numero_aleatorio = random.randint(1, 100)
            print(f"{numero_aleatorio:4}", end=" ")
        print()  