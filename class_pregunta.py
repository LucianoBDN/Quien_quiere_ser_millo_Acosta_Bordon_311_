import pygame
import random

class Pregunta:
    def __init__(self):
        self.id = None
        self.monto_premio = None
        self.pregunta = None
        self.posibles_respuestas = None
        self.respuesta_correcta = None
        self.nivel = None
        self.pista = None


    def establecer_pregunta(self, nivel_jugador: int, lista_preguntas: list[dict]) -> dict:

        nivel_pregunta_random = 0
        
        while nivel_pregunta_random != nivel_jugador:
        
            id_pregunta_random = random.randint(1, 75)

            for pregunta in lista_preguntas:

                if id_pregunta_random == pregunta['id']:

                    nivel_pregunta_random = pregunta['nivel']

                    pregunta_final = pregunta

        self.id = pregunta_final['id']
        self.monto_premio = pregunta_final['monto_premio']
        self.pregunta = pregunta_final['pregunta']
        self.posibles_respuestas = pregunta_final['posibles_respuestas']
        self.respuesta_correcta = pregunta_final['respuesta_correcta']
        self.nivel = pregunta_final['nivel']
        self.pista = pregunta_final['pista']