# 05_polimorfismo.py

class Arquero:
    def atacar(self):
        return "Dispara flecha"

class Caballero:
    def atacar(self):
        return "Golpea con escudo"

class Dragon:
    def atacar(self):
        return "Escupe fuego"

# Función polimórfica: No le importa qué clase sea, solo que tenga el método .atacar()
def turno_de_combate(participante):
    print(f"Acción: {participante.atacar()}")

# --- USO ---
if __name__ == "__main__":
    mis_unidades = [Arquero(), Caballero(), Dragon()]

    print("--- INICIO DEL TURNO ---")
    for unidad in mis_unidades:
        # Aquí ocurre la magia: llamamos al mismo método, 
        # pero cada objeto responde de forma distinta.
        turno_de_combate(unidad)