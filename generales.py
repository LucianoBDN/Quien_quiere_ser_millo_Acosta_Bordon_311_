import pygame
import random
from texto import *

# Definir la función comodin_publico_barras

# def generar_lista_alturas():
#     """genera numeros aleatorios los cuales se van a utilizar
#     para graficar rectangulos con distintas alturas
#     el for itera cuatro veces y agrega a lista aturas la altura que se genero
#     en cada vuelta

#     Returns:
#         list: lista de alturas
#     """

#     lista_alturas = []

#     for i in range(4):
#         height = random.randint(30,100)
#         lista_alturas.append(height)

#     return lista_alturas



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


# def actualizar_texto_respuestas(lista_botones, lista_respuestas):

        #  for boton in lista_botones:

        #      if boton.nombre == 'boton_a' or boton.nombre == 'boton_b' or boton.nombre == 'boton_c' or boton.nombre == 'boton_d':

        #          for respuesta in lista_respuestas:

        #              boton.texto = respuesta
