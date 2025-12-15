from Personaje import Personaje

class Orco(Personaje):
    def __init__(self):
        super().__init__("Orco Gruñón", vida_maxima=70, caras_dado=10)

    def atacar(self, objetivo):
        dano = self.arma.tirar()
        print(f"{self.nombre} golpea con su garrote! Daño: {dano}")
        objetivo.recibir_dano(dano)

class Dragon(Personaje):
    def __init__(self):
        super().__init__("Smaug", vida_maxima=120, caras_dado=12)

    def atacar(self, objetivo):
        # El dragón tiene una probabilidad de crítico
        dano = self.arma.drop()
        if dano > 10:
            print("¡GOLPE CRÍTICO! El dragón escupe fuego intenso.")
            dano += 5
        print(f"{self.nombre} ataca con garras! Daño: {dano}")
        objetivo.recibir_dano(dano)