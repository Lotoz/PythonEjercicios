from abc import ABC, abstractmethod
from Alumno import Alumno

class Evaluable(ABC):
    @abstractmethod
    def evaluarAlumno(self, alum: Alumno)-> None:
        pass
