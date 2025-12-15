# 01_clases.py

class Personaje:
    """
    Una CLASE es como un plano o molde. Define atributos (datos)
    y métodos (comportamiento) que tendrán los objetos creados a partir de ella.
    """

    # El método __init__ es el CONSTRUCTOR.
    # Se ejecuta automáticamente al crear un nuevo objeto (instancia).
    # 'self' hace referencia a la instancia actual que se está creando.
    def __init__(self, nombre, nivel):
        # Atributos de instancia (propios de cada objeto)
        self.nombre = nombre
        self.nivel = nivel
        self.esta_vivo = True

    # MÉTODOS: Funciones que pertenecen a la clase
    def saludar(self):
        return f"Hola, soy {self.nombre} y soy nivel {self.nivel}."

    def morir(self):
        self.esta_vivo = False
        print(f"{self.nombre} ha caído en batalla.")

# --- USO ---
if __name__ == "__main__":
    # Instanciación: Crear objetos a partir de la clase
    hero = Personaje("Aragorn", 10)
    villano = Personaje("Orco", 3)

    print(hero.saludar())   # Salida: Hola, soy Aragorn...
    print(villano.saludar()) # Salida: Hola, soy Orco...
    
    # Accediendo a atributos
    print(f"¿El héroe vive?: {hero.esta_vivo}")