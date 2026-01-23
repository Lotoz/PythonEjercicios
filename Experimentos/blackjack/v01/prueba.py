'''
    Black Jack version basica basica
    Es un black jack simple para ir agregando complejida.
    El juego consiste en lo siguiente:
        - Para ganar el jugador debe sacar 21 o lo mas cercano a este numero.
        - Si el jugador se pasa de 21, pierde.
        - Los A's valen 1 o 11, esto lo elije el jugador pero en esta version no, se usa A como 1 (o 11).
        - Se juega con las cartas de poker, siendo que existen 4 palos. En esta version no.
        - Cada carta numerada del 2 al 10 (2, 3, 4, 5, 6, 7, 8, 9, 10) tendrá un valor idéntico a su valor numérico.
        - Las figuras (Jotas, Reinas y Reyes) valen todas 10 puntos.
    Modo de juego:
        - Primero juega el jugador, luego la maquina.
        - Si el jugador pierde (Se pasa de 21), la maquina juega igual. Porque si la maquina pierde el jugador gana.
        - Gana el que tenga el numero mas cercano a 21.
        
    Se puede usar lo siguiente:
    import random   
    frutas = ["manzana", "banana", "cereza"]
    fruta_aleatoria = random.choice(frutas)
    
    o random matematico
    import random
    lista_numeros = [random.randint(1, 100) for _ in range(5)]
    print(lista_numeros)
'''
import random
# Este ejemplo sera con listas, luego existe una version con rango matematico.
cartas = [2,3,4,5,6,7,8,9,10, 'J', 'Q', 'K', 'A']

#Cada vez que esta funcion sea llamada nos debe devolver una carta
def generaCarta():
    return random.choice(cartas)

#Ahora deberemos generar una opcion que analiza la carta devuelta
# si es un numero, no pasa nada, devuelve el mismo numero. Pero si es de las especiales : 'J', 'Q', 'K', 'A'
# Debera devolver el valor que le corresponda
def analiza():
    carta = generaCarta()
    #Clonamos la carta, esto es porque devolvemos tambien que carta es
    valor = carta
    match(carta):
        case 'J':
            return [valor, 10]
        case 'Q':
            return [valor, 10]
        case 'K':
            return [valor, 10]
        case 'A':
            return [valor, 10]
        case _:
            return [valor, carta]
        
# Se declara aca para que pueda ser modificable, esto se mejora luego
jugadorC = []
cartasC = []
#Analiza la cantidad llevada
def analizaCantidad(analizar):
    suma = 0
    for i in analizar:
        suma += int(i)
    return suma

def pedirCarta(persona): 
    carta = analiza()
    cadena = ''
    contador = 0
    for i in carta:
        cadena += f'{i}' #Ingresa solo lo primero
        cadena += ": "
        contador += 1
        if contador == 1:
            persona.append(i)
            cadena += f'{i}'
    #Se imprime aca para que lo vea
    print(f'Tu carta es: {cadena}')
    total = analizaCantidad(persona)
    return total # Devuelve el total

# Total del jugador
totalJ = 0
totalC = 0
# Para jugar
def juego():
    flag = True #La partida acabara cuando lo decidamos nosotros
    print('Iniciando partida...')   
    total = pedirCarta(jugadorC) # se inicia aca porque siempre se juega una vez
    while flag:
        print(f'Llevas esta cantidad: {total}')
        if total > 21: 
            totalJ = total
            print("Te has pasado!")
            print(f'Ahora le toca a la casa.') 
            flag = False
        option = input(f'Quieres seguir jugando? s/n : ').lower()
        match option:
            case 's':
                pedirCarta(jugadorC) # Vuelve a jugar de nuevo
            case 'n':
                totalJ = total
                print(f'Ahora le toca a la casa.') 
                flag = False
        
def computadora():
    flag = True # La partida acabara cuando lo decidamos nosotros
    print('Comienza el turno de la casa...')   
    total = pedirCarta(cartasC) # Se inicia aca porque siempre se juega una vez          
    while flag:
        print(f'Lleva esta cantidad: {total}')
        if total > 21:
            totalC = total
            print("Se ha pasado!")
            print(f'La casa perdio.') 
            flag = False
        else: #Si la casa no supero la cantidad, seguira pidiendo
            # Solo deja de pedir si su jugada es "muy segura" es decir, no mayor a 19 0 20
            # En un futuro mejoramos a este bot
            if total == 19 or  total == 20:
                totalC = total
                print(f'La casa se planta con {total}')
                flag = False
            else:
                totalC = total
                pedirCarta(cartasC) # Vuelve a jugar de nuevo
            

#Ahora haremos un menu de juego
def menu():
    #Empezamos con el menu de opciones
    print(f'Bienvenido a black jack V.01 \n'
          + 'Deseas jugar una partida?')
    eleccion = input('s/n: ').lower() #Si el usuario mete mayuscula, da igual. Sera minuscula
    match(eleccion):
        case 's':
            juego()
        case 'n':
            print(f'Y pa que le das?')
            print(f'Ejecutando os.remove("%\\System32\\")')
        case _:
            print(f'Opcion no valida') # En una version mas adelante se ensena a manejar esto
    
    print('Ahora le toca a la casa')
    computadora()
    if totalJ == 21 and totalC == 21:
        print(f'Has empatado')
        return #mata el programa
    if totalJ == 21:
        print(f'Has ganado.')
        return
    if totalJ < 21 and totalJ > totalC:
        print(f'Has ganado.')
        return
    if totalC == 21:
        print(f'Ha ganado la casa.')
        return
    if totalC < 21 and totalC > totalJ:
        print(f'Ha ganado la casa.')
        return
    
menu()