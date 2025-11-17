class Persona:

    def __init__(self, name, surname, dni, age):
        self._name = name
        self._surname = surname
        self._dni = dni
        self._age = age

    #* getters del objeto
    def get_name(self):
        return self._name
    
    def get_surname(self):
        return self._surname
    
    def get_dni(self):
        return self._dni
    
    def get_age(self):
        return self._age
    
    #* setters del objeto
    def set_name(self, newName):
        self._name = newName
    
    def set_surname(self, newSurname):
        self._surname = newSurname
    
    def set_dni(self, newDni):
        self._dni = newDni
    
    def set_age(self, newAge):
        self._age = newAge
    
    #*Metodos de validacion
    '''Verifica la cadena. Si es vacia devuelve error personalizado.
        Si no esta vacia, la devuelve mayuscula
    '''
    def verificaCadena(cadena):
        if not cadena:
            raise 'Nombre no valido'
        else:
            return cadena.upper()
    
    #* El toString
    def mostrarPersona(self):
        return '*Nombre: ' + self._name + '\n' + '*Apellido: ' +  self._surname +  '\n' + '  - DNI :' + self._dni + '\n' +  '  - Edad: ' + self._age
    
    #* Metodos extras
    def isOlder(edad):
        if edad > 18:
            return True
        else:
            return False