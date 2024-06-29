import pygame
import random
from texto import *

# Definir la función comodin_publico_barras
def dibujar_barras(ventana, color, x, y, width):

    height = random.randint(30, 100)
    y -= height
    rectangulo = pygame.draw.rect(ventana, color, (x, y, width, height))

    
    return rectangulo


def mostrar_barras(ventana, color, x, y, width, fuente, color_txt):

    opciones = {"A", "B", "C", "D"}

    x_texto = x +18
    y_texto = y -20

    lista_alturas_barras = []

    for opcion in opciones:
        altura = dibujar_barras(ventana, color, x, y, width)
        lista_alturas_barras.append(altura)
        escribir_texto(ventana, opcion ,fuente, color_txt, x_texto, y_texto)

        x_texto += 60
        x += 60

def porcentaje_barras(valores:list):

    suma_total = 0
    for valor in valores:
        suma_total  += valor
    porcentajes = []

    for valor in valores:
        porcentaje = (valor / suma_total) * 100
        porcentajes.append(porcentaje)
        

    return porcentajes


print(porcentaje_barras([50, 35, 47, 66]))
