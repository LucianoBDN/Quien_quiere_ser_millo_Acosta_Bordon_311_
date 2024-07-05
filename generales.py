import pygame
import random
from texto import *

# Definir la función comodin_publico_barras

def generar_lista_alturas():

    lista_alturas = []

    for i in range(4):
        height = random.randint(30,100)
        lista_alturas.append(height)

    return lista_alturas



def dibujar_barras(ventana, color, x, y, width, height):

    y -= height
    rectangulo = pygame.draw.rect(ventana, color, (x, y, width, height))

    
    return rectangulo



def porcentaje_barras(valores:list):

    suma_total = 0
    for valor in valores:
        suma_total  += valor
    porcentajes = []

    for valor in valores:
        porcentaje = (valor / suma_total) * 100
        porcentajes.append(porcentaje)
        

    return porcentajes



def crear_rectangulo(ventana,color, fuente, texto):

    input_rect = pygame.Rect(600,360,200,70)
    pygame.draw.rect(ventana, color, input_rect, 2)
    escribir_texto(ventana, texto,fuente,color,input_rect.x + 50 ,input_rect.y + 25)