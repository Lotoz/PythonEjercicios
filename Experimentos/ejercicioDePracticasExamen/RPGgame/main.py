import random
import time
from Villanos import Orco, Dragon
from Heroes import Guerrero, Mago


def jugar_partida():
    print("=== BIENVENIDO AL COLISEO ===")
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

    # Selección aleatoria del Villano 
    villanos_posibles = [Orco(), Dragon()]
    enemigo = random.choice(villanos_posibles) #Elige entre un array de opciones

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

        time.sleep(1) # Relentiza la salida de terminal

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
