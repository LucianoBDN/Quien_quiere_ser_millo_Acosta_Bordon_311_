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

menu_principal_status = True
pantalla_juego = True
flag = True
player = Jugador()
nivel_jugador = player.nivel
pregunta = seleccionar_pregunta(nivel_jugador, lista_preguntas)
cronometro = Cronometro(15)
pausa = False

boton_a = Boton(ventana, 5,370,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte)
boton_b = Boton(ventana, 505,370,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte)
boton_c = Boton(ventana, 5,530,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte)
boton_d = Boton(ventana, 505,530,550,200,(18,79,134), (18,79,134), (18,79,134),"",fuente_arial_veinte)
boton_volver = Boton(ventana, 970, 200, 200, 100, (0,0,0), (0,0,0), (0,0,0), "Volver al menú principal", fuente_arial_quince)
boton_jugar = Boton(ventana, 560,300,150,50, (28,99,162), (18,79,134), (18,79,134), "Jugar", fuente_arial_treinta)
boton_salir = Boton(ventana, 560,400,150,50, (28,99,162), (18,79,134), (18,79,134), "Salir", fuente_arial_treinta)
boton_continuar = Boton(ventana, 970, 200, 200, 100, (0,0,0), (0,0,0), (0,0,0), "Continuar", fuente_arial_quince)


while flag:

    lista_eventos = pygame.event.get()

    for evento in lista_eventos:
        
        if evento.type == pygame.QUIT:
            flag = False
        
    if menu_principal_status == True:
        
        fondo_menu_principal = Fondo(r"graficos\stage.png", DIMENSION_VENTANA)
        fondo_menu_principal.dibujar_fondo(ventana, (0,0))
        presentador_bienvenida = Presentador(r"graficos\guido_static.png",(1050,400))
        presentador_bienvenida.voltear_imagen(presentador_bienvenida.posicion)
        presentador_bienvenida.dibujar(ventana)
        escribir_texto(ventana, "Quien quiere ser millonario?", fuente_titulo, (255,255,255), 310, 100)
        boton_jugar.dibujar((255,255,255))    
        boton_salir.dibujar((255,255,255))
        boton_jugar.manejar_evento(evento)
        boton_salir.manejar_evento(evento)

        if boton_jugar.es_click():
                
            menu_principal_status = False
            cronometro.iniciar()

        elif boton_salir.es_click():
            flag = False  
    
    elif menu_principal_status == False:        
    
        tiempo_restante = cronometro.actualizar()
        
        ventana = agregar_img_a_escena(ventana, DIMENSION_VENTANA, r"graficos\fondo_azul_oscuro.jpg", (0,0))
        escribir_texto(ventana, f"{tiempo_restante}" , fuente_titulo, (255,255,255), 640, 50)
        presentador_pregunta = Presentador(r"graficos\guido_pregunta.png", (340,105))
        presentador_pregunta.escalar_imagen(presentador_pregunta.posicion, 400, 200)
        presentador_pregunta.voltear_imagen(presentador_pregunta.posicion)
        presentador_pregunta.dibujar(ventana)
        pregunta_superficie = Boton(ventana, 100, 150, 840, 300, (18,79,134), (18,79,134), (18,79,134), pregunta['pregunta'],fuente_arial_treinta)
        pregunta_superficie.agregar_imagen_boton(r"graficos\boton_respuesta.png", pregunta_superficie.rect.width, pregunta_superficie.rect.height, pregunta_superficie.rect.x, pregunta_superficie.rect.y)
        pregunta_superficie.escribir_sobre_imagen((255,255,255))
        
        banco = Banco(r"graficos\boton_banco.png",(250,350),(100,70))
        banco.dibujar_banco(ventana)
        
        boton_a.manejar_evento(evento)
        boton_b.manejar_evento(evento)
        boton_c.manejar_evento(evento)
        boton_d.manejar_evento(evento)
        boton_volver.manejar_evento(evento)                 
        boton_a.texto = pregunta['posibles_respuestas'][0]
        boton_b.texto = pregunta['posibles_respuestas'][1]
        boton_c.texto = pregunta['posibles_respuestas'][2]
        boton_d.texto = pregunta['posibles_respuestas'][3]

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

        if player.vidas == 1 and pausa == False:

            if boton_a.es_click():          
                if player.aumentar_nivel(boton_a, pregunta['respuesta_correcta']):
                    cronometro.reiniciar()
                    pausa = True  
                
            elif boton_b.es_click():    
                if player.aumentar_nivel(boton_b, pregunta['respuesta_correcta']):
                    cronometro.reiniciar()
                    pausa = True


            elif boton_c.es_click():
                if player.aumentar_nivel(boton_c, pregunta['respuesta_correcta']):
                    cronometro.reiniciar()
                    pausa = True

            elif boton_d.es_click():
                if player.aumentar_nivel(boton_d, pregunta['respuesta_correcta']):
                    cronometro.reiniciar()
                    pausa = True

        elif pausa == True:

            boton_continuar.dibujar((255,255,255))
            boton_continuar.manejar_evento(evento)
            
            if boton_continuar.es_click():
                    pausa = False
                    boton_a.reiniciar_switches()
                    boton_b.reiniciar_switches()
                    boton_c.reiniciar_switches()
                    boton_d.reiniciar_switches()
                    pregunta = seleccionar_pregunta(player.nivel, lista_preguntas)
                    cronometro.iniciar()
                
        elif player.vidas == 0:
                           
            boton_volver.dibujar((255,255,255))
            boton_volver.manejar_evento(evento)

            if boton_volver.es_click():
                
                player.vidas = 1
                menu_principal_status = True
                print(menu_principal_status)
        

    pygame.display.update()
    clock.tick(60)

pygame.quit()
