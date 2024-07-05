import pygame

def escribir_texto(ventana, texto: str, fuente: str, color_texto: tuple, x: int, y: int):
    """Escribe texto en pantalla

    Args:
        ventana (surface): pantalla en la que escribimos
        texto (str): texto que deseamos escribir
        fuente (str): fuente para el texto
        color_texto (tuple): color asignado al texto
        x (int): ubicación en eje x del texto
        y (int): ubicación en eje y del texto
    """

    txt = fuente.render(texto, True, color_texto)

    ventana.blit(txt,(x,y))


def renderizar_texto(ventana, fuente: str, texto: str, x: int, y: int, ancho_max: int):
    """Se encarga de recortar el texto en distintas lineas para que no supere el ancho máximo, y luego lo muestra en pantalla

    Args:
        ventana (surface): pantalla donde muestra el texto 
        fuente (str): fuente para el texto
        texto (str): texto que deseamos mostrar
        x (int): ubicación del texto en eje x
        y (int): ubicación del texto en eje y
        ancho_max (int): ancho máximo a respetar por el texto
    """
    palabras = texto.split(' ')
    lineas = []
    linea_actual = ""

    for palabra in palabras:
        if fuente.size(linea_actual + palabra)[0] < ancho_max:
            linea_actual += palabra + " "
        else:
            lineas.append(linea_actual.strip())
            linea_actual = palabra + " "

    lineas.append(linea_actual.strip())

    for i, linea in enumerate(lineas):
        texto_renderizado = fuente.render(linea, True, (0, 0, 0))
        ventana.blit(texto_renderizado, (x, y + i * fuente.get_linesize()))

def mostrar_respuestas(ventana, fuente: str, lista_respuestas: list[dict], x: int, y: int):
    """Muestra las posibles respuestas

    Args:
        ventana (surface): pantalla donde se mostrarán las respuestas
        fuente (str): fuente de las respuestas
        lista_respuestas (list): lista donde se encuentran las posibles respuestas
        x (int): posición en eje x para mostrar las respuestas
        y (int): posición en eje y para mostrar las respuestas
    """
    ancho_max = 400

    auxiliar = x
    for respuesta in lista_respuestas[:2]:
        renderizar_texto(ventana, fuente, respuesta, x, y, ancho_max)
        texto_temp = fuente.render(respuesta, True, (0, 0, 0))
        #rectangulo_texto = texto_temp.get_rect()
        x += 500

    y += 160
    x = auxiliar

    for respuesta in lista_respuestas[(len(lista_respuestas)//2):]:
        renderizar_texto(ventana, fuente, respuesta, x, y, ancho_max)
        texto_temp = fuente.render(respuesta, True, (0, 0, 0))
        #rectangulo_texto = texto_temp.get_rect()
        x += 500
