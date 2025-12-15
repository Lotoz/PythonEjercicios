# 03_herencia.py

# Clase Padre (Superclase)
class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre

    def atacar(self):
        return "El personaje ataca con los puños."

# Clase Hija (Subclase) -> Hereda de Personaje
class Guerrero(Personaje):
    def __init__(self, nombre, espada):
        # super() llama al __init__ de la clase padre para no repetir código
        super().__init__(nombre) 
        self.espada = espada

    # SOBREESCRITURA (Overriding): Cambiamos el comportamiento del padre
    def atacar(self):
        return f"{self.nombre} ataca con su {self.espada}!"

class Mago(Personaje):
    def atacar(self):
        return f"{self.nombre} lanza una bola de fuego!"

# --- USO ---
if __name__ == "__main__":
    g = Guerrero("Conan", "Espada Bastarda")
    m = Mago("Gandalf")

    # Ambos tienen 'nombre' porque heredaron de Personaje
    print(g.atacar()) # Usa su propia versión de atacar
    print(m.atacar()) # Usa su propia versión de atacar