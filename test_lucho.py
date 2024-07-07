import pygame
from jugador import Jugador
from botones import *
from score import *
from eventos import *
from pantalla import *

pygame.init()

ventana = setear_ventana("¿Quién quiere ser millonario?", r"logos\utnavellaneda.jpg", 1280, 720)

fuente_arial_quince = pygame.font.SysFont("Arial",18)
fuente_arial_veinte = pygame.font.SysFont("Arial",20, bold=True)
fuente_arial_treinta = pygame.font.SysFont("Arial",30)


clock = pygame.time.Clock()

lista_preguntas = cargar_archivo_json(r"datos\preguntas_y_respuestas.json")

menu_principal = True
jugando = False
pausa = False
flag = True
comodin_publico = False
cincuenta_cincuenta = False
comodin_llamada = False
resultado_respuesta = None
pantalla_score = False
bandera_retirarse = False
player = Jugador()


#lista_botones = [   Boton(ventana, 5,370,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte),
                #     Boton(ventana, 505,370,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte),
                #     Boton(ventana, 5,530,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte),
                #     Boton(ventana, 505,530,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte),
                #     Boton(ventana, 870,270,150,50, (28,99,162), (18,79,134), (18,79,134), "Continuar", fuente_arial_quince),
                #     Boton(ventana, 870,330,150,50, (28,99,162), (18,79,134), (18,79,134), "Retirarse", fuente_arial_quince),
                #     Boton(ventana, 870,330,200,50, (28,99,162), (18,79,134), (18,79,134), "Volver al menú principal", fuente_arial_quince),
                #     Boton(ventana,1000,100,50,50,(0,0,0),(0,0,0),(0,0,0),"",fuente_arial_veinte),
                #     Boton(ventana,1100,100,50,50,(0,0,0),(0,0,0),(0,0,0),"",fuente_arial_veinte),
                #     Boton(ventana,1200,100,50,50,(0,0,0),(0,0,0),(0,0,0),"",fuente_arial_veinte)
                # ]

 

lista_alturas = []
#lista_score = cargar_matriz_csv()

while flag:

    lista_eventos = pygame.event.get()
    
    flag = cerrar_ventana(lista_eventos, flag)
    
        
       

    if menu_principal == True:
          mostrar_menu_principal(ventana, r"graficos\stage.png",(1280, 720), r"graficos\guido_static.png", (1050, 400), 550,700, "Quien quiere ser millonario?", pygame.font.Font(r"fuentes\Audiowide.ttf", 40),(255,255,255), 310, 100)
    
    mostrar_pantalla_juego(ventana, r"graficos\fondo_azul_oscuro.jpg", (1280, 720), r"graficos\guido_pregunta.png", (340,105), 400, 200, True, r"graficos\boton_banco.png", (280,350), (110,70), player.score, pygame.font.Font(r"fuentes\Audiowide.ttf", 25), (255,223,0), r"graficos\boton_respuesta.png",(840, 300), (500,300), pygame.font.SysFont("Arial",20, bold=True), "Pio es Gay??", (255,255,255))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
