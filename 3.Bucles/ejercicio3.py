numero = int(input("Introduce un número(cero para finalizar): "))

contador = 0
suma = 0
maximo = 0
minimo = 0
while numero != 0:
    suma += numero
    contador += 1
    if numero > maximo:
        maximo = numero
    if minimo == 0 or numero < minimo:
        minimo = numero
    numero = int(input("Introduce un número: "))

print("Has introducido", contador)
print("La suma de los números es", suma)
print("La media de los números es", round(suma / contador, 2))
print("El máximo es", maximo)
print("El mínimo es", minimo)