import pygame
from generales import *
from score import *
from texto import *
class Jugador:
    def __init__(self):
        """Inicia la clase con los valores por defecto de un jugador
                self.nombre = ""
                self.score = 100
                self.vidas = 1
                self.nivel = 
        """
        self.nombre = ""
        self.score = 100
        self.vidas = 1
        self.nivel = 1
    

    def manejar_evento_jugador(self, lista_eventos: list ,texto:str, switches: dict, lista_score: list[list], path_csv_score: str):
        """Recibe como parametro una variable texto la cual al finalizar la funcion
        pasara a ser el nombre del jugador para asi poder tener un registro
        el primer si una tecla es presionada entra y realiza las acciones
        borrar si la key presionada es K_BACKSPACE,
        actualiza el nombre del jugador si la tecla presionada es (ENTER),
        else if si el texto

        Args:
            evento (event): acciones dentro del juego
            texto (str): string vacio a rellenar

        Returns:
            _type_: _description_
        """


        
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if switches['escribir']:
                    if evento.key == pygame.K_BACKSPACE:
                        texto = texto[:-1]   
                    elif evento.key == pygame.K_RETURN:
                        self.nombre = texto

                        agregar_jugador_highscore(self.nombre, self.score, lista_score, path_csv_score)
                        reiniciar_switches(switches)
                        # switches['escribir'] = False
                        # switches['menu_principal'] = True
                    else:
                        if len(texto) < 8:
                            texto += evento.unicode
               
        
        return texto
    

    def aumentar_nivel_y_monto(self):
        """Si el jugador responde bien la pregunta se llamara a esta funcion para actualizar nivel y monto
        utilizando un match que compare los distintos niveles y asigne el monto por el cual esta jugando
        """

        self.nivel += 1

        match (self.nivel):
            
            case 1:
                self.score = 100
            case 2:
                self.score = 200
            case 3:
                self.score = 300
            case 4:
                self.score = 500
            case 5:
                self.score = 1000
            case 6:
                self.score = 2000
            case 7:
                self.score = 4000
            case 8:
                self.score = 8000
            case 9:
                self.score = 16000
            case 10:
                self.score = 32000
            case 11:
                self.score = 64000
            case 12:
                self.score = 125000
            case 13:
                self.score = 250000
            case 14:
                self.score = 500000
            case 15:
                self.score = 1000000




    



    