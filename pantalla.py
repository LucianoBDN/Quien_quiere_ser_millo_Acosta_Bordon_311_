import pygame
from fondo import Fondo
from presentador import Presentador
from botones import Boton
from texto import *
from imagen import *




def pantalla_menu_principal(ventana, dict_switches: dict, lista_botones: list, lista_eventos: list):
        """Muestra todo lo grafico que se ve en el menu principal

        Args:
            ventana (suface): superficie donde se vera el menu
            dict_switches (dict): diccionario de banderas
            lista_botones (list): lista de botones que se muetran en el menu
            lista_eventos (list): eventos de pygame
        """
        

        if dict_switches['menu_principal'] == True:
                fondo_menu_principal = Fondo(r"graficos\stage.png", (1280,720))
                fondo_menu_principal.dibujar_fondo(ventana, (0,0))
                presentador_bienvenida = Presentador(r"graficos\guido_static.png",(1050, 400))
                presentador_bienvenida.escalar_imagen((1050, 400),550,700)
                presentador_bienvenida.voltear_imagen(presentador_bienvenida.posicion)
                presentador_bienvenida.dibujar(ventana)
                escribir_texto(ventana, "¿Quien quiere ser millonario?", pygame.font.Font(r"fuentes\Audiowide.ttf", 40) , (255,255,255), 310, 100)
                
                for boton in lista_botones:
                        if boton.nombre == "boton_jugar" or boton.nombre == "boton_salir" or boton.nombre == "boton_score":
                                boton.dibujar((255,255,255))
                                boton.manejar_evento(lista_eventos)
        
                                




def pantalla_juego(ventana, dict_switches: dict, score: int, lista_botones: list, lista_comodines: list, pregunta: object, jugador: object, lista_eventos:list, cronometro: object) :
        """muestra todo lo grafico que se vera en la pantalla de juego para su funcionamiento

        Args:
            ventana (surface): donde se vera
            dict_switches (dict): diccionario de banderas
            score (int): putnuacion del jugador
            lista_botones (list): lista de botones para el uso de esta pantalla
            lista_comodines (list): comodines que se pueden usar aqui
            pregunta (object): objeto pregunta 
            jugador (object): objeto jugador
            lista_eventos (list): eventos de pygame
            cronometro (object): objeto cronometro
        """

        
        if dict_switches['menu_principal'] == False and dict_switches['jugando'] == True and jugador.nivel < 16:
                fondo_juego = Fondo(r"graficos\fondo_azul_oscuro.jpg", (1280, 720))
                fondo_juego.dibujar_fondo(ventana, (0,0))
                presentador_juego = Presentador(r"graficos\guido_pregunta.png",(340,105))
                presentador_juego.escalar_imagen((340,105),400, 200)
                presentador_juego.voltear_imagen(presentador_juego.posicion)

                presentador_juego.dibujar(ventana)



                banco = Imagen(r"graficos\boton_banco.png", (280,350), (110,70))
                banco.dibujar_imagen(ventana)
                banco.escribir_imagen(ventana,pygame.font.Font(r"fuentes\Audiowide.ttf", 30), f"${jugador.score}", (255,223,0))



                cuadro_pregunta = Imagen(r"graficos\boton_respuesta.png", (840, 300), (500,300))
                cuadro_pregunta.dibujar_imagen(ventana)
                cuadro_pregunta.escribir_imagen(ventana, pygame.font.SysFont("Arial",22, bold=True), pregunta.pregunta, (255,255,255))
                
                tiempo_restante = cronometro.actualizar()
                escribir_texto(ventana, f"{tiempo_restante}" , pygame.font.Font(r"fuentes\Audiowide.ttf", 40), (255,255,255), 540, 50)


                mostrar_respuestas(lista_botones, r"graficos\boton_respuesta.png", r"graficos\boton_verde.png", r"graficos\boton_rojo.png", pregunta)
                mostrar_comodines(ventana, lista_comodines, lista_botones, r"graficos\publico.png", r"graficos\llamada.png", r"graficos\50_50.png", pregunta)

                if dict_switches['pausa'] == True and dict_switches['resultado_respuesta'] == True:
                        mostrar_botones_pausa(lista_botones, jugador, lista_eventos)



def mostrar_botones_pausa(lista_botones: list, jugador: object, lista_eventos: list):
        """muestra los botones de pausa y retirarse 

        Args:
            lista_botones (list): lista con los botones
            jugador (object): obejto
            lista_eventos (list): eventos de pygame
        """

        for boton in lista_botones:

                match boton.nombre:

                        case "boton_continuar":
                                boton.dibujar((255,255,255))
                                boton.manejar_evento(lista_eventos)

                        case "boton_retirarse":
                                if jugador.nivel == 4 or jugador.nivel == 9:

                                        boton.dibujar((255,255,255))
                                        boton.manejar_evento(lista_eventos)






def mostrar_respuestas(lista_botones: list, path_boton: str, path_boton_verde: str, path_boton_rojo: str, pregunta: object):
        """muestra los botones con el cuadro de respuesta y la respuesta correspondiente a cada opcion

        Args:
            lista_botones (list): lista con los botones
            path_boton (str): url de la imagen del boton default
            path_boton_verde (str): url con la imagen del boton cuando la respuesta es correcta
            path_boton_rojo (str): url con la imagen del boton cuando la respuesta es erronea
            pregunta (object): clase pregunta
        """
        
        


        for boton in lista_botones:

                match boton.nombre:

                        case "boton_a":
                                if boton.switch_default:

                                        boton.agregar_imagen_boton(path_boton,550,200,5,370)
                                        boton.cambiar_texto(pregunta.respuesta_a)
                                        boton.escribir_sobre_imagen(pregunta.respuesta_a ,(255,255,255))
                                
                                elif boton.switch_verde:

                                        boton.agregar_imagen_boton(path_boton_verde,550,200,5,370)
                                        boton.escribir_sobre_imagen(pregunta.respuesta_a ,(255,255,255))
                                        
                                elif boton.switch_rojo:
                                        boton.agregar_imagen_boton(path_boton_rojo,550,200,505,370)
                                        boton.escribir_sobre_imagen(pregunta.respuesta_a,(255,255,255))

                                        
                        case "boton_b":
                                if boton.switch_default:

                                        boton.agregar_imagen_boton(path_boton,550,200,505,370)
                                        boton.cambiar_texto(pregunta.respuesta_b)
                                        boton.escribir_sobre_imagen(pregunta.respuesta_b,(255,255,255))

                                elif boton.switch_verde:
                                        boton.agregar_imagen_boton(path_boton_verde,550,200,505,370)
                                        boton.escribir_sobre_imagen(pregunta.respuesta_b,(255,255,255))
                                
                                elif boton.switch_rojo:
                                        boton.agregar_imagen_boton(path_boton_rojo,550,200,505,370)
                                        boton.escribir_sobre_imagen(pregunta.respuesta_b,(255,255,255))
                                

                        case "boton_c":

                                if boton.switch_default:

                                        boton.agregar_imagen_boton(path_boton,550,200,5,530)
                                        boton.cambiar_texto(pregunta.respuesta_c)
                                        boton.escribir_sobre_imagen(pregunta.respuesta_c,(255,255,255))

                                elif boton.switch_verde:
                                        boton.agregar_imagen_boton(path_boton_verde,550,200,5,530)
                                        boton.escribir_sobre_imagen(pregunta.respuesta_c,(255,255,255))

                                elif boton.switch_rojo:
                                        boton.agregar_imagen_boton(path_boton_rojo,550,200,505,370)
                                        boton.escribir_sobre_imagen(pregunta.respuesta_c,(255,255,255))

                        case "boton_d":
                                
                                if boton.switch_default:

                                        boton.agregar_imagen_boton(path_boton,550,200,505,530)
                                        boton.cambiar_texto(pregunta.respuesta_d)
                                        boton.escribir_sobre_imagen(pregunta.respuesta_d,(255,255,255))


                                elif boton.switch_verde:

                                        boton.agregar_imagen_boton(path_boton_verde,550,200,505,530)
                                        boton.escribir_sobre_imagen(pregunta.respuesta_d,(255,255,255))

                                elif boton.switch_rojo:
                                        boton.agregar_imagen_boton(path_boton_rojo,550,200,505,370)
                                        boton.escribir_sobre_imagen(pregunta.respuesta_d,(255,255,255))

                        
                
def mostrar_comodines(ventana, lista_comodines:list, lista_botones: list, path_comodin_publico: str, path_comodin_llamada: str, path_comodin_cincuenta: str, pregunta: object):
        """muestra en pantalla los comodines que se pueden utiizar una unica vez por partida

        Args:
            ventana (surface): superficie donde se muestra
            lista_comodines (list): lista de comodines a usar
            lista_botones (list): lista de botones que se utilizar para llamar a los comodines
            path_comodin_publico (str): imagen del comodin de ayuda de publico
            path_comodin_llamada (str): imagen del comodin de llamada
            path_comodin_cincuenta (str): imagen del comodin 50/50
            pregunta (object): clase pregunta
        """


        for boton in lista_botones:

                match boton.nombre:

                        case "boton_publico":
                                boton.agregar_imagen_boton(path_comodin_publico, 60,60,1000,10)
                                
                                
                        case "boton_llamada":
                                boton.agregar_imagen_boton(path_comodin_llamada,50,50,1100,10)

                        case "boton_cincuenta":        
                                boton.agregar_imagen_boton(path_comodin_cincuenta,50,50,1200,10)


        for comodin in lista_comodines:

                match comodin.nombre:

                        case "comodin_publico":
                                if comodin.activo == True:
                                        comodin.mostrar_barras(ventana, (255,255,255), 700, 150, 50, pygame.font.SysFont("Arial",18), (0,0,0))
                        
                        case "comodin_llamada":
                                if comodin.activo == True:
                                        comodin.palabra_clave(ventana, pregunta.pista, pygame.font.SysFont("Arial",18), (255,255,255), 600, 153)

                        case "comodin_cincuenta":
                                if comodin.activo == True:
                                        comodin.cincuenta(pregunta)



def pantalla_perdiste(ventana, lista_botones: list, lista_eventos: list, switches: dict, cronometro: object):
        """muestra una pantalla cuando la respuesta que diste es equivocada o el tiempo es 0

        Args:
            ventana (ventana): donde se muestra
            lista_botones (list): lista de botones
            lista_eventos (list): eventos de pygame
            switches (dict): diccionario de banderas
            cronometro (object): clase cronometro
        """


        tiempo_restante = cronometro.actualizar()

        if (switches['resultado_respuesta'] == False and switches['jugando'] == False and switches['menu_principal'] == False) or (tiempo_restante ==0):
                fondo_menu_principal = Fondo(r"graficos\fondo_azul_oscuro.jpg", (1280,720))
                fondo_menu_principal.dibujar_fondo(ventana, (0,0))
                presentador_perdiste = Presentador(r"graficos\guido_triste.png",(400,250))
                presentador_perdiste.escalar_imagen((400,250), 600, 500)
                presentador_perdiste.voltear_imagen(presentador_perdiste.posicion)
                presentador_perdiste.dibujar(ventana)

                escribir_texto(ventana,"PERDISTE",pygame.font.SysFont("Arial",50, bold=True), (255,255,255), 300, 600)

                for boton in lista_botones:
                        if boton.nombre == "boton_volver":
                                Boton.dibujar(boton, (255,255,255))
                                Boton.manejar_evento(boton,lista_eventos)


def pantalla_score(ventana, lista_score: list, switches: dict, lista_botones: list, lista_eventos, jugador: object):
        """muestra en pantalla los higscore

        Args:
            ventana (surface): superficie
            lista_score (list): lista de puntuaciones
            switches (dict): dict de banderas
            lista_botones (list): botones
            lista_eventos (_type_): eventos de pygame
        """


        y = 90

        if switches['menu_principal'] == False and switches['jugando'] == False and switches['pantalla_score']:
                fondo_score = Fondo(r"graficos\fondo_azul_oscuro.jpg", (1280,720))
                fondo_score.dibujar_fondo(ventana, (0,0))
                presentador_score = Presentador(r"graficos\guido_respuesta_bien.png",(200,250))
                presentador_score.escalar_imagen((300,350), 750, 750)
                
                presentador_score.dibujar(ventana)


                for score in lista_score:
                        escribir_texto(ventana, score[0],pygame.font.SysFont("Arial",40, bold=True) , (255,255,255), 700 ,  y)
                        escribir_texto(ventana, f"{score[1]}",pygame.font.SysFont("Arial",40, bold=True) , (255,255,255), 900 ,  y)
                        y += 70

                for boton in lista_botones:

                        if boton.nombre == "boton_volver":
                                Boton.manejar_evento(boton,lista_eventos)
                                boton.dibujar((255,255,255))




def pantalla_retirarse(ventana, lista_score: list[list], jugador: object, switches: dict, lista_eventos: list):
        """muestra esta pantalla cuando el jugador decide retirarse o gana el juego

        Args:
            ventana (surface): donde se muestra
            lista_score (list[list]): lista de puntuaciones
            jugador (object): clase jugador
            switches (dict): diccionario de banderas
            lista_eventos (list): eventos d pygame
        """

        if (switches['retirarse'] == True and switches['jugando'] == False and switches['menu_principal'] == False) or jugador.nivel == 16:
                fondo_menu_principal = Fondo(r"graficos\fondo_azul_oscuro.jpg", (1280,720))
                fondo_menu_principal.dibujar_fondo(ventana, (0,0))
                presentador_bienvenida = Presentador(r"graficos\guido_feliz_sinfondo.png",(400, 390))
                presentador_bienvenida.escalar_imagen((400, 390),1134,664)
                presentador_bienvenida.voltear_imagen(presentador_bienvenida.posicion)
                presentador_bienvenida.dibujar(ventana)
                escribir_texto(ventana, "Sos un crack GANASTE:", pygame.font.Font(r"fuentes\Audiowide.ttf", 40) , (255,255,255), 550, 60)
                escribir_texto(ventana, f"${jugador.score}", pygame.font.Font(r"fuentes\Audiowide.ttf", 45) , (255,223,0), 700, 150)
                escribir_texto(ventana, "Escribe tu nombre para guardar tu puntuacion", pygame.font.Font(r"fuentes\Audiowide.ttf", 20) , (255,255,255), 600, 300)
                
                jugador.nombre = jugador.manejar_evento_jugador(lista_eventos, jugador.nombre, switches, lista_score, r"datos\score.csv")



                escribir_texto(ventana, f"{jugador.nombre}", pygame.font.Font(r"fuentes\Audiowide.ttf", 40) , (255,255,255), 800, 400)



