import pygame
import random

# Definir la función comodin_publico_barras
def dibujar_barras(ventana, color, x, y, width):

    height = random.randint(30, 100)
    y -= height
    rectangulo = pygame.draw.rect(ventana, color, (x, y, width, height))

    return rectangulo


def mostrar_barras(ventana, color, x, y, width):

    for i in range(4):
    
        dibujar_barras(ventana, color, x, y, width)
        x += 100


# def comodin_llamada(preguntas: list, respuesta: str):

#     pregunta_comodin = []

#     for pregunta in preguntas:
#         if respuesta == pregunta:
#             pregunta_comodin.append(pregunta)
        
