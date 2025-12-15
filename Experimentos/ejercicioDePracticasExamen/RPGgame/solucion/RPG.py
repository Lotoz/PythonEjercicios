import random
from abc import ABC, abstractmethod
import time

# ==========================================
# 1. COMPOSICIÓN ("TIENE UN")
# ==========================================
class Dado:
    """
    Esta clase será usada dentro de los personajes.
    Los personajes NO heredan del dado, sino que TIENEN un dado.
    """
    def __init__(self, caras):
        self.caras = caras

    def tirar(self):
        return random.randint(1, self.caras)


# ==========================================
# 2. INTERFAZ / CLASE ABSTRACTA
# ==========================================
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


# ==========================================
# 3. ENCAPSULACIÓN Y CLASE PADRE
# ==========================================
class Personaje(ICombatiente):
    def __init__(self, nombre, vida_maxima, caras_dado):
        self.nombre = nombre
        self._vida_maxima = vida_maxima  # Atributo protegido (convención)
        self.__vida = vida_maxima        # Atributo PRIVADO (doble guion bajo)
        
        # COMPOSICIÓN: Creamos el objeto Dado DENTRO del personaje
        self.arma = Dado(caras_dado)

    # --- GETTER Y SETTER PARA ENCAPSULACIÓN ---
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


# ==========================================
# 4. HERENCIA
# ==========================================

# --- Héroes ---
class Guerrero(Personaje):
    def __init__(self, nombre):
        # El guerrero tiene mucha vida (100) y un dado de 8 caras
        super().__init__(nombre, vida_maxima=100, caras_dado=8)

    # 5. POLIMORFISMO (Implementación propia de atacar)
    def atacar(self, objetivo):
        dano = self.arma.tirar() + 2  # Bono fijo de fuerza
        print(f"{self.nombre} (Guerrero) ataca con su espada! Daño: {dano}")
        objetivo.recibir_dano(dano)

class Mago(Personaje):
    def __init__(self, nombre):
        # El mago tiene poca vida (60) pero un dado de 20 caras (hechizos potentes)
        super().__init__(nombre, vida_maxima=60, caras_dado=20)

    # 5. POLIMORFISMO (Implementación propia de atacar)
    def atacar(self, objetivo):
        dano = self.arma.tirar()
        print(f"{self.nombre} (Mago) lanza una bola de fuego! Daño: {dano}")
        objetivo.recibir_dano(dano)


# --- Villanos ---
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
        dano = self.arma.tirar()
        if dano > 10:
            print("¡GOLPE CRÍTICO! El dragón escupe fuego intenso.")
            dano += 5
        print(f"{self.nombre} ataca con garras! Daño: {dano}")
        objetivo.recibir_dano(dano)


# ==========================================
# MAIN: EL BUCLE DE JUEGO
# ==========================================
def jugar_partida():
    print("=== BIENVENIDO AL COLIEUM PYTHON ===")
    print("Selecciona tu héroe:")
    print("1. Guerrero (Vida alta, daño estable)")
    print("2. Mago (Vida baja, daño explosivo)")
    
    opcion = input("Elige (1 o 2): ")
    nombre_usuario = input("Nombra a tu héroe: ")

    # Instanciación del Héroe
    if opcion == '1':
        jugador = Guerrero(nombre_usuario)
    else:
        jugador = Mago(nombre_usuario)

    # Selección aleatoria del Villano (Polimorfismo en acción: no importa cuál salga)
    villanos_posibles = [Orco(), Dragon()]
    enemigo = random.choice(villanos_posibles)

    print(f"\n¡Un {enemigo.nombre} salvaje ha aparecido!")
    print(f"Comienza el combate: {jugador.nombre} VS {enemigo.nombre}")
    print("-" * 40)
    time.sleep(1)

    turno = 1
    while jugador.esta_vivo and enemigo.esta_vivo:
        print(f"\n--- TURNO {turno} ---")
        
        # Turno del Jugador
        input("Presiona ENTER para atacar...")
        jugador.atacar(enemigo)
        
        if not enemigo.esta_vivo:
            print(f"\n¡VICTORIA! {enemigo.nombre} ha sido derrotado.")
            break

        time.sleep(1)

        # Turno del Villano
        print(f"\nTurno de {enemigo.nombre}...")
        enemigo.atacar(jugador)

        if not jugador.esta_vivo:
            print("\nHas muerto... GAME OVER.")
            break
        
        turno += 1
        print("-" * 40)

if __name__ == "__main__":
    jugar_partida()