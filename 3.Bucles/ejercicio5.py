numero = int(input("Introduce un número: "))

cadena = ""

for i in range(numero):
    i += 1
    i_cadena = i * i
    #Siempre debes convertir a cadena para concatenar, no es como en java
    cadena += str(i_cadena) + " "


print(cadena)