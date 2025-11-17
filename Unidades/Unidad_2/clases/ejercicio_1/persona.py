class Persona:
    #! Por asi, decirlo, el constructor
    def __init__(self,name, direccion, tel):
        self._name = name #? Es la forma de dar los atributos al objeto creado
        self._direccion = direccion
        self._tel = tel

    #* getters del objeto
    def get_name(self):
        return self._name
    
    def get_dirreccion(self):
        return self._direccion
    
    def get_tel(self):
        return self._tel
    
    #* setters del objeto
    def set_name(self, newName):
        self._name = newName
        
    def set_dirrecion(self, newDir):
        self._direccion = newDir
    
    def set_tel(self,newTel):
        self._tel =  newTel
    
    #* El toString
    def mostrarPersona(self):
        return '*Nombre: ' + self._name + '\n' + '  - Dirrecion: ' +  self._direccion +  '\n' + '  - Tel:' + self._tel
    