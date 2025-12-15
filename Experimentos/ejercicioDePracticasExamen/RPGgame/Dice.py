import random
# Clase dado
# Es el que usaran para atacar
class DiceError(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Dice:

    def __init__(self, faces):
        if faces > 0:
            self.faces = faces
        else:
            raise DiceError('Number not valid.')
        
    def drop(self):
        return random.randint(1, self.faces)