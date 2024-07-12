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


def manejar_eventos_respuesta(diccionario_switches: dict, jugador: object, cronometro: object, lista_eventos: list, lista_botones: list, pregunta: object, sonido_respuesta_mal):
    
    for evento in lista_eventos:
    
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and diccionario_switches['menu_principal'] == False and diccionario_switches['jugando'] == True and diccionario_switches['pausa'] == False:

                if jugador.vidas > 0 and cronometro.actualizar() > 0: # A chequear si funciona con while o si hay que reemplazar con "if"

                    for boton in lista_botones:

                        if boton.rect.collidepoint(pygame.mouse.get_pos()) and boton.switch_default == True:          
                        
                            match boton.nombre:
                                
                                case "boton_a":                                
                                    if boton.texto !="":
                                        manejar_niveles(boton, pregunta, diccionario_switches, sonido_respuesta_mal)
                                        cronometro.reiniciar()

                                case "boton_b":
                                    if boton.texto !="":
                                        manejar_niveles(boton, pregunta, diccionario_switches, sonido_respuesta_mal)
                                        cronometro.reiniciar()

                                case "boton_c":
                                    if boton.texto !="":
                                        manejar_niveles(boton, pregunta, diccionario_switches, sonido_respuesta_mal)
                                        cronometro.reiniciar()


                                case "boton_d":
                                    if boton.texto !="":
                                        manejar_niveles(boton, pregunta, diccionario_switches, sonido_respuesta_mal)
                                        cronometro.reiniciar()


                elif cronometro.actualizar() == 0:

                    diccionario_switches['jugando'] = False
                    diccionario_switches['resultado_respuesta'] = False

    return diccionario_switches

def manejar_eventos_comodines(diccionario_switches: dict, lista_eventos: list, lista_comodines: list, lista_botones: list):

    for evento in lista_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and diccionario_switches['menu_principal'] == False and diccionario_switches['jugando'] == True:

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

                                    pregunta.establecer_pregunta(jugador.nivel, lista_preguntas)
                                    diccionario_switches['resultado_respuesta'] = None
                                    diccionario_switches['jugando'] = True
                                    diccionario_switches['pausa'] = False                             
                                    jugador.aumentar_nivel_y_monto()
                                    cronometro.iniciar()

                            case "boton_retirarse":
                                
                                    diccionario_switches['retirarse'] = True
                                    diccionario_switches['jugando'] = False
                                    
                            


    return diccionario_switches


def manejar_eventos_derrota(diccionario_switches: dict, jugador: object, cronometro, lista_eventos: list, lista_botones: list, lista_comodines: list):

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


def manejar_eventos_score(diccionario_switches, lista_botones, lista_eventos):

    for evento in lista_eventos:

        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and diccionario_switches['pantalla_score'] == True:

            for boton in lista_botones:

                if boton.rect.collidepoint(pygame.mouse.get_pos()):

                    match boton.nombre:

                        case "boton_volver":

                            diccionario_switches['pantalla_score'] = False
                            diccionario_switches['menu_principal'] = True
                            


    
    return diccionario_switches