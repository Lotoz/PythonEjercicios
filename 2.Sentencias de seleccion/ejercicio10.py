#Funciones de control de resultado
# 1 = no puede
# 0 = poder
def isAyunas(ayuna):
    ayuna if 1 else 0

def isEdad(edad):
    edad >= 18 and edad <= 65 if  0 else 1


def frecuenciaCardicac(pulsaciones):
    pulsaciones >= 50 and pulsaciones <= 110 if 1 else 0

#Tension 
# 1 = BAJA
# 0 = ALTA
# 2 = NORMAL
def tensionArterial(tension):
    if tension >= 50 and tension <= 100: 
        return 1 
    elif tension >= 90 and tension <= 180:
        return 0
    else:
        return 2
    
##Te has quedao aqui.
# Termina mujer y si da bien para que done
# queda hacer interfaz
# Probar luego 
def valoresHemoglobina(hemoglobina, genero):
    if genero == 'M':
        if hemoglobina > 13.5:
            return 1
    elif genero == 'F':
        if hemoglobina > 12.5:
            return 1
        

def conteoDePlaquetas(plaq):
    if plaq >= 150000:
        return 1
    else:
        return 0

def proteinasTotales(proteinas):
    if proteinas >= 6.0:
        return 1
    else:
        return 0

def puedeDonar(ayuna, edad, pulsaciones, tension, hemoglobina, genero, plaq, proteinas):
    if isAyunas(ayuna) == 1:
        return "No puede donar por no estar en ayunas"
    elif isEdad(edad) == 1:
        return "No puede donar por no tener la edad adecuada"
    elif frecuenciaCardicac(pulsaciones) == 1:
        return "No puede donar por no tener la frecuencia cardiaca adecuada"
    elif tensionArterial(tension) == 0:
        return "No puede donar por tener la tension arterial alta"
    elif valoresHemoglobina(hemoglobina, genero) != 1:
        return "No puede donar por no tener los valores de hemoglobina adecuados"
    elif conteoDePlaquetas(plaq) == 0:
        return "No puede donar por no tener el conteo de plaquetas adecuado"
    elif proteinasTotales(proteinas) == 0:
        return "No puede donar por no tener las proteinas totales adecuadas"
    else:
        return "Puede donar sangre"
    
#Prueba
ayuna = input("Realizo ayuna? (1 = si, 0 = no): ")
edad = int(input("Cual es su edad?: "))
pulsaciones = int(input("Cual es su frecuencia cardiaca?: "))
tension = int(input("Cual es su tension arterial?: "))
hemoglobina = float(input("Cual es su nivel de hemoglobina?: "))
genero = input("Cual es su genero? (M = masculino, F = femenino): ")
plaq = int(input("Cual es su conteo de plaquetas?: "))
proteinas = float(input("Cual es su nivel de proteinas totales?: "))    

print(puedeDonar(ayuna, edad, pulsaciones, tension, hemoglobina, genero, plaq, proteinas))