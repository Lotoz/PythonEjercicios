# 02_encapsulacion.py

class PersonajeProtegido:
    def __init__(self, nombre, vida_maxima):
        self.nombre = nombre
        
        # Atributo PRIVADO: Se indica con doble guion bajo (__).
        # Python "oculta" esta variable para que no se toque desde fuera fácilmente.
        self.__vida = vida_maxima  
        self.__vida_maxima = vida_maxima

    # GETTER: Usamos el decorador @property para leer el valor como si fuera un atributo
    @property
    def vida(self):
        return self.__vida

    # SETTER: Permite modificar el valor con reglas de validación
    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self.__vida = 0
            print("La vida no puede ser negativa. Se ha ajustado a 0.")
        elif valor > self.__vida_maxima:
            self.__vida = self.__vida_maxima
        else:
            self.__vida = valor

# --- USO ---
if __name__ == "__main__":
    p = PersonajeProtegido("Leonidas", 100)

    # p.vida = -50  # Esto activará la lógica del SETTER y pondrá 0, no -50
    # print(p.__vida) # Esto daría ERROR, porque es privado.
    
    print(f"Vida actual: {p.vida}") # Usamos el GETTER
    
    p.vida = -200 # Intentamos romper el código
    print(f"Vida tras ataque masivo: {p.vida}") # Salida: 0