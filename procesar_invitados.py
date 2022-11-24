from dataclasses import dataclass
from abc import ABC, abstractmethod
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
        print(f"Nombre: {self.persona_1.nombre}, Edad: {self.persona_1.edad}")

    def __str__(self) -> str:
        return super().__str__()

class GrupoB(Grupo):

    def __init__(self, persona_1: Persona, persona_2: Persona):
        self.persona_1 = persona_1
        self.persona_2 = persona_2
    
    def presentar(self):
        print(f"Persona uno: {self.persona_1.nombre} y Persona dos: {self.persona_2.nombre}")

class GrupoC(Grupo):

    def __init__(self, persona_1: Persona, persona_2: Persona, persona_3: Persona):
        self.persona_1 = persona_1
        self.persona_2 = persona_2
        self.persona_3 = persona_3
    
    def presentar(self):
        print(f"Persona uno: {self.persona_1.nombre}, Persona dos: {self.persona_2.nombre} y  Persona tres: {self.persona_3.nombre}")

def crear_invitados():
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
                grupos.append(Grupo)
            elif len(acompañantes) == 1:
                grupo = GrupoB(invitado, acompañantes[0])
                grupos.append(grupo)
            elif len(acompañantes) == 2:
                grupo = GrupoC(invitado, acompañantes[0], acompañantes[1])
                grupos.append(grupo)            
            acompañantes.clear()
            # print(grupos)
    return grupos

def mostrar_grupos(grupos):
    print(grupos)
    for grupo in grupos:
        print(grupo)
        # grupo.presentar()
    return

grupos_evento = crear_invitados()
mostrar_grupos(grupos_evento)