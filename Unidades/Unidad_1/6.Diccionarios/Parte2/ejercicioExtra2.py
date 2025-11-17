#print(f'{persona.get('Nombre')} de {persona.get('Edad')} años, vive en {persona.get('Dirrecion')} y su numero es {persona.get('Telefono')}')

personas = {}

def creaDiccionario(contador, nombre, edad, dirrecion, telefono):
    #Creamos un diccionario peque de esa persona
    persona = {
        "Nombre" : nombre,
        "Edad" : edad,
        "Dirrecion" : dirrecion,
        "Telefono" : telefono
    }
    #cadena = "persona "+ str(contador)
    personas[contador] = persona
#Intentar luego imprimir como en el texto 1
def imprimeDiccionario():
    for numero,persona  in personas.items():
            print(f"{numero}.{persona.get('Nombre')} tiene {persona.get('Edad')} años, vive en {persona.get('Dirrecion')} y su numero de telefono es {persona.get('Telefono')} ")
            #for persona, valor in persona.items():
                #print(f"{persona} : {valor}")

def menu():
    print('Crea un diccionario de personas')
    flag = True
    contador = 1
    while flag:
        #Se piden los datos de la persona
        nombre = input('Dame el nombre de la persona: ')
        edad = int(input('Dame la edad de la persona: '))
        dirreccion = input('Dame la dirrecion de la persona: ')
        telefono = int(input('Dame el telefono de la persona: '))

        creaDiccionario(contador,nombre, edad, dirreccion, telefono)

        respuesta = input('Quieres seguir agregando personas? (s/n) ')
        respuesta = respuesta.lower()
        match respuesta:
            case 's': 
                print('Perfecto! ahi vamos.') 
                contador += 1
            case 'n': 
                imprimeDiccionario()
                flag = False
            case _: 
                print('Valor invalido. Finalizando de emergencia.')
                flag = False
        
        
        
menu()