from ICombat import ICombatiente
from Dice import Dice

class PersonajeError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Personaje(ICombatiente):

    def __init__(self, nombre, vida_maxima, caras_dado):
        self.nombre = nombre
        if vida_maxima < 0:
            raise PersonajeError('La vida debe ser mayor a 0')
        else:    
            self._vida_maxima = vida_maxima  # Atributo protegido (convención)
        self.__vida = vida_maxima        # Atributo PRIVADO (doble guion bajo)
        self.arma = Dice(caras_dado)

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self.__vida = 0
        elif valor > self._vida_maxima:
            self.__vida = self._vida_maxima
        else:
            self.__vida = valor

    @property
    def esta_vivo(self):
        return self.__vida > 0

    # Implementación base de recibir daño
    def recibir_dano(self, cantidad):
        self.vida -= cantidad  # Usa el setter automáticamente
        print(f" > {self.nombre} recibe {cantidad} de daño. Vida restante: {self.vida}/{self._vida_maxima}")
