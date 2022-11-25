from errores import *

def separacion_nombre_edad(participante):
    if len(participante) > 0:
        participante_ordenado = participante.split(",")
        if len(participante_ordenado[0]) <= 5:
            pass
        else:
            participante_ordenado[0] = "xxxxx"
            # raise NombreMayorCincoLetras
        return participante_ordenado
    else:
        return ["X", "X"]
