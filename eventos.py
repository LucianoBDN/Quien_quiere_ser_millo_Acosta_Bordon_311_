import pygame
from ventana import *
from escenas import *
from datos import *
from texto import *
from niveles import *
from generales import *
from cronometro import Cronometro
from botones import Boton
from presentador import Presentador
from fondo import Fondo
from banco import Banco
from jugador import Jugador
from comodin import Comodin
from score import *

def cerrar_ventana(lista_eventos: list, flag_bucle_principal: bool):

    for evento in lista_eventos:
        
        if evento.type == pygame.QUIT:
            
            flag_bucle_principal = False

    return flag_bucle_principal


def manejar_eventos_menu_principal(flag_menu_principal: bool, flag_jugando: bool, jugador: object, cronometro: object, lista_eventos: list, lista_botones: list, lista_comodines: list, lista_preguntas: list):

    for evento in lista_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and flag_menu_principal == True:

            for boton in lista_botones:

                if boton.rect.collidepoint(pygame.mouse.get_pos()):
                    
                    match boton:
                        
                        case "boton_jugar":
                            menu_principal = not menu_principal
                            flag_jugando = not flag_jugando
                            pregunta = seleccionar_pregunta(jugador.nivel, lista_preguntas)
                            cronometro.iniciar()
                            
                            for comodin in lista_comodines:
                                
                                comodin.reiniciar_comodines()

                        case "boton_salir":
                            
                            flag_menu_principal = False

    return pregunta


def manejar_eventos_pantalla_juego():
    pass