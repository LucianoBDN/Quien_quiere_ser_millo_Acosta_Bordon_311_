import pygame

class Presentador:
    
    def __init__(self, imagen_path, posicion):
        self.imagen = pygame.image.load(imagen_path).convert_alpha()
        self.rect = self.imagen.get_rect(center=posicion)
        self.posicion = posicion

    def dibujar(self, ventana):          
        ventana.blit(self.imagen, self.rect)

    def voltear_imagen(self, posicion):
        self.imagen = pygame.transform.flip(self.imagen, True, False)
        self.rect = self.imagen.get_rect(center=posicion)
        
    def escalar_imagen(self, posicion, ancho, alto):

        self.imagen = pygame.transform.scale(self.imagen, (ancho,alto))
        self.rect = self.imagen.get_rect(center=posicion)