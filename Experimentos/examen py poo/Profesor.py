from Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre: str, email: str, especialidad: str, experiencia: int) -> None:
        super().__init__(nombre, email)
        if experiencia < 0:
            raise ValueError("Error, la experiencia no puede ser negativa")
        elif especialidad == "" or especialidad.isspace():
            raise ValueError("Error: especialidad indicada no existe")
        self.especialidad = especialidad
        self.experiencia = experiencia

    def getEspecialidad(self) -> str:
        return self.especialidad

    def setEspecialidad(self, especialidad) -> None:
        if especialidad == "" or especialidad.isspace():
            raise ValueError("Error: especialidad indicada no existe")
        self.especialidad = especialidad
    
    def getExperiencia(self) -> int: 
        return self.experiencia
    
    def setExperiencia(self, experiencia) -> None:
        if experiencia < 0:
            raise ValueError("Error, la experiencia no puede ser negativa")
        self.experiencia = experiencia
    
    def __str__(self):
        return(
        f"Profesor: \n"
        + super().__str__()
        + f"\n Especialidad: {self.getEspecialidad()} \t"
        + f"Años de experiencia: {self.getExperiencia()} años"
        )