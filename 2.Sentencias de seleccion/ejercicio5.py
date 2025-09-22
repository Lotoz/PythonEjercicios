def precioEntrada(edad):
    if edad < 5:
        print(f"Su entrada es gratis.")
    elif edad >= 5 and edad < 18:
        print(f"La entrada vale 3$.")
    elif edad >= 18 and edad < 65:
        print(f"La entrada vale 6$.")
    else:
        print(f"Su entrada es gratis.")

edad = int(input("Introduzca la edad: ")) 