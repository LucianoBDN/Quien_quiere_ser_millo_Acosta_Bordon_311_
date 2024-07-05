import pygame


def setear_ventana(titulo, path_icono, ancho_ventana, alto_ventana):

    DIMENSION_VENTANA = (ancho_ventana, alto_ventana)

    ventana = pygame.display.set_mode((DIMENSION_VENTANA))
    pygame.display.set_caption(titulo)
    icono = pygame.image.load(path_icono)
    pygame.display.set_icon(icono)

    return ventana