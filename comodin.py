import pygame
import random
from texto import *
from generales import *

class Comodin:
    def __init__(self) -> None:
        self.llamada = 1
        self.cincuenta = 1
        self.publico = 1
    
    def reiniciar_comodines(self):
        self.llamada = 1
        self.cincuenta = 1
        self.publico = 1

    
    def mostrar_barras(self, ventana, color, x, y, width, fuente, color_txt, height):

        opciones = ["A", "B", "C", "D"]

        x_texto = x +18
        y_texto = y -20

        

        x_porcentaje = x + 18
        y_porcentaje = y - 40
        vuelta = 0

        for i in range(len(height)):
            dibujar_barras(ventana, color, x, y, width, height[i])
            escribir_texto(ventana, opciones[i] ,fuente, color_txt, x_texto, y_texto)
            vuelta += 1
            x_texto += 60
            x += 60

        lista_alturas_barras = porcentaje_barras(height)

        for porcentaje in lista_alturas_barras:
            porcentaje = str(porcentaje)
            escribir_texto(ventana, f"{porcentaje[:4]}%" ,fuente, color_txt, x_porcentaje, y_porcentaje)
            x_porcentaje += 55

        self.publico = 0
        
    def palabra_clave(self,ventana, pista: str, fuente, color_texto, x, y):

        pista = "Pista: " + pista

        escribir_texto(ventana, pista , fuente, color_texto, x, y)

        self.llamada = 0

    
    def comodin_cincuenta(self,lista_respuestas: list, respuesta_correcta) :

        lista_dos_respuesta = []

        lista_dos_respuesta.append(respuesta_correcta)

        for respuesta in lista_respuestas:
            if respuesta != respuesta_correcta:
                if len(lista_dos_respuesta) < 2:
                    lista_dos_respuesta.append(respuesta)
                else:
                    respuesta = "----------------"
                    lista_dos_respuesta.append(respuesta)
        
        self.cincuenta = 0

        return lista_dos_respuesta 