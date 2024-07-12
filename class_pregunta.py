import pygame
import random

class Pregunta:
    def __init__(self):
        """Inicializa la clase pregunta con sus atributos
        """
        self.id = None
        self.monto_premio = None
        self.pregunta = None
        self.respuesta_a = None
        self.respuesta_b = None
        self.respuesta_c = None
        self.respuesta_d = None
        self.respuesta_correcta = None
        self.nivel = None
        self.pista = None


    def establecer_pregunta(self, nivel_jugador: int, lista_preguntas: list[dict]) -> dict:
        """Establece una nueva pregunta según los atributos del jugador

        Args:
            nivel_jugador (int): nivel en el que se encuentra el jugador
            lista_preguntas (list[dict]): _description_

        Returns:
            dict: _description_
        """

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
        self.respuesta_a = pregunta_final['posibles_respuestas'][0]
        self.respuesta_b = pregunta_final['posibles_respuestas'][1]
        self.respuesta_c = pregunta_final['posibles_respuestas'][2]
        self.respuesta_d = pregunta_final['posibles_respuestas'][3]
        self.respuesta_correcta = pregunta_final['respuesta_correcta']
        self.nivel = pregunta_final['nivel']
        self.pista = pregunta_final['pista']

    def reiniciar_pregunta(self):
        
        self.id = None
        self.monto_premio = None
        self.pregunta = None
        self.posibles_respuestas = None
        self.respuesta_correcta = None
        self.nivel = None
        self.pista = None