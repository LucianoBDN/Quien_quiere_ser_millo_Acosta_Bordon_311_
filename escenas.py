import pygame


def agregar_img_a_escena(ventana, DIMENSIONES: tuple, path_escena: str, posicion: tuple[int,int] ):

    fondo_superficie = pygame.image.load(path_escena)
    fondo_superficie_escalado = pygame.transform.scale(fondo_superficie,(DIMENSIONES))
    
    ventana.blit(fondo_superficie_escalado, posicion)

    return ventana


def cambiar_status_presentador(ventana, dimension_reescalado: tuple, path: str, posicion: tuple[int,int]):

    presentador_img_sin_escalar = pygame.image.load(path).convert_alpha()
    presentador_img_reescalada = pygame.transform.scale(presentador_img_sin_escalar,dimension_reescalado)
    presentador_img_reescalada = pygame.transform.flip(presentador_img_reescalada, True, False)

    ventana.blit(presentador_img_reescalada, posicion)

    return ventana



