# 04_interfaces.py
from abc import ABC, abstractmethod

# Esta clase no se puede instanciar, es solo un "contrato" o plantilla abstracta
class Enemigo(ABC):
    
    @abstractmethod
    def gritar(self):
        pass  # No hace nada aquí, pero OBLIGA a los hijos a tener este método

    @abstractmethod
    def dar_experiencia(self):
        pass

class Goblin(Enemigo):
    # Si borro este método, Python dará error al intentar crear un Goblin
    def gritar(self):
        return "¡Waaaaarg!"

    def dar_experiencia(self):
        return 50

# --- USO ---
if __name__ == "__main__":
    # e = Enemigo() # ESTO DARÍA ERROR. No se pueden crear abstractos.
    
    g = Goblin() # Esto funciona porque cumple el contrato (tiene gritar y dar_exp)
    print(f"El goblin hace: {g.gritar()}")