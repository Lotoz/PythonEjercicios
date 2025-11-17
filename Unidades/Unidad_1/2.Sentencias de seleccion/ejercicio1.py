#Analiza si es par o impar
def parImpar(number) :
    text = "El numero %d" %(number)
    if number % 2 == 0:
        print(text + " es par")
    else:
        print(text + " es impar")

#Le pedimos al usuario
numero = int(input("Introduce un numero: "))
parImpar(numero)