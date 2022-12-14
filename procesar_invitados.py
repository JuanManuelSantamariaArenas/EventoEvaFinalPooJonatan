from dataclasses import dataclass
from abc import ABC, abstractmethod
import pickle
import string
import modulos_ayudas


class Persona:

    def __init__(self, nombre: str, edad: str):
        self.nombre = nombre
        self.edad = edad


class Grupo(ABC):

    @abstractmethod
    def presentar(self):
        pass

class GrupoA(Grupo):

    def __init__(self, persona_1: Persona):
        self.persona_1 = persona_1

    def presentar(self):
        print(f"Grupo A = Nombre: {self.persona_1.nombre}, Edad: {self.persona_1.edad}")

"""     def __str__(self) -> str:
        return f"Nombre: {self.persona_1.nombre}, Edad: {self.persona_1.edad}" """

class GrupoB(Grupo):

    def __init__(self, persona_1: Persona, persona_2: Persona):
        self.persona_1 = persona_1
        self.persona_2 = persona_2
    
    def presentar(self):
        print(f"Grupo B = Persona uno: {self.persona_1.nombre} y Persona dos: {self.persona_2.nombre}")

"""     def __str__(self) -> str:
        return f"Persona uno: {self.persona_1.nombre} y Persona dos: {self.persona_2.nombre}" """

class GrupoC(Grupo):

    def __init__(self, persona_1: Persona, persona_2: Persona, persona_3: Persona):
        self.persona_1 = persona_1
        self.persona_2 = persona_2
        self.persona_3 = persona_3
    
    def presentar(self):
        print(f"Grupo C = Persona uno: {self.persona_1.nombre}, Persona dos: {self.persona_2.nombre} y Persona tres: {self.persona_3.nombre}")

"""     def __str__(self) -> str:
        return f"Persona uno: {self.persona_1.nombre}, Persona dos: {self.persona_2.nombre} y  Persona tres: {self.persona_3.nombre}" """

class Evento():

    def __init__(self):
        self.grupos_invitados = []
        self.cantidad_por_grupo = {}
        self.cantidad_total_grupos = 0

    def crear_invitados(self) -> list[Grupo]:
        grupos: list[Grupo] = [] 
        with open("invitados.txt", encoding="utf8") as file:
            acompañantes = []
            for linea in file:
                info = linea.split(" ")
                info.pop()
                if len(info) >= 1:
                    invitado = modulos_ayudas.separacion_nombre_edad(info[0])
                    nombre_invitado = invitado[0]
                    edad_invitado = invitado[1]
                    invitado = Persona(nombre_invitado, edad_invitado)
                    if len(info) >= 2:
                        acompañante_uno = modulos_ayudas.separacion_nombre_edad(info[1])
                        nombre_acompañante_uno = acompañante_uno[0]
                        edad_acompañante_uno = acompañante_uno[1]
                        acompañante_uno = Persona(nombre_acompañante_uno, edad_acompañante_uno)
                        acompañantes.append(acompañante_uno) 
                        if len(info) >= 3:
                            acompañante_dos = modulos_ayudas.separacion_nombre_edad(info[2])
                            nombre_acompañante_dos = acompañante_dos[0]
                            edad_acompañante_dos = acompañante_dos[1]
                            acompañante_dos = Persona(nombre_acompañante_dos, edad_acompañante_dos)
                            acompañantes.append(acompañante_dos)
                if len(acompañantes) == 0:
                    grupo = GrupoA(invitado)
                    grupos.append(grupo)
                elif len(acompañantes) == 1:
                    grupo = GrupoB(invitado, acompañantes[0])
                    grupos.append(grupo)
                elif len(acompañantes) == 2:
                    grupo = GrupoC(invitado, acompañantes[0], acompañantes[1])
                    grupos.append(grupo)            
                acompañantes.clear()
                # print(grupos)
        self.grupos_invitados = grupos
        return self.grupos_invitados
    
    def mostrar_grupos(self):
        for grupo in self.grupos_invitados:
            # print(grupo)
            grupo.presentar()
        return

    def serializar_grupos(self):
        with open("grupos.txt", "wb") as file:
            pickle.dump(self, file)
            print("\nSE SERIALIZARÓN LOS GRUPO CON ÉXITO\n")
        return
    
    def deserializar_grupos(self):
        with open("grupos.txt", "rb") as file:
            grupos_anteriores = pickle.load(file)
            self.grupos_invitados = grupos_anteriores.grupos_invitados
            print("\nSE DESEARIALIZARÓN LOS GRUPOS CON ÉXITO\n")
            cantidad_grupo_a = 0
            cantidad_grupo_b = 0
            cantidad_grupo_c = 0
            for grupo in self.grupos_invitados:
                if issubclass(type(grupo), GrupoA):
                    cantidad_grupo_a += 1
                elif issubclass(type(grupo), GrupoB):
                    cantidad_grupo_b += 1
                elif issubclass(type(grupo), GrupoC):
                    cantidad_grupo_c += 1
            self.cantidad_por_grupo = {"GrupoA": cantidad_grupo_a, "GrupoB": cantidad_grupo_b, "GrupoC": cantidad_grupo_c} # dict[Grupo:Cantidad]
            self.cantidad_total_grupos = cantidad_grupo_a + cantidad_grupo_b + cantidad_grupo_c
            print("\nGrupoA: {} grupos, GrupoB: {} grupos, GrupoC: {} grupos, Total grupos: {}\n".format(self.cantidad_por_grupo["GrupoA"], self.cantidad_por_grupo["GrupoB"],self.cantidad_por_grupo["GrupoC"], self.cantidad_total_grupos))
            return self.cantidad_total_grupos, self.cantidad_por_grupo

    def escribir_archivo_grupos_por_tipo(self):   # Por cada tipo de grupo las personas que hay
        with open("gruposclasificados.txt", "w+") as file:
            grupo_a = []
            grupo_b = []
            grupo_c = []
            for grupo in self.grupos_invitados:
                if issubclass(type(grupo), GrupoA):
                    grupo_a.append(grupo)
                elif issubclass(type(grupo), GrupoB):
                    grupo_b.append(grupo)
                elif issubclass(type(grupo), GrupoC):
                    grupo_c.append(grupo)
            grupos_clasificados = [grupo_a, grupo_b, grupo_c]
            file.write("GRUPO A\n\n")
            modulos_ayudas.grupos_clasificados(file, grupo_a)
            file.write("\nGRUPO B\n\n")
            modulos_ayudas.grupos_clasificados(file, grupo_b)
            file.write("\nGRUPO C\n\n")
            modulos_ayudas.grupos_clasificados(file, grupo_c)
        return

    def escribir_archivo_grupos_general(self):
        with open("gruposordenados.txt", "w+") as file:
            numero_grupo = 0
            for grupo in self.grupos_invitados:
                numero_grupo += 1
                if issubclass(type(grupo), GrupoA):
                    modulos_ayudas.grupos_a_ordenados(file, grupo, numero_grupo)
                elif issubclass(type(grupo), GrupoB):
                    modulos_ayudas.grupos_b_ordenados(file, grupo, numero_grupo)
                elif issubclass(type(grupo), GrupoC):
                    modulos_ayudas.grupos_c_ordenados(file, grupo, numero_grupo)
        return

    def leer_grupos_clasificados(self):
        with open("gruposclasificados.txt", encoding="utf8") as file:
            grupo_A = []
            grupo_B = []
            grupo_C = []
            grupos = []
            for linea in file:
                info = linea.split(" ")
                if len(info) == 2:
                    tipo_grupo = list(info[1])
                    tipo_grupo = tipo_grupo[0]
                if len(info) > 2:
                    info_invitado = modulos_ayudas.leer_invitados_clasificados(tipo_grupo, info)
                    invitado = Persona(info_invitado[1], info_invitado[2])
                    if info_invitado[0] == "A":
                        grupo_A.append(invitado)
                    elif info_invitado[0] == "B":
                        grupo_B.append(invitado)
                    elif info_invitado[0] == "C":
                        grupo_C.append(invitado)
            grupos = [grupo_A, grupo_B, grupo_C]
        return    

    def top_tres_letras_mas_frecuentes(self):
        with open("invitados.txt", encoding="utf8") as file:
            alfabeto = list(string.ascii_lowercase)
            alfabeto = modulos_ayudas.crear_dic_alfabeto(alfabeto)
            for linea in file:
                info = linea.split(" ")
                info.pop()
                for invitado in info:
                    nombre_invitado = invitado.split(",")
                    nombre_invitado.pop()
                    cantidad_por_letras = modulos_ayudas.top_tres_letras_mas_frecuentes_p1(alfabeto, nombre_invitado)
                    alfabeto = cantidad_por_letras
            modulos_ayudas.top_tres_letras_mas_frecuentes_p2(alfabeto)
        return

def iniciar_evento():
    evento_uno = Evento()
    evento_uno.top_tres_letras_mas_frecuentes()
    evento_uno.crear_invitados()
    evento_uno.mostrar_grupos()
    evento_uno.serializar_grupos()
    evento_uno.deserializar_grupos()
    evento_uno.escribir_archivo_grupos_por_tipo()
    evento_uno.escribir_archivo_grupos_general()
    evento_uno.leer_grupos_clasificados()
iniciar_evento()
