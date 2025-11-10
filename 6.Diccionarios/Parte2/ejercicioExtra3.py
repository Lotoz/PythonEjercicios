#Para este ejercicio se ha considera que el mes es de 30 dias
#El analisis sera con 4 productos, llamados A, B, C, D
#Empezaremos vendiendolos por 5 dias

#No afecta que sea asi y se ve mejor
ventas = { 
    "A": {
        1: 5, 
        2: 3, 
        3: 6, 
        4: 8, 
        5: 1
        }, 
    "B": {
        1: 3, 
        2: 7, 
        3: 2, 
        4: 0, 
        5: 4
        }, 
    "C": {
        1: 6, 
        2: 4, 
        3: 3, 
        4: 5, 
        5: 2
        }, 
    "D": {
        1: 0, 
        2: 2, 
        3: 1, 
        4: 3, 
        5: 0
        } 
}
#Creamos una funcion que suma las unidades de un diccionario
#Con esto se recorre el array entero
  #print(f'{letra} = ind = {ind} numero = {numero}')

#Segun la letra calcula lo siguiente
#Calcula la suma total del producto
def sumaTotal(buscado):
    suma = 0
    for letra,valor in ventas.items():
        if (letra == buscado):
            for ind,numero in valor.items():
                suma += numero
    return suma

ventasA = sumaTotal("A")
ventasB = sumaTotal("B")
ventasC = sumaTotal("C")
ventasD = sumaTotal("D")

#*varios indica que son varios componentes, es igual que args en java
#todo se mete en un array
def esMaxMenor(*varios):
    menor = 1 #Numero mas pequeno posible suponiendo si son positivos
    for numero in varios:
        if(menor < numero):
            menor = menor
        else:
            menor = numero  
    return menor

def esMaxMayor(*varios):
    mayor = 1000000000000000000000 #numero grande para logica
    for numero in varios:
        if(mayor < numero):
            mayor = numero
        else:
            mayor = mayor
    return mayor





      
        