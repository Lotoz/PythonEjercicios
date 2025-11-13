#Examen de python
#Importaciones
import random

#Reemplaza los vocales de una frase
def reemplazaVocales():
    frase = input('Ingresa una frase: ')
    #Array de las buscadas
    buscar = [
        'á','Á','a','A',
        'É','é','e','E',
        'o','Ó','ó','O',
        'u','U','ú','Ú']
    #Funcion que reemplaza lo buscado
    nueva = ''
    for i in frase:
        for e in buscar:
           #Si coincide lo sustituye
           if i == e:
               i = '*'
        #Si han coincidido ha cambiado i, si no, es la original
        nueva += i
    #Imprime el resultado
    print(f'{nueva}') 

#Pide numero y analiza si es mayor al anterior. y se deve introducir una cantidad
def pideNumero():
    flag = True
    while flag:
        try: 
            numero = int(input('Ingresa la cantidad de numeros: ')) 
            if numero <= 0:
                print('Ingrese un valor numerico y que sea mayor a 0.')
            else:
                comparaNumeros(numero) 
            flag = False         
        except:
            print('No es numerico el valor ingresado, se reiniciara el programa.')


def comparaNumeros(numero):
    flag = True
    while flag:
        try:
            #Para el bucle while
            contador = 1
            #Para comparar el numero anterior
            numeroVolatil = 0
            while contador <= numero:
                ingresado = float(input('Ingresa un numero: '))
                #No imprime el mensaje pero si esta obligando al usuario a repitir el numero
                if ingresado < numeroVolatil:
                    print(f'Debes introducir un numero mayor al anterior.')
                else:
                    contador += 1
                    #Almacenamos el numero volatil
                    numeroVolatil = ingresado
                flag = False
        except:
            print('Ingresa un valor numerico')
            
#Busca la palabra mas larga
def palabraLarga():
    frase = input('Ingresa una frase: ')
    frase = frase.split(" ")
    larga = ''
    for i in frase:
        if i > larga:
            larga = i
    print(f'La palabra mas larga es {larga}')

#Para imprimir el triangulo
def imprimeRectangulo():
    flag = True
    while flag:
        try:
            filas = int(input("Ingrese el numero de filas: "))
            columnas = int(input("Ingrese el numero de columnas: "))
            #Recorremos para imprimir
            for i in range(filas):
                for j in range(columnas):
                    #Numero aleatorios
                    numero_aleatorio = random.randint(1, 100)
                    print(f"{numero_aleatorio:4}", end=" ")
                print() 
            flag = False
        except:
            print('No es numerico el valor ingresado, ingresa un valor numerico entero.')

#Cuenta las apariciones en una palabra
def cuentaApariciones():
    palabra = input('Ingresa una palabra a contar: ')
    dic = {}
    lista = []
    #Metemos cada letra en el diccionario con valor 0
    for i in palabra:
        for e in palabra:
            if i == e:
                lista.append(i)
    #Cuando ya tengamos una lista con las letras repetidas volvemos a recorrer
    for r in lista:
        numero = palabra.count(r)
        #Guardamos los valores para luego mostrar el diccionario
        dic[r] = numero
    #Imprimimos el diccionario
    for letra, valor in dic.items():
        print(f'{letra} : {valor}')
    
  
#Imprime los ti1tulos en mayuscula
def ImprimeTitulos():
    #Array de titulos
    titulos = [
        'Menu de opciones',
        'a) Reemplazar vocales de una frase',
        'b) Mensaje cuando el numero introducido no sea mayor que el primero',
        'c) Encontrar la primera palabra más larga',
        'd) Mostrar rectángulo con números impares entre 0 y 100',
        'e) Contar la aparición de cada carácter en una palabra.',
        'f) Salir'
    ]
    #Guarda el ancho de titulos para generar una linea mas prolija
    ancho = max(len(t) for t in titulos)
    print("-" * ancho)
    #Recorre la lista e imprime los titulos en mayuscula
    for i in titulos:
        print(i)

#Funcion general de menu
#Es para la seleccion de opciones, devuelve la opcion seleccionada y tratada
def selectorOpciones():
    #Tambien imprime los titulos cada vez que se ejecuta
    ImprimeTitulos()
    opcion = input("Seleccione una opción: ").lower()
    return opcion

#Para salir del menu
def salir():
    print("Saliendo del programa...")

#Funcion del menu
def menu():
    flag = True
    while flag:
        match(selectorOpciones()):
            case 'a': reemplazaVocales()
            case 'b': pideNumero()
            case 'c': palabraLarga()
            case 'd': imprimeRectangulo()
            case 'e': cuentaApariciones()
            case 'f': 
                salir() 
                flag = False
            case _: 
                print("Opción no válida. Por favor, seleccione una opción del menú.")

#Inicia el menu
menu()