from errores import *
import operator

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

def leer_invitados_clasificados(tipo_grupo, info):
    nombre_invitado = info[2]
    edad_invitado = list(info[4])
    edad_invitado = str(edad_invitado[0] + edad_invitado[1])
    info_invitado = [tipo_grupo, nombre_invitado, edad_invitado]
    return info_invitado

def crear_dic_alfabeto(alfabeto):
    alfabeto_diccionario = {}
    for letra in alfabeto:
        alfabeto_diccionario[letra] = 0
    return alfabeto_diccionario


def top_tres_letras_mas_frecuentes_p1(alfabeto, nombre_invitado):
    nombre_invitado = nombre_invitado[0]
    nombre_invitado = list(nombre_invitado)
    for letra_alfabeto in alfabeto:
        for letra_nombre in nombre_invitado:
            if letra_alfabeto == letra_nombre:
                alfabeto[letra_alfabeto] += 1
    return alfabeto

def top_tres_letras_mas_frecuentes_p2(alfabeto):
    alfabeto_ordenado = alfabeto
    alfabeto_ordenado = sorted(alfabeto_ordenado.items(), key=operator.itemgetter(1), reverse=True)
    print("TOP 3 LETRAS MÁS FRECUENTES EN LOS NOMBRES DE LOS INVITADOS")
    for i in range(0, 3):
        letra_alfabeto = alfabeto_ordenado[i][0]
        frecuencia_letra = alfabeto_ordenado[i][1]
        print("Posición {}: {} = {}".format(i + 1, letra_alfabeto, frecuencia_letra))
    return
