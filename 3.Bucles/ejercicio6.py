filas = int(input("Introduce un número para las filas: "))
columnas = int(input("Introduce un número para las columnas: "))

#si el usuario ha introducido dos filas y dos columnas,
#Debo imprimir una tabla de 2x2, que contenga 1, 2, 3  y 4

for i in range(1, filas * columnas + 1):
    #f"{i:2}" significa que el número i se imprime en un campo de 2 caracteres, es un tipo de formateo
    print(f"{i:2}", end="")
    if i % columnas == 0:
        print() 

#Esto se podria hacer del siguiente modo
# for i in range(1, filas + 1):
#     for j in range(1, columnas + 1):
#         print(f"{(i - 1) * columnas + j:2}", end
#     print()

