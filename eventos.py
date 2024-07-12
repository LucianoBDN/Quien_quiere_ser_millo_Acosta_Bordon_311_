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
    """Cierra el juego cuando se toca la "X"

    Args:
        lista_eventos (list): lista de eventos
        diccionario_switches (dict): diccionario de interruptores

    Returns:
        diccionario_switches (dict): diccionario de interruptores actualizado
    """

    for evento in lista_eventos:
        
        if evento.type == pygame.QUIT:
            
            diccionario_switches['bucle_principal'] = False

    return diccionario_switches


def manejar_eventos_menu_principal(diccionario_switches: dict, cronometro: object, jugador: object, lista_eventos: list, lista_botones: list, lista_comodines: list, pregunta: object, lista_preguntas: list):
    """Se encarga de todos los eventos que sucedan en la pantalla de menú principal

    Args:
        diccionario_switches (dict): diccionario de interruptores
        cronometro (object): el cronometro de las preguntas
        jugador (object): la clase jugador
        lista_eventos (list): lista de eventos
        lista_botones (list): lista de botones
        lista_comodines (list): lista de comodines
        pregunta (object): la clase pregunta
        lista_preguntas (list): lista de preguntas

    Returns:
        diccionario_switches (dict): el diccionario de interruptores acutalizado
    """
    
    for evento in lista_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and diccionario_switches['menu_principal'] == True:

            for boton in lista_botones:
                
                if boton.rect.collidepoint(pygame.mouse.get_pos()):
                    
                    match boton.nombre:
                        
                        case "boton_jugar":
                            
                            diccionario_switches['menu_principal'] = False
                            diccionario_switches['jugando'] = True
                            cronometro.iniciar()
                            pregunta.establecer_pregunta(jugador.nivel, lista_preguntas)
                            print(pregunta.pregunta)
                            for comodin in lista_comodines:
                                
                                comodin.reiniciar_comodines()

                            for boton in lista_botones:
                                boton.reiniciar_switches()


                        case "boton_score":
                            diccionario_switches['menu_principal'] = False
                            diccionario_switches['pantalla_score'] = True




                        case "boton_salir":
                            
                            diccionario_switches['bucle_principal'] = False

    return diccionario_switches


def manejar_eventos_respuesta(diccionario_switches: dict, jugador: object, cronometro: object, lista_eventos: list, lista_botones: list, pregunta: object, sonido_respuesta_mal, sonido_respuesta_bien):
    """Se encarga de los eventos cuando el jugador selecciona una respuesta

    Args:
        diccionario_switches (dict): diccionario de interruptores
        jugador (object): clase jugador
        cronometro (object): el cronometro para responder
        lista_eventos (list): lista de todos los eventos
        lista_botones (list): lista de botones
        pregunta (object): clase de la pregunta
        sonido_respuesta_mal (_type_): sonido cuando responde mal
        sonido_respuesta_bien (_type_): sonido cuando responde bien

    Returns:
        diccionario_switches (dict): diccionario de interruptores
    """
    
    for evento in lista_eventos:
    
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and diccionario_switches['menu_principal'] == False and diccionario_switches['jugando'] == True and diccionario_switches['pausa'] == False and jugador.nivel < 16:

                if jugador.vidas > 0 and cronometro.actualizar() > 0: # A chequear si funciona con while o si hay que reemplazar con "if"

                    for boton in lista_botones:

                        if boton.rect.collidepoint(pygame.mouse.get_pos()) and boton.switch_default == True:          
                        
                            match boton.nombre:
                                
                                case "boton_a":                                
                                    if boton.texto !="":
                                        manejar_niveles(boton, pregunta, diccionario_switches, sonido_respuesta_mal, sonido_respuesta_bien)
                                        cronometro.reiniciar()

                                case "boton_b":
                                    if boton.texto !="":
                                        manejar_niveles(boton, pregunta, diccionario_switches, sonido_respuesta_mal, sonido_respuesta_bien)
                                        cronometro.reiniciar()

                                case "boton_c":
                                    if boton.texto !="":
                                        manejar_niveles(boton, pregunta, diccionario_switches, sonido_respuesta_mal, sonido_respuesta_bien)
                                        cronometro.reiniciar()


                                case "boton_d":
                                    if boton.texto !="":
                                        manejar_niveles(boton, pregunta, diccionario_switches, sonido_respuesta_mal, sonido_respuesta_bien)
                                        cronometro.reiniciar()


                elif cronometro.actualizar() == 0:

                    diccionario_switches['jugando'] = False
                    diccionario_switches['resultado_respuesta'] = False

    return diccionario_switches

def manejar_eventos_comodines(diccionario_switches: dict, lista_eventos: list, lista_comodines: list, lista_botones: list):
    """Se encarga de los eventos cuando se usa un comodin

    Args:
        diccionario_switches (dict): diccionario de interruptores
        lista_eventos (list): lista de eventos
        lista_comodines (list): lista de comodines
        lista_botones (list): lista de botones
    """
    for evento in lista_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and diccionario_switches['menu_principal'] == False and diccionario_switches['jugando'] == True and diccionario_switches['pausa'] == False:

            for boton in lista_botones:

                if boton.rect.collidepoint(pygame.mouse.get_pos()):

                    match boton.nombre:

                        case "boton_publico":

                            for comodin in lista_comodines:

                                if comodin.nombre == "comodin_publico" and comodin.usos > 0:
                                    
                                    print("click")
                                    comodin.activo = True
                                    comodin.generar_lista_alturas()
                                    break

                        case "boton_llamada":

                            for comodin in lista_comodines:

                                if comodin.nombre == "comodin_llamada" and comodin.usos > 0:
                                   

                                    comodin.activo = True
                                    break

                        case "boton_cincuenta":

                            for comodin in lista_comodines:

                                if comodin.nombre == "comodin_cincuenta" and comodin.usos > 0:
                                    comodin.generar_auxiliar_cincuenta()
                                    comodin.activo = True
                                    break


def manejar_eventos_pausa(diccionario_switches: dict, jugador: object, cronometro: object, lista_comodines: list, lista_eventos: list, lista_botones: list, pregunta: object, lista_preguntas: list):
    """Maneja los eventos cuando hay una pausa antes de pasar a la próxima pregunta

    Args:
        diccionario_switches (dict): diccionario de interruptores
        jugador (object): clase del jugador
        cronometro (object): cronometro
        lista_comodines (list): lista de comodines
        lista_eventos (list): lista de eventos
        lista_botones (list): lista de botones
        pregunta (object): clase de la pregunta
        lista_preguntas (list): lista de preguntas

    Returns:
        diccionario_switches (dict): diccionario de interruptores
    """

    for evento in lista_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and diccionario_switches['resultado_respuesta'] != False and diccionario_switches['pausa'] == True:
                      
                for boton in lista_botones:

                    if boton.rect.collidepoint(pygame.mouse.get_pos()):

                        match boton.nombre:
                        
                            case "boton_continuar":


                                if jugador.nivel < 15: #Probar con esta ubicación, sino subirlo
                                    


                                    for boton in lista_botones:

                                        boton.reiniciar_switches()
                                                                        
                                    for comodin in lista_comodines:
                                        
                                        comodin.desactivar_comodin()

                                    jugador.aumentar_nivel_y_monto()
                                    pregunta.establecer_pregunta(jugador.nivel, lista_preguntas)
                                    diccionario_switches['resultado_respuesta'] = None
                                    diccionario_switches['jugando'] = True
                                    diccionario_switches['pausa'] = False                             
                                    cronometro.iniciar()

                            case "boton_retirarse":
                                
                                    diccionario_switches['retirarse'] = True
                                    diccionario_switches['jugando'] = False
                                                    

    return diccionario_switches


def manejar_eventos_derrota(diccionario_switches: dict, jugador: object, cronometro, lista_eventos: list, lista_botones: list, lista_comodines: list):
    """Maneja los eventos en la pantalla cuando perdes

    Args:
        diccionario_switches (dict): diccionario de interruptores
        jugador (object): clase jugador
        cronometro (_type_): cronometro
        lista_eventos (list): lista de eventos
        lista_botones (list): lista de botones
        lista_comodines (list): lista de comodines

    Returns:
        diccionario_switches (dict): diccionario de interruptores
    """

    for evento in lista_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and diccionario_switches['resultado_respuesta'] == False  and diccionario_switches['jugando'] == False:

            for boton in lista_botones:

                if boton.rect.collidepoint(pygame.mouse.get_pos()):

                    match boton.nombre:

                        case "boton_volver":
                                                
                            for comodin in lista_comodines:

                                comodin.reiniciar_comodines()

                            for boton in lista_botones:

                                boton.reiniciar_switches()
                            
                            cronometro.reiniciar()
                            diccionario_switches['menu_principal'] = True
                            diccionario_switches['pausa'] = False
                            diccionario_switches['resultado_respuesta'] = None
                            jugador.nivel = 1
                            jugador.score = 100

    return diccionario_switches


def manejar_eventos_score(diccionario_switches: dict, lista_botones: list, lista_eventos: list, jugador: object):
    """Maneja los eventos que suceden en la pantalla de highscore

    Args:
        diccionario_switches (_type_): diccionario de interruptores
        lista_botones (_type_): lista de botones
        lista_eventos (_type_): lista de eventos

    Returns:
        diccionario_switches (_type_): diccionario de interruptores
    """

    for evento in lista_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and diccionario_switches['pantalla_score'] == True:

            for boton in lista_botones:

                if boton.rect.collidepoint(pygame.mouse.get_pos()):

                    match boton.nombre:

                        case "boton_volver":

                            diccionario_switches['pantalla_score'] = False
                            diccionario_switches['menu_principal'] = True
                            jugador.nivel = 1
                            jugador.score = 100
                            
                            
    
    return diccionario_switches