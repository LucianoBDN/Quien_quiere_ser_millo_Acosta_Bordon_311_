import pygame
from escenas import *
from boton import *
from datos import *


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
fuente = pygame.font.SysFont("Arial",30)

fondo_superficie = pygame.image.load(r"graficos\stage.png")
fondo_superficie_escalado = pygame.transform.scale(fondo_superficie,(DIMENSION_VENTANA))

guido_static_superficie = pygame.image.load(r"graficos\guido_static.png").convert_alpha()
guido_static_superficie = pygame.transform.flip(guido_static_superficie, True, False)
guido_static_rectangulo = guido_static_superficie.get_rect(center = (1000,400))



boton_jugar = pygame.Rect(560,300,150,50)
boton_salir = pygame.Rect(560,400,150,50)


preguntas = cargar_archivo_json(r"datos\preguntas_y_respuestas.json")


menu_principal = True
flag = True
while flag == True:

    lista_eventos = pygame.event.get()
    if menu_principal == True:
        ventana.blit(fondo_superficie_escalado,(0,0))
        ventana.blit(guido_static_superficie, guido_static_rectangulo)
        pintar_boton(ventana, boton_jugar, AZUL_CLARO, AZUL_OSCURO, "Jugar", BLANCO, fuente)
        pintar_boton(ventana, boton_salir, AZUL_CLARO, AZUL_OSCURO, "Salir", BLANCO, fuente)

    for evento in lista_eventos:

        if evento.type == pygame.QUIT:
            flag = False

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_jugar.collidepoint(pygame.mouse.get_pos()):
                print("Click")
                ventana = cambiar_escena_jugar(ventana,DIMENSION_VENTANA, r"graficos\preguntas_escena.jpg")
                ventana = cambiar_status_presentador(ventana, (400,200), r"graficos\guido_pregunta.png", (1000, 400))
                menu_principal = False

            elif boton_salir.collidepoint(pygame.mouse.get_pos()):
                flag = False
    
        print(evento)
    

    posicion_mouse = pygame.mouse.get_pos()
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()