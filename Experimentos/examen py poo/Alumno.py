from Persona import Persona
from enum import Enum

class Nivel(Enum):
    Principiante = "Principiante"
    Medio = "Medio"
    Avanzado = "Avanzado"
    @classmethod
    def es_valido(cls, valor: str) -> "Nivel":
        for nivel in cls:
            if nivel.value == valor:
                return nivel
        raise ValueError("Error: nivel no válido")
    
class Alumno(Persona):
    def __init__(self, nombre, email, edad: int, nivel: str) -> None:
        super().__init__(nombre, email)
        if edad < 0:
            raise ValueError("Error: el alumno no puede ser menor de 0 años")
        self.edad = edad
        try:
            self.nivel = Nivel.es_valido(nivel)
        except ValueError:
            raise ValueError(f"Error, ese nivel no es posibel {nivel}")
        self.nota: list[float] = []
    
    def getEdad(self) -> int:
        return self.edad
    
    def setEdad(self, edad) -> None:
        if edad < 0:
            raise ValueError("Error: el alumno no puede ser menor de 0 años")
        self.edad = edad
    
    def getNivel(self) -> "Nivel":
        return self.nivel

    def setNivel(self, nivel) -> None:
        try:
            self.nivel = Nivel.es_valido(nivel)
        except ValueError:
            raise ValueError(f"Error, ese nivel no es posibel {nivel}")
    
    def getNota(self) -> list:
        return self.nota
    
    def __str__(self) -> str:
        return(
            f"Alumno: \n"
            + super().__str__() + "\n"
            + f"Edad: {self.getEdad()} \n"
            + f"Nivel: {self.getNivel().value} \n"
            + f"Nota: {self.getNota()}"
        )