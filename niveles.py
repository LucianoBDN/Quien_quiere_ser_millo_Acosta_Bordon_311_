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



def cronometro( duracion_tiempo: int):

        tiempo = pygame.time.get_ticks() / 1000

        tiempo_restante =  duracion_tiempo - tiempo 


        print(tiempo_restante)

        tiempo_restante = int(tiempo_restante)
        
        if tiempo_restante < 0:
            tiempo_restante = None
        
        return tiempo_restante
        
    

        




