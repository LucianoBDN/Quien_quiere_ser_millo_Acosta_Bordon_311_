import pygame
from escenas import *
from boton import *
from datos import *
from texto import *
from niveles import *
from comodines import *
from test import *
from cronometro import Cronometro
from botones import Boton
ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
DIMENSION_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)

BLANCO = (255,255,255)
AZUL_CLARO = (28,99,162)
AZUL_OSCURO = (18,79,134)
NEGRO = (0,0,0)


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
boton_a_superficie = pygame.transform.scale(boton_superficie,(550,200))
boton_b_superficie = pygame.transform.scale(boton_superficie,(550,200))
boton_c_superficie = pygame.transform.scale(boton_superficie,(550,200))
boton_d_superficie = pygame.transform.scale(boton_superficie,(550,200))
boton_a_rectangulo = boton_a_superficie.get_rect(topleft = (5,370))
boton_b_rectangulo = boton_b_superficie.get_rect(topleft = (505,370))
boton_c_rectangulo = boton_c_superficie.get_rect(topleft = (5,530))
boton_d_rectangulo = boton_d_superficie.get_rect(topleft = (505,530))
preguntas_superficie = pygame.image.load(r"graficos\boton_respuesta.png").convert_alpha()
preguntas_superficie = pygame.transform.scale(boton_superficie,(850,300))
preguntas_rectangulo = preguntas_superficie.get_rect(topleft = (100,150))
banco_superficie = pygame.image.load(r"graficos\boton_banco.png").convert_alpha()
banco_superficie = pygame.transform.scale(banco_superficie,(250,350))
banco_rectangulo = banco_superficie.get_rect(center = (100,70))
boton_rojo_superficie = pygame.image.load(r"graficos\boton_rojo.png").convert_alpha()
boton_rojo_superficie = pygame.transform.scale(boton_rojo_superficie,(550,200))
boton_a_rojo_rectangulo = boton_rojo_superficie.get_rect(topleft = (5,370))
boton_b_rojo_rectangulo = boton_rojo_superficie.get_rect(topleft = (505,370))
boton_c_rojo_rectangulo = boton_rojo_superficie.get_rect(topleft = (5,530))
boton_d_rojo_rectangulo = boton_rojo_superficie.get_rect(topleft = (505,530))
boton_verde_superficie = pygame.image.load(r"graficos\boton_verde.png").convert_alpha()
boton_verde_superficie = pygame.transform.scale(boton_verde_superficie,(550,200))
boton_a_verde_rectangulo = boton_verde_superficie.get_rect(topleft = (5,370))
boton_b_verde_rectangulo = boton_verde_superficie.get_rect(topleft = (505,370))
boton_c_verde_rectangulo = boton_verde_superficie.get_rect(topleft = (5,530))
boton_d_verde_rectangulo = boton_verde_superficie.get_rect(topleft = (505,530))

lista_preguntas = cargar_archivo_json(r"datos\preguntas_y_respuestas.json")

###COMODINES###
rect_x = 100
rect_y = 500  # Altura mayor que el ancho
rect_width = 50
rect_height = 40  # Altura mayor que el ancho

switch_boton_a = True
switch_boton_b = True
switch_boton_c = True
switch_boton_d = True
menu_principal = True
flag = True

 
cronometro = Cronometro(11)

while flag:

    lista_eventos = pygame.event.get()
    
    
    for evento in lista_eventos:
        
        if menu_principal:
            ventana.blit(fondo_superficie_escalado,(0,0))
            ventana.blit(guido_static_superficie, guido_static_rectangulo)
            escribir_texto(ventana, "Quien quiere ser millonario?", fuente_titulo, BLANCO, 310, 100)

        boton_jugar = Boton(560,300,150,50, AZUL_CLARO, AZUL_OSCURO, AZUL_OSCURO, "Jugar", fuente_arial_treinta)
        Boton.manejar_evento(boton_jugar, evento)
        Boton.dibujar(boton_jugar, ventana,BLANCO)
        boton_salir = Boton(560,400,150,50, AZUL_CLARO, AZUL_OSCURO, AZUL_OSCURO, "Salir", fuente_arial_treinta)
       
        Boton.manejar_evento(boton_salir, evento)
        Boton.dibujar(boton_salir, ventana, BLANCO)

        if evento.type == pygame.QUIT:
            flag = False

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and menu_principal != False:

            if boton_jugar.rect.collidepoint(pygame.mouse.get_pos()):
                
                menu_principal = not menu_principal
                pregunta = seleccionar_pregunta(13, lista_preguntas)
                cronometro.iniciar()
                switch_boton_a = True
                switch_boton_b = True
                switch_boton_c = True
                switch_boton_d = True
                switch_boton_rojo_a = False
                switch_boton_rojo_b = False
                switch_boton_rojo_c = False
                switch_boton_rojo_d = False
                switch_boton_verde_a = False
                switch_boton_verde_b = False
                switch_boton_verde_c = False
                switch_boton_verde_d = False

            elif boton_salir.rect.collidepoint(pygame.mouse.get_pos()) and menu_principal != False:
                flag = False
                
    if menu_principal == False :        
                
        ventana = agregar_img_a_escena(ventana, DIMENSION_VENTANA, r"graficos\fondo_azul_oscuro.jpg", (0,0))
        ventana = cambiar_status_presentador(ventana, (400,200), r"graficos\guido_pregunta.png", (130, 5))
        ventana.blit(preguntas_superficie, preguntas_rectangulo)
        escribir_texto(ventana, pregunta['pregunta'], fuente_arial_treinta, BLANCO, 195,265)
                
        if switch_boton_a:
            ventana.blit(boton_a_superficie, boton_a_rectangulo)
        elif switch_boton_rojo_a:
            ventana.blit(boton_rojo_superficie, boton_a_rojo_rectangulo)
        elif switch_boton_verde_a:
            ventana.blit(boton_verde_superficie, boton_a_verde_rectangulo)

        if switch_boton_b:
            ventana.blit(boton_b_superficie, boton_b_rectangulo)
        elif switch_boton_rojo_b:
            ventana.blit(boton_rojo_superficie, boton_b_rojo_rectangulo)
        elif switch_boton_verde_b:
            ventana.blit(boton_verde_superficie, boton_b_verde_rectangulo)
        

        if switch_boton_c:
            ventana.blit(boton_c_superficie, boton_c_rectangulo)
        elif switch_boton_rojo_c:
            ventana.blit(boton_rojo_superficie, boton_c_rojo_rectangulo)
        elif switch_boton_verde_c:
            ventana.blit(boton_verde_superficie, boton_c_verde_rectangulo)

        if switch_boton_d:
            ventana.blit(boton_d_superficie, boton_d_rectangulo)
        elif switch_boton_rojo_d:
            ventana.blit(boton_rojo_superficie, boton_d_rojo_rectangulo)
        elif switch_boton_verde_d:
            ventana.blit(boton_verde_superficie, boton_d_verde_rectangulo)

        ventana.blit(banco_superficie, banco_rectangulo)
        
        mostrar_respuestas(ventana, fuente_arial_veinte, pregunta['posibles_respuestas'], 65, 415)

        tiempo_restante = cronometro.actualizar()
        escribir_texto(ventana, f"{tiempo_restante}" , fuente_titulo, BLANCO, 640, 50)

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:

                if boton_a_rectangulo.collidepoint(pygame.mouse.get_pos()) and switch_boton_a:
                    
                    if pregunta['posibles_respuestas'][0] == pregunta['respuesta_correcta']:
                        
        
                        switch_boton_a = not switch_boton_a
                        switch_boton_verde_a = not switch_boton_verde_a
                        print("COOORRECTOOOOOOO")
                    else:
                        
                        
                        switch_boton_a = not switch_boton_a
                        switch_boton_rojo_a = not switch_boton_rojo_a
                        print("BURROOOOOOOO")

                elif boton_b_rectangulo.collidepoint(pygame.mouse.get_pos()) and switch_boton_b:
                    if pregunta['posibles_respuestas'][1] == pregunta['respuesta_correcta']:
                        switch_boton_b = not switch_boton_b
                        switch_boton_verde_b = not switch_boton_verde_b
                        print("COOORRECTOOOOOOO")
                    else:
                        switch_boton_b = not switch_boton_b
                        switch_boton_rojo_b = not switch_boton_rojo_b
                        print("BURROOOOOOOO")

                elif boton_c_rectangulo.collidepoint(pygame.mouse.get_pos()) and switch_boton_c:
                    if pregunta['posibles_respuestas'][2] == pregunta['respuesta_correcta']:
                        switch_boton_c = not switch_boton_c
                        switch_boton_verde_c = not switch_boton_verde_c
                        print("COOORRECTOOOOOOO")
                    else:
                        switch_boton_c = not switch_boton_c
                        switch_boton_rojo_c = not switch_boton_rojo_c
                        print("BURROOOOOOOO")

                elif boton_d_rectangulo.collidepoint(pygame.mouse.get_pos()) and switch_boton_d:
                    if pregunta['posibles_respuestas'][3] == pregunta['respuesta_correcta']:
                        switch_boton_d = not switch_boton_d
                        switch_boton_verde_d = not switch_boton_verde_d
                        print("COOORRECTOOOOOOO")
                    else:
                        switch_boton_d = not switch_boton_d
                        switch_boton_rojo_d = not switch_boton_rojo_d
                        print("BURROOOOOOOO")
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
