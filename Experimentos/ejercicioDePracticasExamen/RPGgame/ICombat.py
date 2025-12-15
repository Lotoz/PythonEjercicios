from abc import ABC, abstractmethod

class ICombatiente(ABC):
    """
    Define el CONTRATO que todo ser que pelee debe cumplir.
    Sirve como la 'Interfaz de Ataque' que pediste.
    """
    @abstractmethod
    def atacar(self, objetivo):
        pass

    @abstractmethod
    def recibir_dano(self, cantidad):
        pass
