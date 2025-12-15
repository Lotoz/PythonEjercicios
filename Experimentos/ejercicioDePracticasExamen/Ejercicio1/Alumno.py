from persona import Persona
from enum import Enum

# Excepciones personalizadas
class alumnoError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

# Enum para nivel
class Nivel(Enum):
    PRINCIPIANTE = 1
    MEDIO = 2
    AVANZADO = 3

class Alumno(Persona):
    # Aquí usamos métodos estáticos porque no necesitan acceder a 'self'.
    @staticmethod
    def verificaEdad(edad):
        if edad < 1:
            raise alumnoError("La edad no puede ser negativa")
        
    @staticmethod
    def verificaNivel(nivel_valor):
        if nivel_valor not in [1, 2, 3]:
            raise alumnoError("El nivel es inválido")
        elif  nivel_valor != int:
            raise alumnoError("El nivel es inválido")

    def __init__(self, id, nombre, email, edad, nivel): 
        super().__init__(id, nombre, email)
        #Verifica
        Alumno.verificaEdad(edad)
        Alumno.verificaNivel(nivel)
        
        self.edad = edad
        self.nivel = nivel

    # Getters
    def get_edad(self):
        return self.edad
    
    def get_nivel(self):
        return self.nivel
    
    def mostrar(self):
        return f"ID: {super().get_id()} \nNombre: {super().get_nombre()} \nEmail: {super().get_email()} \nEdad: {self.edad} \nNivel: {self.nivel}"