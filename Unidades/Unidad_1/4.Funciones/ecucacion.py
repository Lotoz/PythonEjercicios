import math

def resuelveEcuacion():
    print(f"Resuelve ecuaciones de segundo grado")
    variableA = float(input("Dame el valor A: "))
    variableB = float(input("Dame el valor B: "))
    variableC = float(input("Dame el valor C: "))
    if(variableA == 0 and variableB == 0):
        print("No es una ecuacion lo planteado.")
        print("Tecnicamente el valor es C: ",  variableC)
    elif (variableA == 0):
        x = -(variableC) / variableB
        print("La x vale: ", x)
    elif (variableB == 0):
        determinante = -(variableC)/variableA   
        if determinante < 0: 
            print("No tiene solucion")
        else:
            x = math.sqrt(determinante)
            print("La primera x vale 0")
            print("La primera x vale: ", x)
    elif (variableC == 0):
        x1 = -(variableB) / variableA
        x2 = -(-(variableB) / variableA)
        print(f"Las raices son ",x1, " y ", x2)
    else:
        determinante = math.pow(variableB,2) - 4 * variableA * variableC
        if (determinante > 0):
            x1 = (-variableB + math.sqrt(determinante)) / 2 * variableA
            x2 = (variableB + math.sqrt(determinante)) / 2 * variableA
            print(f"El valor de x1 =",x1)
            print(f"El valor de x2 =",x2)
        else:
            print(f"No tiene solucion.")