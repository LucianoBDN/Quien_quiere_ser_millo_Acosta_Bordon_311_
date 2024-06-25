import pygame

def escribir_texto(ventana, texto, fuente, color_texto, x, y):

    txt = fuente.render(texto, True, color_texto)
    ventana.blit(txt,(x,y))