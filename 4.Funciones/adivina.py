import random
def adivinaNumero():
    adivina = random.randint(1,100)
    numero = int(input("Adivina el numero! "))
    while(adivina != numero):
        if (numero > adivina):
            print("Es menor al que tienes que adivinar.")
            numero = int(input("Adivina el numero! "))
        elif(numero < adivina):
            print("Es mayor al que tienes que adivinar.")
            numero = int(input("Adivina el numero! "))
    
    print("Lo has acertado!")

