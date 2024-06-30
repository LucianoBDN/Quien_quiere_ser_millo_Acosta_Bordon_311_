import pygame
import random
from texto import *

# Definir la función comodin_publico_barras

numero_aleatorio = lambda inicio, fin: random.randint(inicio, fin)


def dibujar_barras(ventana, color, x, y, width, height):

    y -= height
    rectangulo = pygame.draw.rect(ventana, color, (x, y, width, height))

    
    return rectangulo


def mostrar_barras(ventana, color, x, y, width, fuente, color_txt):

    opciones = {"A", "B", "C", "D"}

    x_texto = x +18
    y_texto = y -20

    lista_alturas_barras = []

    x_porcentaje = x + 18
    y_porcentaje = y - 40

    for opcion in opciones:
        height = numero_aleatorio(30,100)
        dibujar_barras(ventana, color, x, y, width, height)
        escribir_texto(ventana, opcion ,fuente, color_txt, x_texto, y_texto)
        lista_alturas_barras.append(height)
    
        x_texto += 60
        x += 60

        

    for porcentaje in lista_alturas_barras:
        escribir_texto(ventana, f"{porcentaje}%" ,fuente, color_txt, x_porcentaje, y_porcentaje)
        x_porcentaje += 60
        

    


def porcentaje_barras(valores:list):

    suma_total = 0
    for valor in valores:
        suma_total  += valor
    porcentajes = []

    for valor in valores:
        porcentaje = (valor / suma_total) * 100
        porcentajes.append(porcentaje)
        

    return porcentajes


#print(porcentaje_barras([50, 35, 47, 66]))
