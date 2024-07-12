import pygame
from texto import *



def dibujar_barras(ventana, color:tuple[int, int, int], x: int, y: int, width: int, height: int):
    """dibuja rectangulos utilizando el metodo pygame.draw.rect
    

    Args:
        ventana (surface): superficie donde se dibujara
        color (tuple[int, int, int]): colores con valor RGB
        x (int): posicion en pantalla sobre el eje x
        y (int): posicion en patalla sobre el eje y
        width (int): ancho de los rentangulos
        height (int): alto de los rectangulos

    Returns:
        _type_: _description_
    """

    y -= height
    rectangulo = pygame.draw.rect(ventana, color, (x, y, width, height))

    
    return rectangulo



def porcentaje_barras(valores:list):
    """Recibe una lista de numeros, los suma y normaliza
    el resultado a una division para que cada numero tenga el
    porcentaje de lo que ocupa en esa sumatoria total

    Args:
        valores (list): numeros

    Returns:
        list: lista de porcentajes
    """

    suma_total = 0
    for valor in valores:
        suma_total  += valor
    porcentajes = []

    for valor in valores:
        porcentaje = (valor / suma_total) * 100
        porcentajes.append(porcentaje)
        

    return porcentajes




def reiniciar_switches(switches:dict):
    """devuelve los swuitches a su su estado inicial

    Args:
        switches (dict): diccionario con banderas

    Returns:
        dict: diccionario con banderas
    """

    switches['bucle_principal'] = True
    switches['menu_principal'] = True
    switches['jugando'] = False
    switches['pausa'] = False
    switches['comodin_publico'] = False
    switches['cincuenta_cincuenta'] = False
    switches['comodin_llamada'] = False
    switches['resultado_respuesta'] = None
    switches['pantalla_score'] = False
    switches['retirarse'] = False
    switches['escribir'] = True
    
    return switches


def cargar_sonidos(path_musica: str, path_correcto: str, path_perdiste: str):
    """carga los sonidos que utilizamos en el juego

    Args:
        path_musica (str): _description_
        path_correcto (str): _description_
        path_perdiste (str): _description_

    Returns:
        _type_: _description_
    """


    musica_fondo = pygame.mixer.music.load(path_musica)
    sonido_respuesta_mal = pygame.mixer.Sound(path_perdiste)
    sonido_respuesta_bien = pygame.mixer.Sound(path_correcto)
    sonido_respuesta_bien.set_volume(0.2)
    pygame.mixer.music.play(-1)
    pygame.mixer_music.set_volume(0.2)

    return sonido_respuesta_mal, sonido_respuesta_bien