final = int(input("Dame un numero"))

#Inicio porque necesito iniciar en el numero menor para pillar la inversion
for inicio in range(final):
    for i in range(inicio, final-1, -1):
        if (i % 2 != 0):
            print(i)