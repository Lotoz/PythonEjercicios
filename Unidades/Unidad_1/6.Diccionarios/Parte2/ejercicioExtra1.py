#Le pregunta a un usuario su nombre edad dirrecion y telefono y lo guarda

#Le pedimos los datos al usuario
nombreEntrada = input('Dime tu nombre: ')
edadEntrada = int(input('Dime tu edad: '))
dirrecionEntrada = input('Dime tu dirrecion: ')
telefonoEntrada = int(input('Dime tu telefono: '))

#Primero deberemos crear un diccionario propio de esa persona
persona = {
    "Nombre" : nombreEntrada,
    "Edad" : edadEntrada,
    "Dirrecion" : dirrecionEntrada,
    "Telefono" : telefonoEntrada
}

#Imprimimos 
print(f'{persona.get('Nombre')} de {persona.get('Edad')} años, vive en {persona.get('Dirrecion')} y su numero es {persona.get('Telefono')}')
