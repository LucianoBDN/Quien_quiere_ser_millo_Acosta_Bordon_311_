import pygame
from jugador import Jugador
from botones import *
from score import *
from eventos import *
from pantalla import *
from class_pregunta import Pregunta
from generales import *
from  funciones_lambda import *

pygame.init()

ventana = setear_ventana("¿Quién quiere ser millonario?", r"logos\utnavellaneda.jpg", 1280, 720)
clock = pygame.time.Clock()
player = Jugador()

lista_preguntas = cargar_archivo_json(r"datos\preguntas_y_respuestas.json")

switches = cargar_switches()

lista_botones = cargar_botones(ventana)

lista_comodines = cargar_comodines()



sonido = cargar_sonidos(r"sonidos\musica_fondo.mp3", r"sonidos\sonido_acierto.mp3", r"sonidos\respuesta_mal.mp3")



cronometro = Cronometro(30)
lista_score = cargar_matriz_csv(r"datos\score.csv")


pregunta = Pregunta()

while switches["bucle_principal"]:

    lista_eventos = pygame.event.get()

    manejar_eventos_menu_principal(switches, cronometro, player, lista_eventos, lista_botones, lista_comodines, pregunta, lista_preguntas) 

    manejar_eventos_respuesta(switches, player, cronometro, lista_eventos, lista_botones, pregunta, sonido[0], sonido[1])

    manejar_eventos_comodines(switches, lista_eventos, lista_comodines, lista_botones)

    pantalla_score(ventana, lista_score, switches, lista_botones, lista_eventos)

    manejar_eventos_score(switches, lista_botones, lista_eventos)

    pantalla_menu_principal(ventana,switches, lista_botones, lista_eventos)

    pantalla_juego(ventana, switches, player.score, pregunta.pregunta, lista_botones, lista_comodines, pregunta, player, lista_eventos, cronometro)

    manejar_eventos_pausa(switches, player, cronometro, lista_comodines, lista_eventos, lista_botones, pregunta, lista_preguntas)

    pantalla_perdiste(ventana, lista_botones, lista_eventos, switches, cronometro)

    manejar_eventos_derrota(switches, player, cronometro, lista_eventos, lista_botones, lista_comodines)

    pantalla_retirarse(ventana, lista_score, player, switches, lista_eventos)

    cerrar_ventana(lista_eventos, switches)

    pygame.display.update()

    clock.tick(60)


pygame.quit()

   