import pygame
import random
from texto import *
from generales import *

class Comodin:
    def __init__(self, nombre) -> None:
        """Inicializa el comodin con sus atributos
        """
        self.nombre = nombre
        self.alturas = []
        self.usos = 1
        self.comodin_activo = False 
    
    def reiniciar_comodines(self):
        """Restablece los usos del comodín
        """
        self.usos = 1
        self.comodin_activo = False
    
    def generar_lista_alturas(self):
        """genera numeros aleatorios los cuales se van a utilizar
        para graficar rectangulos con distintas alturas
        el for itera cuatro veces y agrega a lista aturas la altura que se genero
        en cada vuelta

        Returns:
            list: lista de alturas
        """

        lista_alturas = []

        for i in range(4):
            altura = random.randint(30,100)
            lista_alturas.append(altura)

        self.alturas = lista_alturas
        

    def mostrar_barras(self, ventana, color: tuple, x: int, y: int, width: int, fuente: int, color_txt: tuple):
        """Muestra el grafico del comodin del publico

        Args:
            ventana (surface): pantalla en la que se mostrará el grafico
            color (tuple): color de las barras
            x (int): posición en eje x de las barras
            y (int): posición en eje y de las barras
            width (int): ancho de las barras
            fuente (str): fuente del texto para el grafico
            color_txt (tuple): color para el texto
            height (int): altura de las barras
        """

        opciones = ["A", "B", "C", "D"]

        x_texto = x +18
        y_texto = y -20

        

        x_porcentaje = x + 18
        y_porcentaje = y - 40
        vuelta = 0

        for i in range(len(self.alturas)):
            dibujar_barras(ventana, color, x, y, width, self.alturas[i])
            escribir_texto(ventana, opciones[i] ,fuente, color_txt, x_texto, y_texto)
            vuelta += 1
            x_texto += 60
            x += 60

        lista_alturas_barras = porcentaje_barras(self.alturas)

        for porcentaje in lista_alturas_barras:
            porcentaje = str(porcentaje)
            escribir_texto(ventana, f"{porcentaje[:4]}%" ,fuente, color_txt, x_porcentaje, y_porcentaje)
            x_porcentaje += 55

        self.comodin_activo = True
        self.usos = 0
        
    def palabra_clave(self, ventana, pista: str, fuente: str, color_texto: tuple, x: int, y: int):
        """Otorga una pista en forma de palabra clave al jugador

        Args:
            ventana (surface): pantalla donde se mostrará la pista
            pista (str): palabra clave en relación a la respuesta correcta
            fuente (str): fuente que usará la pista
            color_texto (tuple): color asignado al texto
            x (int): posición en eje x de la pista
            y (int): posición en eje y de la pista
        """
        pista = "Pista: " + pista

        escribir_texto(ventana, pista , fuente, color_texto, x, y)

        self.comodin_activo = True
        self.usos = 0

    
    def comodin_cincuenta(self,lista_respuestas: list, respuesta_correcta: str) :
        """Borra 2 opciones posibles de las respuestas para que el jugado solo tenga que elegir entre 2

        Args:
            lista_respuestas (list): las 4 posibles respuestas
            respuesta_correcta (str): la respuesta que es correcta 

        Returns:
            lista_dos_respuesta (list): lista que solo contiene 2 respuestas posibles
        """
        lista_dos_respuesta = []

        lista_dos_respuesta.append(respuesta_correcta)

        for respuesta in lista_respuestas:
            if respuesta != respuesta_correcta:
                if len(lista_dos_respuesta) < 2:
                    lista_dos_respuesta.append(respuesta)
                else:
                    respuesta = "----------------"
                    lista_dos_respuesta.append(respuesta)
        
        self.comodin_activo = True
        self.usos = 0

        return lista_dos_respuesta