import pygame


def agregar_img_a_escena(ventana, DIMENSIONES: tuple, path_imagen: str, posicion: tuple[int,int] ):
    """Agrega una imagen a la pantalla

    Args:
        ventana (surface): pantalla donde se agregará la imagen
        DIMENSIONES (tuple): dimensiones de la imagen que se agrega
        path_imagen (str): ruta de la imagen
        posicion (tuple[int,int]): posición donde se agregará la imagen

    Returns:
        ventana (surface): la pantalla con la imagen agregada 
    """

    superficie = pygame.image.load(path_imagen)
    superficie_escalado = pygame.transform.scale(superficie,(DIMENSIONES))
    superficie_rectangulo = superficie_escalado.get_rect(topleft=posicion)
    ventana.blit(superficie_escalado, posicion)

    return ventana


def cambiar_status_presentador(ventana, dimension_reescalado: tuple, path: str, posicion: tuple[int,int]):
    """Agrega una imagen del presentador según su estado

    Args:
        ventana (surface): pantalla dónde se muestra
        dimension_reescalado (tuple): dimensión que le queremos dar a la imagen
        path (str): ruta de la imagen del presentador
        posicion (tuple[int,int]): posición donde estará la imagen

    Returns:
        ventana (surface): pantalla con el presentador ubicado
    """
    presentador_img_sin_escalar = pygame.image.load(path).convert_alpha()
    presentador_img_reescalada = pygame.transform.scale(presentador_img_sin_escalar,dimension_reescalado)
    presentador_img_reescalada = pygame.transform.flip(presentador_img_reescalada, True, False)

    ventana.blit(presentador_img_reescalada, posicion)

    return ventana

