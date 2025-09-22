def division(dividiendo, divisor):
    if divisor != 0:
        print(f"El dividiendo es {dividiendo}, el divisor es {divisor} y el resultado es {dividiendo/divisor}")
    else:
        print(f"El divisor no puede ser 0.")

dividiendo = float(input("Introduce el dividiendo: "))
divisor = float(input("Introduce el divisor: "))

division(dividiendo, divisor)