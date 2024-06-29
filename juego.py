import pygame
from escenas import *
from boton import *
from datos import *
from texto import *
from niveles import *
from comodines import *

ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
DIMENSION_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)

BLANCO = (255,255,255)
AZUL_CLARO = (28,99,162)
AZUL_OSCURO = (18,79,134)


pygame.init()

ventana = pygame.display.set_mode((DIMENSION_VENTANA))
pygame.display.set_caption("¿Quién quiere ser millonario?")
icono = pygame.image.load(r"logos\utnavellaneda.jpg")
pygame.display.set_icon(icono)
clock = pygame.time.Clock()
fuente_arial_quince = pygame.font.SysFont("Arial",18)
fuente_arial_veinte = pygame.font.SysFont("Arial",20, bold=True)
fuente_arial_treinta = pygame.font.SysFont("Arial",30)
fuente_titulo = pygame.font.Font(r"fuentes\Audiowide.ttf", 40)

fondo_superficie = pygame.image.load(r"graficos\stage.png")
fondo_superficie_escalado = pygame.transform.scale(fondo_superficie,(DIMENSION_VENTANA))

guido_static_superficie = pygame.image.load(r"graficos\guido_static.png").convert_alpha()
guido_static_superficie = pygame.transform.flip(guido_static_superficie, True, False)
guido_static_rectangulo = guido_static_superficie.get_rect(center = (1050,400))

boton_jugar = pygame.Rect(560,300,150,50)
boton_salir = pygame.Rect(560,400,150,50)

boton_superficie = pygame.image.load(r"graficos\boton_respuesta.png").convert_alpha()
boton_superficie_a = pygame.transform.scale(boton_superficie,(550,200))
boton_superficie_b = pygame.transform.scale(boton_superficie,(550,200))
boton_superficie_c = pygame.transform.scale(boton_superficie,(550,200))
boton_superficie_d = pygame.transform.scale(boton_superficie,(550,200))
boton_rectangulo_a = boton_superficie_a.get_rect(topleft = (5,370))
boton_rectangulo_b = boton_superficie_b.get_rect(topleft = (505,370))
boton_rectangulo_c = boton_superficie_c.get_rect(topleft = (5,530))
boton_rectangulo_d = boton_superficie_d.get_rect(topleft = (505,530))
preguntas_superficie = pygame.image.load(r"graficos\boton_respuesta.png").convert_alpha()
preguntas_superficie = pygame.transform.scale(boton_superficie,(850,300))
preguntas_rectangulo = preguntas_superficie.get_rect(topleft = (100,150))
banco_superficie = pygame.image.load(r"graficos\boton_banco.png").convert_alpha()
banco_rectangulo = banco_superficie.get_rect(center = (620,100))

lista_preguntas = cargar_archivo_json(r"datos\preguntas_y_respuestas.json")

###COMODINES###
rect_x = 100
rect_y = 500  # Altura mayor que el ancho
rect_width = 50
rect_height = 40  # Altura mayor que el ancho

menu_principal = True
flag = True
while flag == True:

    lista_eventos = pygame.event.get()
    if menu_principal == True:
        ventana.blit(fondo_superficie_escalado,(0,0))
        ventana.blit(guido_static_superficie, guido_static_rectangulo)
        pintar_boton(ventana, boton_jugar, AZUL_CLARO, AZUL_OSCURO, "Jugar", BLANCO, fuente_arial_treinta)
        pintar_boton(ventana, boton_salir, AZUL_CLARO, AZUL_OSCURO, "Salir", BLANCO, fuente_arial_treinta)
        escribir_texto(ventana, "Quien quiere ser millonario?", fuente_titulo, BLANCO, 310, 100)
    
    for evento in lista_eventos:

        if evento.type == pygame.QUIT:
            flag = False

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_jugar.collidepoint(pygame.mouse.get_pos()):
                ventana = cambiar_escena_jugar(ventana,DIMENSION_VENTANA, r"graficos\fondo_azul_oscuro.jpg")
                ventana = cambiar_status_presentador(ventana, (400,200), r"graficos\guido_pregunta.png", (130, 5))
                pregunta = seleccionar_pregunta(15, lista_preguntas)
                ventana.blit(preguntas_superficie, preguntas_rectangulo)
                escribir_texto(ventana, pregunta['pregunta'], fuente_arial_treinta, BLANCO, 195,265)
                ventana.blit(boton_superficie_a, boton_rectangulo_a)
                ventana.blit(boton_superficie_b, boton_rectangulo_b)
                ventana.blit(boton_superficie_c, boton_rectangulo_c)
                ventana.blit(boton_superficie_d, boton_rectangulo_d)
                ventana.blit(banco_superficie, banco_rectangulo)
                mostrar_respuestas(ventana, fuente_arial_veinte, pregunta['posibles_respuestas'], 65, 415)
                #mostrar_barras(ventana, BLANCO, rect_x, rect_y, rect_width)
                menu_principal = False
                
            elif boton_salir.collidepoint(pygame.mouse.get_pos()):
                flag = False
    
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()