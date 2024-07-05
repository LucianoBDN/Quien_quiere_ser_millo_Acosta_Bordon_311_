import pygame

class Banco:

    def __init__(self, imagen_path: str, dimension: tuple[int,int], posicion: tuple[int,int]):
        """Inicia la clase banco con sus atributos

        Args:
            self.imagen_path (str): ruta de la imagen
            self.dimension (tuple): dimensiones de la imagen que le asignamos a la imagen
            self.posicion (tuple): posición a colocar la imagen
        """
        self.imagen = pygame.image.load(imagen_path).convert_alpha()
        self.imagen_escalada = pygame.transform.scale(self.imagen, dimension)
        self.rectangulo = self.imagen_escalada.get_rect(center = posicion)

    def dibujar_banco(self, ventana):
        """Muestra el banco en pantalla

        Args:
            ventana (surface): pantalla en la cuál muestro el banco
        """
        ventana.blit(self.imagen_escalada, self.rectangulo)
