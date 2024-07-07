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


def manejar_eventos_respuesta(flag_menu_principal: bool, flag_jugando: bool, flag_pausa: bool, jugador: object, cronometro: object, lista_eventos: list, lista_botones: list, pregunta: list[dict]):
    
    for evento in lista_eventos:
    
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and flag_menu_principal == False and flag_jugando == True and flag_pausa == False:

                while jugador.vidas > 0 and cronometro.actualizar() > 0: # A chequear si funciona con while o si hay que reemplazar con "if"

                    for boton in lista_botones:

                        if boton.rect.collidepoint(pygame.mouse.get_pos()) and boton.switch_default == True:          
                        
                            match boton.nombre:
                                
                                case "boton_a":                                
                                    resultado_respuesta = manejar_niveles(boton, pregunta['respuesta_correcta'])
                                
                                case "boton_b":
                                    resultado_respuesta = manejar_niveles(boton, pregunta['respuesta_correcta'])
                                
                                case "boton_c":
                                    resultado_respuesta = manejar_niveles(boton, pregunta['respuesta_correcta'])

                                case "boton_d":
                                    resultado_respuesta = manejar_niveles(boton, pregunta['respuesta_correcta'])

    return resultado_respuesta

def manejar_eventos_comodines(flag_menu_principal: bool, flag_jugando: bool, flag_pausa: bool, lista_eventos: list, lista_comodines: list):
    
    for evento in lista_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and flag_menu_principal == False and flag_jugando == True and flag_pausa == False:

            for comodin in lista_comodines:

                if comodin.rect.collidepoint(pygame.mouse.get_pos()) and comodin.usos > 0:

                    match comodin.nombre:

                        case "comodin_publico":
                            comodin.activo = True
                            comodin.lista_alturas = generar_lista_alturas() # A editar cuando se convierta en metodo

                        case "comodin_llamada":
                            comodin.activo = True

                        case "comodin_cincuenta_cincuenta":
                            comodin.activo = True


def manejar_eventos_pausa(resultado_respuesta, flag_jugando: bool, flag_pausa: bool, flag_retirarse: bool, jugador: object, cronometro: object, lista_comodines: list, lista_eventos: list, lista_botones: list, lista_preguntas: list):

    for evento in lista_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and resultado_respuesta == True and flag_pausa == True and flag_jugando == False:
                      
                for boton in lista_botones:

                    if boton.rect.collidepoint(pygame.mouse.get_pos()):

                        match boton.nombre:
                        
                            case "boton_continuar":

                                if jugador.nivel < 15: #Probar con esta ubicación, sino subirlo
                            
                                    for boton in lista_botones:

                                        boton.reiniciar_switches()
                                                                        
                                    for comodin in lista_comodines:
                                        
                                        comodin.reiniciar()

                                    resultado_respuesta = None
                                    flag_jugando = True
                                    flag_pausa = False                             
                                    jugador.aumentar_nivel_y_monto()
                                    cronometro.iniciar()
                                    pregunta = seleccionar_pregunta(jugador.nivel, lista_preguntas)

                            case "boton_retirarse":
                                pass
                                # if (jugador.score == 1000 or jugador.score == 32000):

                                #     flag_retirarse = not flag_retirarse
                                #     jugador.nombre = jugador.manejar_evento_jugador(evento,jugador.nombre)

                                #     if evento.key == pygame.K_RETURN:
                                        
                                #         highscore = [jugador.nombre, jugador.score]
                                #         lista_score.append(highscore)


def manejar_eventos_derrota(flag_menu_principal: bool, flag_jugando: bool, flag_pausa, resultado_respuesta, jugador: object, cronometro: object, lista_eventos: list, lista_botones: list, lista_comodines: list, lista_preguntas: list):

    for evento in lista_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and resultado_respuesta == False and flag_pausa == True and flag_jugando == False or (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and cronometro.actualizar() == 0):

            for boton in lista_botones:

                if boton.rect.collidepoint(pygame.mouse.get_pos()):

                    match boton.nombre:

                        case "boton_volver":
                
                            for comodin in lista_comodines:

                                comodin.reiniciar()

                            for boton in lista_botones:

                                boton.reiniciar_switches()
                            
                            flag_menu_principal = not flag_menu_principal
                            flag_pausa = False
                            resultado_respuesta = None
                            jugador.nivel = 1
                            jugador.score = 100