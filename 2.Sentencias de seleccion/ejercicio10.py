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
def tensionArterial(tension)
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
        

