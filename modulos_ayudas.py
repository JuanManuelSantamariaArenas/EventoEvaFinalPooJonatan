def separacion_nombre_edad(participante):
    if len(participante) > 0:
        participante_ordenado = participante.split(",")
        return participante_ordenado
    else:
        return ["X", "X"]