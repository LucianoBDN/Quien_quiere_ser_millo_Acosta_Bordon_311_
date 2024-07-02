import pygame

class Banco:

    def __init__(self, imagen_path, dimension, posicion):
        self.imagen = pygame.image.load(imagen_path).convert_alpha()
        self.imagen_escalada = pygame.transform.scale(self.imagen, dimension)
        self.rectangulo = self.imagen_escalada.get_rect(center = posicion)

    def dibujar_banco(self, ventana):
        ventana.blit(self.imagen_escalada, self.rectangulo)
