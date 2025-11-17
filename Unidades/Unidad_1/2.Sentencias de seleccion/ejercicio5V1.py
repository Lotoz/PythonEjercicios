def precioEntrada(edad):
    if edad < 5:
        print(f"Su entrada es gratis.")
        return 0;
    elif edad >= 5 and edad < 18:
        print(f"La entrada vale 3$.")
        return 3;
    elif edad >= 18 and edad < 65:
        print(f"La entrada vale 6$.")
        return 6;
    else:
        print(f"Su entrada es gratis.")
        return 0;

def museoApp(entrada):
    while entrada != 'F':
        edad = int(input("Introduzca la edad:"))
        numero = precioEntrada(edad)
        
    print(f"El precio total a pagar es de: {cantidad}")

entrada = input("Introduzca cualquier letra menos f.")
museoApp(entrada)