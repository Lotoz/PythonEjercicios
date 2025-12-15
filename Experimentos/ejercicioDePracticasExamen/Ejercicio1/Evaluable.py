from abc import ABC, abstractmethod

class Evaluable(ABC):

    # Implementa métodos de evaluación
    def evaluacion(self, nota):
        # Estructura: "Valor si True" if CONDICION else "Valor si False"
        return "Aprobado" if nota >= 5 else "Desaprobado"
