import pygame
from boton import *

ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
DIMENSION_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)

pygame.init()

ventana = pygame.display.set_mode((DIMENSION_VENTANA))
pygame.display.set_caption("¿Quién quiere ser millonario?")
icono = pygame.image.load(r"logos\utnavellaneda.jpg")
pygame.display.set_icon(icono)
clock = pygame.time.Clock()
fuente = pygame.font.SysFont("Arial",30)

fondo_superficie = pygame.image.load(r"graficos\stage.png")
fondo_superficie_escalado = pygame.transform.scale(fondo_superficie,(DIMENSION_VENTANA))

guido_pregunta_superficie_sin_escalar = pygame.image.load(r"graficos\guido_pregunta.png").convert_alpha()
guido_pregunta_superficie = pygame.transform.scale(guido_pregunta_superficie_sin_escalar,(400,200))
guido_pregunta_rectangulo = guido_pregunta_superficie.get_rect(center = (1000,400))

boton_jugar = pygame.Rect(560,300,150,50)
boton_salir = pygame.Rect(560,400,150,50)

flag = True
while flag == True:

    lista_eventos = pygame.event.get()
    
    for evento in lista_eventos:

        if evento.type == pygame.QUIT:
            flag = False

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
            if boton_jugar.collidepoint(pygame.mouse.get_pos()):
                print("Click")
            elif boton_salir.collidepoint(pygame.mouse.get_pos()):
                flag = False
    
    ventana.blit(fondo_superficie_escalado,(0,0))
    
    ventana.blit(guido_pregunta_superficie, guido_pregunta_rectangulo)
    
    pintar_boton(ventana, boton_jugar, "Jugar", fuente)
    pintar_boton(ventana, boton_salir, "Salir", fuente)

    posicion_mouse = pygame.mouse.get_pos()
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()