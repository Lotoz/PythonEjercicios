from persona import Persona

# Excepciones personalizadas
class profesorError(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)

class Profesor(Persona):
    # Aquí usamos métodos estáticos porque no necesitan acceder a 'self'.
    @staticmethod
    def verificaEx(edad):
        if edad < 0:
            raise profesorError("La experiencia puede ser 0 pero no menor.")
        

    def __init__(self, id, nombre, email, especialidad, experiencia ): 
        super().__init__(id, nombre, email)
        self.especialidad = especialidad
        #Verifica
        Profesor.verificaEx(experiencia)
        self.experiencia = experiencia

    # Getters
    def get_experiencia(self):
        return self.experiencia
    
    def get_especialdiad(self):
        return self.especialidad
    
    def mostrar(self):
        return f"ID: {super().get_id()} \nNombre: {super().get_nombre()} \nEmail: {super().get_email()} \nExperiencia: {self.experiencia} \nEspecialdiad: {self.especialidad}"