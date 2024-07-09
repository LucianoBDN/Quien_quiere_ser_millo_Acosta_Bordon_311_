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
from jugador import Jugador
from comodin import Comodin
from score import *
from class_pregunta import Pregunta

def cerrar_ventana(lista_eventos: list, diccionario_switches: dict):

    for evento in lista_eventos:
        
        if evento.type == pygame.QUIT:
            
            diccionario_switches['bucle_principal'] = False

    return diccionario_switches


def manejar_eventos_menu_principal(diccionario_switches: dict, cronometro: object, jugador: object, lista_eventos: list, lista_botones: list, lista_comodines: list, pregunta: object, lista_preguntas: list):
    
    for evento in lista_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and diccionario_switches['menu_principal'] == True:

            for boton in lista_botones:
                
                if boton.rect.collidepoint(pygame.mouse.get_pos()):
                    
                    match boton.nombre:
                        
                        case "boton_jugar":
                            print("click")
                            diccionario_switches['menu_principal'] = False
                            diccionario_switches['jugando'] = True
                            cronometro.iniciar()
                            pregunta.establecer_pregunta(jugador.nivel, lista_preguntas)
                            print(pregunta.pregunta)
                            for comodin in lista_comodines:
                                
                                comodin.reiniciar_comodines()

                        case "boton_salir":
                            print("click")
                            diccionario_switches['bucle_principal'] = False

    return diccionario_switches


def manejar_eventos_respuesta(diccionario_switches: dict, jugador: object, cronometro: object, lista_eventos: list, lista_botones: list, pregunta: list[dict]):
    
    for evento in lista_eventos:
    
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and diccionario_switches['menu_principal'] == False and diccionario_switches['jugando'] == True and diccionario_switches['pausa'] == False:

                if jugador.vidas > 0 and cronometro.actualizar() > 0: # A chequear si funciona con while o si hay que reemplazar con "if"

                    for boton in lista_botones:

                        if boton.rect.collidepoint(pygame.mouse.get_pos()) and boton.switch_default == True:          
                        
                            match boton.nombre:
                                
                                case "boton_a":                                
                                    diccionario_switches['resultado_respuesta'] = manejar_niveles(boton, pregunta['respuesta_correcta'])
                                
                                case "boton_b":
                                    diccionario_switches['resultado_respuesta'] = manejar_niveles(boton, pregunta['respuesta_correcta'])
                                
                                case "boton_c":
                                    diccionario_switches['resultado_respuesta'] = manejar_niveles(boton, pregunta['respuesta_correcta'])

                                case "boton_d":
                                    diccionario_switches['resultado_respuesta'] = manejar_niveles(boton, pregunta['respuesta_correcta'])

    return diccionario_switches

def manejar_eventos_comodines(diccionario_switches: dict, lista_eventos: list, lista_comodines: list, lista_botones: list):

    for evento in lista_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and diccionario_switches['menu_principal'] == False and diccionario_switches['jugando'] == True and diccionario_switches['pausa'] == False:

            for boton in lista_botones:

                if boton.rect.collidepoint(pygame.mouse.get_pos()):

                    match boton.nombre:

                        case "boton_publico":

                            for comodin in lista_comodines:

                                if comodin.nombre == "comodin_publico" and comodin.usos > 0:

                                    comodin.activo = True
                                    comodin.lista_alturas = generar_lista_alturas() # A editar cuando se convierta en metodo
                                    break

                        case "boton_llamada":

                            for comodin in lista_comodines:

                                if comodin.nombre == "comodin_llamada" and comodin.usos > 0:

                                    comodin.activo = True
                                    break

                        case "boton_cincuenta":

                            for comodin in lista_comodines:

                                if comodin.nombre == "comodin_cincuenta" and comodin.usos > 0:

                                    comodin.activo = True
                                    break


def manejar_eventos_pausa(diccionario_switches: dict, jugador: object, cronometro: object, lista_comodines: list, lista_eventos: list, lista_botones: list, pregunta: object, lista_preguntas: list):

    for evento in lista_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and diccionario_switches['resultado_respuesta'] == True and diccionario_switches['pausa'] == True and diccionario_switches['jugando'] == False:
                      
                for boton in lista_botones:

                    if boton.rect.collidepoint(pygame.mouse.get_pos()):

                        match boton.nombre:
                        
                            case "boton_continuar":

                                if jugador.nivel < 15: #Probar con esta ubicación, sino subirlo
                            
                                    for boton in lista_botones:

                                        boton.reiniciar_switches()
                                                                        
                                    for comodin in lista_comodines:
                                        
                                        comodin.reiniciar()

                                    pregunta.establecer_pregunta(pregunta, jugador.nivel, lista_preguntas)
                                    diccionario_switches['resultado_respuesta'] = None
                                    diccionario_switches['jugando'] = True
                                    diccionario_switches['pausa'] = False                             
                                    jugador.aumentar_nivel_y_monto()
                                    cronometro.iniciar()

                            case "boton_retirarse":
                                pass
                                # if (jugador.score == 1000 or jugador.score == 32000):

                                #     flag_retirarse = not flag_retirarse
                                #     jugador.nombre = jugador.manejar_evento_jugador(evento,jugador.nombre)

                                #     if evento.key == pygame.K_RETURN:
                                        
                                #         highscore = [jugador.nombre, jugador.score]
                                #         lista_score.append(highscore)

    return diccionario_switches


def manejar_eventos_derrota(diccionario_switches: dict, jugador: object, cronometro: object, lista_eventos: list, lista_botones: list, lista_comodines: list):

    for evento in lista_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and diccionario_switches['resultado_respuesta'] == False and diccionario_switches['pausa'] == True and diccionario_switches['jugando'] == False or (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and cronometro.actualizar() == 0):

            for boton in lista_botones:

                if boton.rect.collidepoint(pygame.mouse.get_pos()):

                    match boton.nombre:

                        case "boton_volver":
                
                            for comodin in lista_comodines:

                                comodin.reiniciar()

                            for boton in lista_botones:

                                boton.reiniciar_switches()
                            
                            diccionario_switches['menu_principal'] = True
                            diccionario_switches['pausa'] = False
                            diccionario_switches['resultado_respuesta'] = None
                            jugador.nivel = 1
                            jugador.score = 100

    return diccionario_switches