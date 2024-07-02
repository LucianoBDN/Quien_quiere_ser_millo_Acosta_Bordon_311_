import pygame
from escenas import *
from boton import *
from datos import *
from texto import *
from niveles import *
from comodines import *
from cronometro import Cronometro
from botones import Boton
from presentador import Presentador
from fondo import Fondo
from banco import Banco

ANCHO_VENTANA = 1280
ALTO_VENTANA = 720
DIMENSION_VENTANA = (ANCHO_VENTANA, ALTO_VENTANA)

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

lista_preguntas = cargar_archivo_json(r"datos\preguntas_y_respuestas.json")

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
            fondo_menu_principal = Fondo(r"graficos\stage.png", DIMENSION_VENTANA)
            fondo_menu_principal.dibujar_fondo(ventana, (0,0))
            presentador_bienvenida = Presentador(r"graficos\guido_static.png",(1050,400))
            presentador_bienvenida.voltear_imagen(presentador_bienvenida.posicion)
            presentador_bienvenida.dibujar(ventana)
            escribir_texto(ventana, "Quien quiere ser millonario?", fuente_titulo, (255,255,255), 310, 100)

        boton_jugar = Boton(560,300,150,50, (28,99,162), (18,79,134), (18,79,134), "Jugar", fuente_arial_treinta)
        Boton.manejar_evento(boton_jugar, evento)
        Boton.dibujar(boton_jugar, ventana,(255,255,255))
        boton_salir = Boton(560,400,150,50, (28,99,162), (18,79,134), (18,79,134), "Salir", fuente_arial_treinta)
       
        Boton.manejar_evento(boton_salir, evento)
        Boton.dibujar(boton_salir, ventana, (255,255,255))

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
                
    if menu_principal == False:        
                
        ventana = agregar_img_a_escena(ventana, DIMENSION_VENTANA, r"graficos\fondo_azul_oscuro.jpg", (0,0))
        presentador_pregunta = Presentador(r"graficos\guido_pregunta.png", (340,105))
        presentador_pregunta.escalar_imagen(presentador_pregunta.posicion, 400, 200)
        presentador_pregunta.voltear_imagen(presentador_pregunta.posicion)
        presentador_pregunta.dibujar(ventana)
        pregunta_superficie = Boton(100, 150, 840, 300, (18,79,134), (18,79,134), (18,79,134), pregunta['pregunta'],fuente_arial_treinta)
        Boton.agregar_imagen_boton(pregunta_superficie, ventana,r"graficos\boton_respuesta.png", pregunta_superficie.rect.width, pregunta_superficie.rect.height, pregunta_superficie.rect.x, pregunta_superficie.rect.y)
        Boton.escribir_sobre_imagen(pregunta_superficie, ventana, (255,255,255))
        banco = Banco(r"graficos\boton_banco.png",(250,350),(100,70))
        banco.dibujar_banco(ventana)
                
        if switch_boton_a:
            boton_a = Boton(5,370,550,200,(18,79,134), (18,79,134), (18,79,134),pregunta['posibles_respuestas'][0],fuente_arial_veinte)
            Boton.agregar_imagen_boton(boton_a, ventana, r"graficos\boton_respuesta.png", boton_a.rect.width, boton_a.rect.height, boton_a.rect.x, boton_a.rect.y)
            Boton.escribir_sobre_imagen(boton_a, ventana, (0,0,0))    
        elif switch_boton_rojo_a:
            boton_a_rojo = Boton(5,370,550,200,(18,79,134), (18,79,134), (18,79,134),pregunta['posibles_respuestas'][0],fuente_arial_veinte)
            Boton.agregar_imagen_boton(boton_a_rojo, ventana, r"graficos\boton_rojo.png", boton_a_rojo.rect.width, boton_a_rojo.rect.height, boton_a_rojo.rect.x, boton_a_rojo.rect.y)
            Boton.escribir_sobre_imagen(boton_a_rojo, ventana, (0,0,0))
        elif switch_boton_verde_a:
            boton_a_verde = Boton(5,370,550,200,(18,79,134), (18,79,134), (18,79,134),pregunta['posibles_respuestas'][0],fuente_arial_veinte)
            Boton.agregar_imagen_boton(boton_a_verde, ventana, r"graficos\boton_verde.png", boton_a_verde.rect.width, boton_a_verde.rect.height, boton_a_verde.rect.x, boton_a_verde.rect.y)
            Boton.escribir_sobre_imagen(boton_a_verde, ventana, (0,0,0))

        if switch_boton_b:
            boton_b = Boton(505,370,550,200,(18,79,134), (18,79,134), (18,79,134),pregunta['posibles_respuestas'][1],fuente_arial_veinte)
            Boton.agregar_imagen_boton(boton_b, ventana, r"graficos\boton_respuesta.png", boton_b.rect.width, boton_b.rect.height, boton_b.rect.x, boton_b.rect.y)
            Boton.escribir_sobre_imagen(boton_b, ventana, (0,0,0))    
        elif switch_boton_rojo_b:
            boton_b_rojo = Boton(505,370,550,200,(18,79,134), (18,79,134), (18,79,134),pregunta['posibles_respuestas'][1],fuente_arial_veinte)
            Boton.agregar_imagen_boton(boton_b_rojo, ventana, r"graficos\boton_rojo.png", boton_b_rojo.rect.width, boton_b_rojo.rect.height, boton_b_rojo.rect.x, boton_b_rojo.rect.y)
            Boton.escribir_sobre_imagen(boton_b_rojo, ventana, (0,0,0))
        elif switch_boton_verde_b:
            boton_b_verde = Boton(505,370,550,200,(18,79,134), (18,79,134), (18,79,134),pregunta['posibles_respuestas'][1],fuente_arial_veinte)
            Boton.agregar_imagen_boton(boton_b_verde, ventana, r"graficos\boton_verde.png", boton_b_verde.rect.width, boton_b_verde.rect.height, boton_b_verde.rect.x, boton_b_verde.rect.y)
            Boton.escribir_sobre_imagen(boton_b_verde, ventana, (0,0,0))
        
        if switch_boton_c:
            boton_c = Boton(5,530,550,200,(18,79,134), (18,79,134), (18,79,134),pregunta['posibles_respuestas'][2],fuente_arial_veinte)
            Boton.agregar_imagen_boton(boton_c, ventana, r"graficos\boton_respuesta.png", boton_c.rect.width, boton_c.rect.height, boton_c.rect.x, boton_c.rect.y)
            Boton.escribir_sobre_imagen(boton_c, ventana, (0,0,0))    
        elif switch_boton_rojo_c:
            boton_c_rojo = Boton(5,530,550,200,(18,79,134), (18,79,134), (18,79,134),pregunta['posibles_respuestas'][2],fuente_arial_veinte)
            Boton.agregar_imagen_boton(boton_c_rojo, ventana, r"graficos\boton_rojo.png", boton_c_rojo.rect.width, boton_c_rojo.rect.height, boton_c_rojo.rect.x, boton_c_rojo.rect.y)
            Boton.escribir_sobre_imagen(boton_c_rojo, ventana, (0,0,0))
        elif switch_boton_verde_c:
            boton_c_verde = Boton(5,530,550,200,(18,79,134), (18,79,134), (18,79,134),pregunta['posibles_respuestas'][2],fuente_arial_veinte)
            Boton.agregar_imagen_boton(boton_c_verde, ventana, r"graficos\boton_verde.png", boton_c_verde.rect.width, boton_c_verde.rect.height, boton_c_verde.rect.x, boton_c_verde.rect.y)
            Boton.escribir_sobre_imagen(boton_c_verde, ventana, (0,0,0))

        if switch_boton_d:
            boton_d = Boton(505,530,550,200,(18,79,134), (18,79,134), (18,79,134),pregunta['posibles_respuestas'][3],fuente_arial_veinte)
            Boton.agregar_imagen_boton(boton_d, ventana, r"graficos\boton_respuesta.png", boton_d.rect.width, boton_d.rect.height, boton_d.rect.x, boton_d.rect.y)
            Boton.escribir_sobre_imagen(boton_d, ventana, (0,0,0))    
        elif switch_boton_rojo_d:
            boton_d_rojo = Boton(505,530,550,200,(18,79,134), (18,79,134), (18,79,134),pregunta['posibles_respuestas'][3],fuente_arial_veinte)
            Boton.agregar_imagen_boton(boton_d_rojo, ventana, r"graficos\boton_rojo.png", boton_d_rojo.rect.width, boton_d_rojo.rect.height, boton_d_rojo.rect.x, boton_d_rojo.rect.y)
            Boton.escribir_sobre_imagen(boton_d_rojo, ventana, (0,0,0))
        elif switch_boton_verde_d:
            boton_d_verde = Boton(505,530,550,200,(18,79,134), (18,79,134), (18,79,134),pregunta['posibles_respuestas'][3],fuente_arial_veinte)
            Boton.agregar_imagen_boton(boton_d_verde, ventana, r"graficos\boton_verde.png", boton_d_verde.rect.width, boton_d_verde.rect.height, boton_d_verde.rect.x, boton_d_verde.rect.y)
            Boton.escribir_sobre_imagen(boton_d_verde, ventana, (0,0,0))
        
        tiempo_restante = cronometro.actualizar()
        escribir_texto(ventana, f"{tiempo_restante}" , fuente_titulo, (255,255,255), 640, 50)

        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:

                if boton_a.rect.collidepoint(pygame.mouse.get_pos()) and switch_boton_a:
                    
                    if pregunta['posibles_respuestas'][0] == pregunta['respuesta_correcta']:
                        
        
                        switch_boton_a = not switch_boton_a
                        switch_boton_verde_a = not switch_boton_verde_a
                        print("COOORRECTOOOOOOO")
                    else:
                                       
                        switch_boton_a = not switch_boton_a
                        switch_boton_rojo_a = not switch_boton_rojo_a
                        print("BURROOOOOOOO")

                elif boton_b.rect.collidepoint(pygame.mouse.get_pos()) and switch_boton_b:
                    if pregunta['posibles_respuestas'][1] == pregunta['respuesta_correcta']:
                        switch_boton_b = not switch_boton_b
                        switch_boton_verde_b = not switch_boton_verde_b
                        print("COOORRECTOOOOOOO")
                    else:
                        switch_boton_b = not switch_boton_b
                        switch_boton_rojo_b = not switch_boton_rojo_b
                        print("BURROOOOOOOO")

                elif boton_c.rect.collidepoint(pygame.mouse.get_pos()) and switch_boton_c:
                    if pregunta['posibles_respuestas'][2] == pregunta['respuesta_correcta']:
                        switch_boton_c = not switch_boton_c
                        switch_boton_verde_c = not switch_boton_verde_c
                        print("COOORRECTOOOOOOO")
                    else:
                        switch_boton_c = not switch_boton_c
                        switch_boton_rojo_c = not switch_boton_rojo_c
                        print("BURROOOOOOOO")

                elif boton_d.rect.collidepoint(pygame.mouse.get_pos()) and switch_boton_d:
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
