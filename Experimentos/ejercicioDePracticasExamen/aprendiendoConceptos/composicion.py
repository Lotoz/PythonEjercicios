# 06_composicion.py

class Motor:
    def encender(self):
        return "Motor en marcha: Brrrumm!"

class Ruedas:
    def girar(self):
        return "Las ruedas giran."

# El Coche NO hereda de Motor, sino que TIENE un motor dentro.
class Coche:
    def __init__(self):
        # Composición: Creamos las instancias de otras clases DENTRO de esta
        self.motor = Motor() 
        self.ruedas = Ruedas()

    def conducir(self):
        inicio = self.motor.encender()
        movimiento = self.ruedas.girar()
        return f"{inicio} -> {movimiento}"

# --- USO ---
if __name__ == "__main__":
    mi_auto = Coche()
    # No necesitamos saber cómo funciona el motor, el coche lo gestiona
    print(mi_auto.conducir())