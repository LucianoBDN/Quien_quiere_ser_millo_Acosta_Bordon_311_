import random
from texto import *
import pygame

def seleccionar_pregunta(nivel_jugador: int, preguntas: list[dict]):

    nivel_pregunta_random = 0
    
    while nivel_pregunta_random != nivel_jugador:
    
        id_pregunta_random = random.randint(1, 375)

        for pregunta in preguntas:

            if id_pregunta_random == pregunta['id']:

                nivel_pregunta_random = pregunta['nivel']

                pregunta_final = pregunta

    return pregunta_final


def manejar_niveles(boton, respuesta, vidas_jugador, nivel_jugador: int, preguntas: list[dict]):
                      
        if boton.texto == respuesta:                    
            boton.switch_default = False
            boton.switch_verde = True
            nivel_jugador += 1
            print("COOORRECTOOOOOOO")
            respuesta_correcta = True
                
        else:                               
            boton.switch_default = False
            boton.switch_rojo = True
            vidas_jugador = 0
            print("BURROOOOOOOO")
            respuesta_correcta = False

        return respuesta_correcta