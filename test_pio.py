import pygame
from ventana import *
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


pygame.init()

ventana = setear_ventana("¿Quién quiere ser millonario?", r"logos\utnavellaneda.jpg", 1280, 720)

fuente_arial_quince = pygame.font.SysFont("Arial",18)
fuente_arial_veinte = pygame.font.SysFont("Arial",20, bold=True)
fuente_arial_treinta = pygame.font.SysFont("Arial",30)
fuente_titulo = pygame.font.Font(r"fuentes\Audiowide.ttf", 40)

clock = pygame.time.Clock()

lista_preguntas = cargar_archivo_json(r"datos\preguntas_y_respuestas.json")

menu_principal = True
jugando = False
pausa = False
flag = True
resultado_respuesta = None
player = Jugador()

boton_a = Boton(ventana, 5,370,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte)
boton_b = Boton(ventana, 505,370,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte)
boton_c = Boton(ventana, 5,530,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte)
boton_d = Boton(ventana, 505,530,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte)
boton_continuar = Boton(ventana, 870,270,150,50, (28,99,162), (18,79,134), (18,79,134), "Continuar", fuente_arial_quince)
boton_retirarse = Boton(ventana, 870,330,150,50, (28,99,162), (18,79,134), (18,79,134), "Retirarse", fuente_arial_quince)
boton_volver = Boton(ventana, 870,330,150,50, (28,99,162), (18,79,134), (18,79,134), "Volver al menú principal", fuente_arial_quince)

 
cronometro = Cronometro(30)

while flag:

    lista_eventos = pygame.event.get()
    
    
    for evento in lista_eventos:
          
        if evento.type == pygame.QUIT:
            flag = False

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and menu_principal == True:

            if boton_jugar.rect.collidepoint(pygame.mouse.get_pos()):
                
                menu_principal = not menu_principal
                jugando = True
                pregunta = seleccionar_pregunta(player.nivel, lista_preguntas)
                cronometro.iniciar()

            elif boton_salir.rect.collidepoint(pygame.mouse.get_pos()):
                flag = False

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and menu_principal == False and jugando == True and pausa == False:

            if player.vidas > 0 and tiempo_restante > 0:

                if boton_a.rect.collidepoint(pygame.mouse.get_pos()) and boton_a.switch_default == True:          
                    resultado_respuesta = manejar_niveles(boton_a, pregunta['respuesta_correcta'])      
                    
                elif boton_b.rect.collidepoint(pygame.mouse.get_pos()) and boton_b.switch_default == True:    
                    resultado_respuesta = manejar_niveles(boton_b, pregunta['respuesta_correcta'])

                elif boton_c.rect.collidepoint(pygame.mouse.get_pos()) and boton_c.switch_default == True:
                    resultado_respuesta = manejar_niveles(boton_c, pregunta['respuesta_correcta'])

                elif boton_d.rect.collidepoint(pygame.mouse.get_pos()) and boton_d.switch_default == True:
                    resultado_respuesta = manejar_niveles(boton_d, pregunta['respuesta_correcta'])

        elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and resultado_respuesta == True and pausa == True and jugando == False:

            if boton_continuar.rect.collidepoint(pygame.mouse.get_pos()):

                resultado_respuesta = None
                jugando = True
                pausa = False
                boton_a.reiniciar_switches()
                boton_b.reiniciar_switches()
                boton_c.reiniciar_switches()
                boton_d.reiniciar_switches()
                player.aumentar_nivel_y_monto()
                cronometro.iniciar()
                pregunta = seleccionar_pregunta(player.nivel, lista_preguntas)

            elif boton_retirarse.rect.collidepoint(pygame.mouse.get_pos()):
                pass
                #Acá va lo que pasa si se retira en vez de seguir jugando

        elif (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and resultado_respuesta == False and pausa == True and jugando == False) or (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and cronometro.tiempo_restante == 0):
            
            if boton_volver.rect.collidepoint(pygame.mouse.get_pos()):

                menu_principal = True
                pausa = False
                resultado_respuesta = None
                boton_a.reiniciar_switches()
                boton_b.reiniciar_switches()
                boton_c.reiniciar_switches()
                boton_d.reiniciar_switches()
                player.nivel = 1
        

    if menu_principal:
            
            fondo_menu_principal = Fondo(r"graficos\stage.png", (1280, 720))
            fondo_menu_principal.dibujar_fondo(ventana, (0,0))
            presentador_bienvenida = Presentador(r"graficos\guido_static.png",(1050,400))
            presentador_bienvenida.voltear_imagen(presentador_bienvenida.posicion)
            presentador_bienvenida.dibujar(ventana)
            escribir_texto(ventana, "Quien quiere ser millonario?", fuente_titulo, (255,255,255), 310, 100)

            boton_jugar = Boton(ventana, 560,300,150,50, (28,99,162), (18,79,134), (18,79,134), "Jugar", fuente_arial_treinta)
            boton_salir = Boton(ventana, 560,400,150,50, (28,99,162), (18,79,134), (18,79,134), "Salir", fuente_arial_treinta)
            Boton.manejar_evento(boton_jugar, evento)
            Boton.manejar_evento(boton_salir, evento)
            Boton.dibujar(boton_jugar,(255,255,255))
            Boton.dibujar(boton_salir, (255,255,255))            
        
                
    if menu_principal == False:        
                
        ventana = agregar_img_a_escena(ventana, (1280, 720), r"graficos\fondo_azul_oscuro.jpg", (0,0))
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

        if resultado_respuesta == True:

            cronometro.reiniciar()
            pausa = True
            jugando = False 
            boton_continuar.manejar_evento(evento)
            boton_retirarse.manejar_evento(evento)
            boton_continuar.dibujar((255,255,255))
            boton_retirarse.dibujar((255,255,255))

        elif resultado_respuesta == False:

            cronometro.reiniciar()
            pausa = True
            jugando = False 
            boton_volver.manejar_evento(evento)
            boton_volver.dibujar((255,255,255))

        elif tiempo_restante == 0:

            pausa = True
            jugando = False 
            boton_volver.manejar_evento(evento)
            boton_volver.dibujar((255,255,255))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
