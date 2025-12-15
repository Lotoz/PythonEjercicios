#Para crear clases abstractas
from abc import ABC, abstractmethod

class Persona(ABC):
    # Atributo de clase: compartido por todas las instancias
    _contador_id = 1
    #Constructor 
    def __init__(self,  nombre, email): 
        #Atributos
        self.id = Persona._contador_id
        Persona._contador_id += 1
        self.nombre = nombre
        self.email = email
    
    #Getters
    def get_nombre(self):
        return self.nombre

    def get_id(self):
        return self.id
    
    def get_email(self):
        return self.email
    
    #Mostrar
    @abstractmethod
    def mostrar(self):
        return f"ID : {self.id} \n Nombre: {self.nombre} \n Email: {self.email}" 
    
    