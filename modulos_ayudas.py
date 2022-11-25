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

def grupos_clasificados(file, tipo_grupo):
    numero_persona = 0
    for grupo in tipo_grupo:
        numero_persona += 1
        texto = f"persona {numero_persona}: {grupo.persona_1.nombre} - {grupo.persona_1.edad}"
        file.write(f"{texto}\n")
    return

def grupos_a_ordenados(file, grupo, numero_grupo):
    texto_p1 = f"persona 1: {grupo.persona_1.nombre} - {grupo.persona_1.edad}"
    file.write(f"\nGRUPO {numero_grupo}\n\n")
    file.write(f"{texto_p1}\n")
    return

def grupos_b_ordenados(file, grupo, numero_grupo):
    texto_p1 = f"persona 1: {grupo.persona_1.nombre} - {grupo.persona_1.edad}"
    texto_p2 = f"persona 2: {grupo.persona_2.nombre} - {grupo.persona_2.edad}"
    file.write(f"\nGRUPO {numero_grupo}\n\n")
    file.write(f"{texto_p1}\n")
    file.write(f"{texto_p2}\n")
    return

def grupos_c_ordenados(file, grupo, numero_grupo):
    texto_p1 = f"persona 1: {grupo.persona_1.nombre} - {grupo.persona_1.edad}"
    texto_p2 = f"persona 2: {grupo.persona_2.nombre} - {grupo.persona_2.edad}"
    texto_p3 = f"persona 3: {grupo.persona_3.nombre} - {grupo.persona_3.edad}"
    file.write(f"\nGRUPO {numero_grupo}\n\n")
    file.write(f"{texto_p1}\n")
    file.write(f"{texto_p2}\n")
    file.write(f"{texto_p3}\n")
    return
