from Personaje import Personaje

class Mago(Personaje):
    def __init__(self, nombre):
        # El mago tiene poca vida (60) pero un dado de 20 caras (hechizos potentes)
        super().__init__(nombre, vida_maxima=60, caras_dado=20)

    # 5. POLIMORFISMO (Implementación propia de atacar)
    def atacar(self, objetivo):
        dano = self.arma.drop()
        print(f"{self.nombre} (Mago) lanza una bola de fuego! Daño: {dano}")
        objetivo.recibir_dano(dano)


class Guerrero(Personaje):
    def __init__(self, nombre):
        # El guerrero tiene mucha vida (100) y un dado de 8 caras
        super().__init__(nombre, vida_maxima=100, caras_dado=8)

    def atacar(self, objetivo):
        dano = self.arma.drop() + 2  # Bono fijo de fuerza
        print(f"{self.nombre} (Guerrero) ataca con su espada! Daño: {dano}")
        objetivo.recibir_dano(dano)