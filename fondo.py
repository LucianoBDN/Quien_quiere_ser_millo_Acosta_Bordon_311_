import pygame

class Fondo:

    def __init__(self, imagen_path, dimension):
        self.imagen = pygame.image.load(imagen_path).convert_alpha()
        self.imagen_escalada = pygame.transform.scale(self.imagen, dimension)

    def dibujar_fondo(self, ventana, posicion):
        ventana.blit(self.imagen_escalada, posicion)