import pygame


def agregar_img_a_escena(ventana, DIMENSIONES: tuple, path_imagen: str, posicion: tuple[int,int] ):

    superficie = pygame.image.load(path_imagen)
    superficie_escalado = pygame.transform.scale(superficie,(DIMENSIONES))
    superficie_rectangulo = superficie_escalado.get_rect(topleft=posicion)
    ventana.blit(superficie_escalado, posicion)

    return ventana


def cambiar_status_presentador(ventana, dimension_reescalado: tuple, path: str, posicion: tuple[int,int]):

    presentador_img_sin_escalar = pygame.image.load(path).convert_alpha()
    presentador_img_reescalada = pygame.transform.scale(presentador_img_sin_escalar,dimension_reescalado)
    presentador_img_reescalada = pygame.transform.flip(presentador_img_reescalada, True, False)

    ventana.blit(presentador_img_reescalada, posicion)

    return ventana

