import random
def adivinaNumero():
    adivina = random.randint(1,100)
    numero = int(input("Adivina el numero! "))
    while(adivina != numero):
        if (numero > adivina):
            print("Has ingresado un numero mayor. Pon uno mas pequeno!")
            numero = int(input("Adivina el numero! "))
        elif(numero < adivina):
            print("Has ingresado un numero menor. Pon uno mas grande!")
            numero = int(input("Adivina el numero! "))
    
    print("Lo has acertado!")
