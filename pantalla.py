import pygame
from fondo import Fondo
from presentador import Presentador
from botones import Boton
from texto import *
from imagen import *




def pantalla_menu_principal(ventana, dict_switches: dict, lista_botones: list, lista_eventos: list):
        

        if dict_switches['menu_principal'] == True:
                fondo_menu_principal = Fondo(r"graficos\stage.png", (1280,720))
                fondo_menu_principal.dibujar_fondo(ventana, (0,0))
                presentador_bienvenida = Presentador(r"graficos\guido_static.png",(1050, 400))
                presentador_bienvenida.escalar_imagen((1050, 400),550,700)
                presentador_bienvenida.voltear_imagen(presentador_bienvenida.posicion)
                presentador_bienvenida.dibujar(ventana)
                escribir_texto(ventana, "¿Quien quiere ser millonario?", pygame.font.Font(r"fuentes\Audiowide.ttf", 40) , (255,255,255), 310, 100)
                
                for Boton in lista_botones:
                        if Boton.nombre == "boton_jugar" or Boton.nombre == "boton_salir":
                                Boton.dibujar((255,255,255))
                                Boton.manejar_evento(lista_eventos)
        
                                




def pantalla_juego(ventana, dict_switches: dict, score: int, texto_cuadro_pregunta: str, lista_botones: list, lista_comodines, pregunta):


        if dict_switches['menu_principal'] == False:
                fondo_juego = Fondo(r"graficos\fondo_azul_oscuro.jpg", (1280, 720))
                fondo_juego.dibujar_fondo(ventana, (0,0))
                presentador_juego = Presentador(r"graficos\guido_pregunta.png",(340,105))
                presentador_juego.escalar_imagen((340,105),400, 200)
                presentador_juego.voltear_imagen(presentador_juego.posicion)

                presentador_juego.dibujar(ventana)



                banco = Imagen(r"graficos\boton_banco.png", (280,350), (110,70))
                banco.dibujar_imagen(ventana)
                banco.escribir_imagen(ventana,pygame.font.Font(r"fuentes\Audiowide.ttf", 30), f"${score}", (255,223,0))



                cuadro_pregunta = Imagen(r"graficos\boton_respuesta.png", (840, 300), (500,300))
                cuadro_pregunta.dibujar_imagen(ventana)
                cuadro_pregunta.escribir_imagen(ventana, pygame.font.SysFont("Arial",25, bold=True), texto_cuadro_pregunta, (255,255,255))
                
                
                mostrar_respuestas(lista_botones, r"graficos\boton_respuesta.png", pregunta)
                mostrar_comodines(lista_comodines, lista_botones, r"graficos\publico.png", r"graficos\llamada.png", r"graficos\50_50.png")



def mostrar_respuestas(lista_botones: list, path_boton: str, pregunta):
        
        for boton in lista_botones:

                match boton.nombre:

                        case "boton_a":
                                boton.agregar_imagen_boton(path_boton,550,200,5,370)
                                boton.escribir_sobre_imagen(pregunta.respuesta_a ,(255,255,255))

                        case "boton_b":
                                boton.agregar_imagen_boton(path_boton,550,200,505,370)
                                boton.escribir_sobre_imagen(pregunta.respuesta_b,(255,255,255))

                        case "boton_c":
                                boton.agregar_imagen_boton(path_boton,550,200,5,530)
                                boton.escribir_sobre_imagen(pregunta.respuesta_c,(255,255,255))

                        case "boton_d":
                                boton.agregar_imagen_boton(path_boton,550,200,505,530)
                                boton.escribir_sobre_imagen(pregunta.respuesta_d,(255,255,255))

                              
                
def mostrar_comodines(lista_comodines:list, lista_botones: list, path_comodin_publico, path_comodin_llamada, path_comodin_cincuenta):
        
        for boton in lista_botones:

                match boton.nombre:

                        case "boton_publico":
                                boton.agregar_imagen_boton(path_comodin_publico, 60,60,1000,10)
                        case "boton_llamada":
                                boton.agregar_imagen_boton(path_comodin_llamada,50,50,1100,10)
                        case "boton_cincuenta":        
                                boton.agregar_imagen_boton(path_comodin_cincuenta,50,50,1200,10)
                                

def pantalla_perdiste(ventana, lista_botones: list, lista_eventos):

        fondo_menu_principal = Fondo(r"graficos\fondo_azul_oscuro.jpg", (1280,720))
        fondo_menu_principal.dibujar_fondo(ventana, (0,0))
        presentador_perdiste = Presentador(r"graficos\guido_triste.png",(400,250))
        presentador_perdiste.escalar_imagen((400,250), 600, 500)
        presentador_perdiste.voltear_imagen(presentador_perdiste.posicion)
        presentador_perdiste.dibujar(ventana)

        escribir_texto(ventana,"PERDISTE SOS HORRIBLE",pygame.font.SysFont("Arial",50, bold=True), (255,255,255), 300, 600)

        for boton in lista_botones:
                if boton.nombre == "boton_volver":
                        Boton.dibujar(boton, (255,255,255))
                        Boton.manejar_evento(boton,lista_eventos)


def pantalla_score(ventana, lista_score, y):

        fondo_score = Fondo(r"graficos\fondo_azul_oscuro.jpg", (1280,720))
        fondo_score.dibujar_fondo(ventana, (0,0))
        presentador_score = Presentador(r"graficos\guido_respuesta_bien.png",(200,250))
        presentador_score.escalar_imagen((300,350), 750, 750)
        
        presentador_score.dibujar(ventana)

        for score in lista_score:
                escribir_texto(ventana, score[0],pygame.font.SysFont("Arial",40, bold=True) , (255,255,255), 700 , y)
                escribir_texto(ventana, score[1],pygame.font.SysFont("Arial",40, bold=True) , (255,255,255), 900, y)
                y += 70




