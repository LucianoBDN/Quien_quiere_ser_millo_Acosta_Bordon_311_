import pygame

def escribir_texto(ventana, texto, fuente, color_texto, x, y):

    txt = fuente.render(texto, True, color_texto)

    ventana.blit(txt,(x,y))


def escribir_pregunta(ventana, texto, fuente, color_texto, x, y):

    txt = fuente.render(texto, True, color_texto)

    ventana.blit(txt,(x,y))

def renderizar_texto(ventana, fuente, texto, x, y, ancho_max):
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

def mostrar_respuestas(ventana, fuente, lista_respuestas, x, y):
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
