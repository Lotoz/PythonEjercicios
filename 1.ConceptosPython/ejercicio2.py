#Recoje 2 numeros enteros y muestra por teclado los siguientes resultados
numero1 = int(input("Introduce un numero:"))
numero2 = int(input("Introduce otro numero:"))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
if numero2 == 0:
    print("No se puede dividir entre cero")
else: 
    divisionReal = numero1 / numero2
    divisionEntera = numero1 // numero2
    divisionModulo = numero1 % numero2

potencia = numero1 ** numero2
print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicacion: ", multiplicacion)
print("Division real: ", divisionReal)
print("Division entera: ", divisionEntera)
print("Division modulo: ", divisionModulo)
print("Potencia: ", potencia)