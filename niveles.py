import random
from texto import *
import pygame

def seleccionar_pregunta(nivel_jugador: int, preguntas: list[dict]):

    nivel_pregunta_random = 0
    
    while nivel_pregunta_random != nivel_jugador:
    
        id_pregunta_random = random.randint(1, 15)

        for pregunta in preguntas:

            if id_pregunta_random == pregunta['id']:

                nivel_pregunta_random = pregunta['nivel']

                pregunta_final = pregunta

    return pregunta_final


def manejar_niveles(boton, respuesta):
                      
        if boton.texto == respuesta:                    
            boton.switch_default = False
            boton.switch_verde = True
            respuesta_correcta = True  
                
        else:                               
            boton.switch_default = False
            boton.switch_rojo = True
            respuesta_correcta = False

        return respuesta_correcta