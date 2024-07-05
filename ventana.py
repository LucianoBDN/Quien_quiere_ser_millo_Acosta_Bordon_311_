import pygame


def setear_ventana(titulo, path_icono: str, ancho_ventana: int, alto_ventana: int):
    """Inicializa la ventana con todas sus características

    Args:
        self.titulo (str): titulo de la ventana
        self.path_icono (str): ruta del icono de la ventana
        self.ancho_ventana (int): ancho de la ventana
        self.alto_ventana (int): alto de la ventana

    Returns:
        ventana (surface): devuelve la ventana ya armada
    """
    DIMENSION_VENTANA = (ancho_ventana, alto_ventana)

    ventana = pygame.display.set_mode((DIMENSION_VENTANA))
    pygame.display.set_caption(titulo)
    icono = pygame.image.load(path_icono)
    pygame.display.set_icon(icono)

    return ventana