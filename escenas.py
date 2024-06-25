import pygame


def cambiar_escena_jugar(ventana, DIMENSIONES: tuple, path_escena: str):

    fondo_superficie = pygame.image.load(path_escena)
    fondo_superficie_escalado = pygame.transform.scale(fondo_superficie,(DIMENSIONES))
    
    ventana.blit(fondo_superficie_escalado,(0,0))

    return ventana


def cambiar_status_presentador(ventana, dimension_reescalado: tuple, path: str, posicion: tuple):

    presentador_img_sin_escalar = pygame.image.load(path).convert_alpha()
    presentador_img_reescalada = pygame.transform.scale(presentador_img_sin_escalar,dimension_reescalado)

    ventana.blit(presentador_img_reescalada, posicion)

    return ventana



