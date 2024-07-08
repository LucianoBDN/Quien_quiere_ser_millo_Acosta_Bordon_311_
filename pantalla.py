import pygame
from fondo import Fondo
from presentador import Presentador
from texto import *
from imagen import *




def mostrar_menu_principal(ventana, path_fondo: str, dimensiones_fondo: tuple[int, int], path_presentador: str, posicion_presentador: tuple[int, int], ancho_presentador: int, alto_presentador: int, texto_titulo: str, fuente_titulos: str, color_titulo:tuple[int, int, int], x_titulo: int, y_titulo: int):



            fondo_menu_principal = Fondo(path_fondo, (dimensiones_fondo))
            fondo_menu_principal.dibujar_fondo(ventana, (0,0))
            presentador_bienvenida = Presentador(path_presentador,(posicion_presentador))
            presentador_bienvenida.escalar_imagen(posicion_presentador,ancho_presentador, alto_presentador)
            presentador_bienvenida.voltear_imagen(presentador_bienvenida.posicion)
            presentador_bienvenida.dibujar(ventana)
            escribir_texto(ventana, texto_titulo, fuente_titulos, color_titulo, x_titulo, y_titulo)



def mostrar_pantalla_juego(ventana, path_fondo: str, dimensiones_fondo: tuple[int, int], path_presentador: str, posicion_presentador: tuple[int, int], ancho_presentador: int, alto_presentador: int, voltear_img: bool,path_banco, dimension_banco: tuple[int,int], posicion_banco: tuple[int,int], score: int, fuente_score: str, color_texto_score: tuple[int, int, int], path_rect_pregunta: str, dimension_rect_reguntas: tuple[int, int], posicion_rect_preguntas: tuple[int, int],fuente_rect_pregunta:str, texto_rect_pregunta: str, color_texto_pregunta: tuple[int, int, int]):


        
        fondo_menu_principal = Fondo(path_fondo, dimensiones_fondo)
        fondo_menu_principal.dibujar_fondo(ventana, (0,0))
        presentador_bienvenida = Presentador(path_presentador,(posicion_presentador))
        presentador_bienvenida.escalar_imagen(posicion_presentador,ancho_presentador, alto_presentador)



        if voltear_img == True:
                presentador_bienvenida.voltear_imagen(presentador_bienvenida.posicion)



        presentador_bienvenida.dibujar(ventana)



        banco = Imagen(path_banco, dimension_banco, posicion_banco)
        banco.dibujar_imagen(ventana)
        banco.escribir_imagen(ventana,fuente_score, f"${score}", color_texto_score)



        rect_pregunta = Imagen(path_rect_pregunta, dimension_rect_reguntas, posicion_rect_preguntas)
        rect_pregunta.dibujar_imagen(ventana)
        rect_pregunta.escribir_imagen(ventana, fuente_rect_pregunta, texto_rect_pregunta, color_texto_pregunta)
        
