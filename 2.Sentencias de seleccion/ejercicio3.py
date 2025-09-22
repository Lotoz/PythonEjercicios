def comparaTres(num1, numero2, numero3):
    if num1 > numero2 and num1 > numero3:
        if numero2 > numero3:
            print(f"El numero {num1} es el mayor y el numero {numero3} es el menor")
        else:
            print(f"El numero {num1} es el mayor y el numero {numero2} es el menor")
    elif numero2 > numero3 and numero2 > num1:
        if numero3 < num1:
            print(f"El numero {numero2} es el mayor y el numero {numero3} es el menor")
        else:
            print(f"El numero {numero2} es el mayor y el numero {num1} es el menor")
    else:
        if num1 > numero2:
            print(f"El numero {numero3} es el mayor y el numero {numero2} es el menor")
        else:
            print(f"El numero {numero3} es el mayor y el numero {num1} es el menor")

numero1 = int(input("Primer numero: "))
numero2 = int(input("Segundo numero: "))
numero3 = int(input("Tercer numero: "))

comparaTres(numero1, numero2, numero3)
