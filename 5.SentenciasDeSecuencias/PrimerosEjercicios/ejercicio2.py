def app():
    lista = []
    flag = False
    while (flag == False):
        palabra = input("Introduce una palabra: (Para finalizar no introduzcas nada) \n")
        palabra = palabra.lower()
        if(palabra == "" or palabra == " "):
            flag = True
        lista.append(palabra)
    
    #Ahora mostramos la lista
    cadena1 = ""
    #Aqui imprimimos normal
    for i in (lista):
        cadena1 += str("'"+i+"'") + " "
    #Impresion creciente
    cadena2 = ""
    lista.sort(reverse=False)
    for e in (lista):
        cadena2 += str("'"+e+"'") + " "
    #Impresion decreciente
    cadena3 = ""
    lista.sort(reverse=True)
    for u in(lista):
        cadena3 +=  str("'"+u+"'") + " "
    
    print("Normal: " + cadena1)
    print("Creciente: " + cadena2)
    print("Decreciente: " + cadena3)