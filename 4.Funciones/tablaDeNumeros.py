#Se debe pedir un número de filas y un número de columnas.  
#A  continuación,  mostrará  una  tabla  con  números  aleatorios  con  las  filas  y  
#columnas indicadas.
filas = int(input('Numero de filas: '))
cols = int(input('Numero de columnas: '))

for i in range(filas):
    for j in range(cols):
        print( str(i) + str(j))