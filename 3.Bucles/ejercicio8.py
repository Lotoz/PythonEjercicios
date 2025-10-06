numero = int(input("Introduce un numero para saber si es primo:"))

flag = False
contador = 2
while(flag == False & contador < numero):
    if(numero % contador == 0):
        flag = True
    contador += 1

if(contador >= numero):
    print("Es primo")
else:
    print("No es primo")