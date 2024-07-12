import pygame
from jugador import Jugador
from botones import *
from score import *
from eventos import *
from pantalla import *
from class_pregunta import Pregunta
from generales import *

pygame.init()

ventana = setear_ventana("¿Quién quiere ser millonario?", r"logos\utnavellaneda.jpg", 1280, 720)
clock = pygame.time.Clock()
lista_preguntas = cargar_archivo_json(r"datos\preguntas_y_respuestas.json")
player = Jugador()
switches = {
                'bucle_principal' : True,
                'menu_principal' : True,
                'jugando' : False,
                'pausa' : False,
                'comodin_publico' : False,
                'cincuenta_cincuenta' : False,
                'comodin_llamada' : False,
                'resultado_respuesta' : None,
                'pantalla_score' : False,
                'retirarse' : False,
                'escribir' : True
            }
lista_botones = [   Boton(ventana, "boton_jugar", 560,300,150,50, (28,99,162), (18,79,134), (18,79,134), "Jugar", pygame.font.SysFont("Arial",30)),
                    Boton(ventana, "boton_score", 560,400,150,50, (28,99,162), (18,79,134), (18,79,134), "Highscore", pygame.font.SysFont("Arial",30)),
                    Boton(ventana, "boton_salir", 560,500,150,50, (28,99,162), (18,79,134), (18,79,134), "Salir", pygame.font.SysFont("Arial",30)),
                    Boton(ventana, "boton_a", 5,370,550,200,(18,79,134), (18,79,134), (18,79,134),"",pygame.font.SysFont("Arial",20, bold=True)),
                    Boton(ventana, "boton_b", 505,370,550,200,(18,79,134), (18,79,134), (18,79,134),"",pygame.font.SysFont("Arial",20, bold=True)),
                    Boton(ventana, "boton_c", 5,530,550,200,(18,79,134), (18,79,134), (18,79,134),"",pygame.font.SysFont("Arial",20, bold=True)),
                    Boton(ventana, "boton_d", 505,530,550,200,(18,79,134), (18,79,134), (18,79,134),"",pygame.font.SysFont("Arial",20, bold=True)),
                    Boton(ventana, "boton_continuar", 870,270,150,50, (28,99,162), (18,79,134), (18,79,134), "Continuar", pygame.font.SysFont("Arial",18)),
                    Boton(ventana, "boton_retirarse", 870,330,150,50, (28,99,162), (18,79,134), (18,79,134), "Retirarse", pygame.font.SysFont("Arial",18)),
                    Boton(ventana, "boton_volver", 870,500,200,50, (28,99,162), (18,79,134), (18,79,134), "Volver al menú principal", pygame.font.SysFont("Arial",18)),
                    Boton(ventana, "boton_publico", 1000,100,50,50,(0,0,0),(0,0,0),(0,0,0),"",pygame.font.SysFont("Arial",20, bold=True)),
                    Boton(ventana, "boton_llamada", 1100,100,50,50,(0,0,0),(0,0,0),(0,0,0),"",pygame.font.SysFont("Arial",20, bold=True)),
                    Boton(ventana, "boton_cincuenta", 1200,100,50,50,(0,0,0),(0,0,0),(0,0,0),"",pygame.font.SysFont("Arial",20, bold=True))
                ]
lista_comodines = [ 
                    Comodin("comodin_publico"),
                    Comodin("comodin_llamada"),
                    Comodin("comodin_cincuenta")
                    ]
cronometro = Cronometro(5)
lista_score = cargar_matriz_csv(r"datos\score.csv")
print(lista_score)
pregunta = Pregunta()

while switches["bucle_principal"]:

    lista_eventos = pygame.event.get()

    manejar_eventos_menu_principal(switches, cronometro, player, lista_eventos, lista_botones, lista_comodines, pregunta, lista_preguntas) 

    manejar_eventos_respuesta(switches, player, cronometro, lista_eventos, lista_botones, pregunta)

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

   