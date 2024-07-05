import pygame

class Fondo:

    def __init__(self, imagen_path: str, dimension: tuple):
        """Inicializa la clase fondo con sus atributos

        Args:
            imagen_path (str): ruta de la imagen del fondo
            dimension (tuple): dimensiones para el fondo
        """
        self.imagen = pygame.image.load(imagen_path).convert_alpha()
        self.imagen_escalada = pygame.transform.scale(self.imagen, dimension)


    def dibujar_fondo(self, ventana, posicion: tuple):
        """Integra el fondo a la pantalla

        Args:
            ventana (surface): pantalla en la que pondremos el fondo
            posicion (tuple): ubicación para poner el fondo
        """
        ventana.blit(self.imagen_escalada, posicion)