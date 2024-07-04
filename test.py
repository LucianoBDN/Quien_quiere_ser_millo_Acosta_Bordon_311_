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
from jugador import Jugador

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

menu_principal = True
flag = True

boton_a = Boton(ventana, 5,370,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte)
boton_b = Boton(ventana, 505,370,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte)
boton_c = Boton(ventana, 5,530,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte)
boton_d = Boton(ventana, 505,530,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte)

 
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

        boton_jugar = Boton(ventana, 560,300,150,50, (28,99,162), (18,79,134), (18,79,134), "Jugar", fuente_arial_treinta)
        Boton.manejar_evento(boton_jugar, evento)
        Boton.dibujar(boton_jugar,(255,255,255))
        boton_salir = Boton(ventana, 560,400,150,50, (28,99,162), (18,79,134), (18,79,134), "Salir", fuente_arial_treinta)
       
        Boton.manejar_evento(boton_salir, evento)
        Boton.dibujar(boton_salir, (255,255,255))

        if evento.type == pygame.QUIT:
            flag = False

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and menu_principal != False:

            if boton_jugar.rect.collidepoint(pygame.mouse.get_pos()):
                
                menu_principal = not menu_principal
                pregunta = seleccionar_pregunta(13, lista_preguntas)
                cronometro.iniciar()

            elif boton_salir.rect.collidepoint(pygame.mouse.get_pos()) and menu_principal != False:
                flag = False
                
    if menu_principal == False:        
                
        ventana = agregar_img_a_escena(ventana, DIMENSION_VENTANA, r"graficos\fondo_azul_oscuro.jpg", (0,0))
        presentador_pregunta = Presentador(r"graficos\guido_pregunta.png", (340,105))
        presentador_pregunta.escalar_imagen(presentador_pregunta.posicion, 400, 200)
        presentador_pregunta.voltear_imagen(presentador_pregunta.posicion)
        presentador_pregunta.dibujar(ventana)
        pregunta_superficie = Boton(ventana, 100, 150, 840, 300, (18,79,134), (18,79,134), (18,79,134), pregunta['pregunta'],fuente_arial_treinta)
        Boton.agregar_imagen_boton(pregunta_superficie, r"graficos\boton_respuesta.png", pregunta_superficie.rect.width, pregunta_superficie.rect.height, pregunta_superficie.rect.x, pregunta_superficie.rect.y)
        Boton.escribir_sobre_imagen(pregunta_superficie, (255,255,255))
        banco = Banco(r"graficos\boton_banco.png",(250,350),(100,70))
        banco.dibujar_banco(ventana)
                
        boton_a.texto = pregunta['posibles_respuestas'][0]
        boton_b.texto = pregunta['posibles_respuestas'][1]
        boton_c.texto = pregunta['posibles_respuestas'][2]
        boton_d.texto = pregunta['posibles_respuestas'][3]
        boton_a.switch_default = True
        boton_b.switch_default = True
        boton_c.switch_default = True
        boton_d.switch_default = True
        player = Jugador()

        tiempo_restante = cronometro.actualizar()
        escribir_texto(ventana, f"{tiempo_restante}" , fuente_titulo, (255,255,255), 640, 50)

        boton_a.manejar_boton(boton_a.switch_default, r"graficos\boton_respuesta.png")
        boton_a.manejar_boton(boton_a.switch_rojo, r"graficos\boton_rojo.png")
        boton_a.manejar_boton(boton_a.switch_verde, r"graficos\boton_verde.png")
        boton_b.manejar_boton(boton_b.switch_default, r"graficos\boton_respuesta.png")
        boton_b.manejar_boton(boton_b.switch_rojo, r"graficos\boton_rojo.png")
        boton_b.manejar_boton(boton_b.switch_verde, r"graficos\boton_verde.png")
        boton_c.manejar_boton(boton_c.switch_default, r"graficos\boton_respuesta.png")
        boton_d.manejar_boton(boton_d.switch_default, r"graficos\boton_respuesta.png")
        boton_c.manejar_boton(boton_c.switch_rojo, r"graficos\boton_rojo.png")
        boton_c.manejar_boton(boton_c.switch_verde, r"graficos\boton_verde.png")
        boton_d.manejar_boton(boton_d.switch_rojo, r"graficos\boton_rojo.png")
        boton_d.manejar_boton(boton_d.switch_verde, r"graficos\boton_verde.png")
               
        for evento in lista_eventos:
            
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:

                if player.vidas > 0 and tiempo_restante > 0:

                    if boton_a.rect.collidepoint(pygame.mouse.get_pos()) and boton_a.switch_default:          
                        player.vidas = manejar_niveles(boton_a, pregunta['respuesta_correcta'], player.vidas)      
                        
                    elif boton_b.rect.collidepoint(pygame.mouse.get_pos()) and boton_b.switch_default:    
                        player.vidas = manejar_niveles(boton_b, pregunta['respuesta_correcta'], player.vidas)

                    elif boton_c.rect.collidepoint(pygame.mouse.get_pos()) and boton_c.switch_default:
                        player.vidas = manejar_niveles(boton_c, pregunta['respuesta_correcta'], player.vidas)

                    elif boton_d.rect.collidepoint(pygame.mouse.get_pos()) and boton_d.switch_default:
                        player.vidas = manejar_niveles(boton_d, pregunta['respuesta_correcta'], player.vidas)


    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
