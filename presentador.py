import pygame

class Presentador:
    
    def __init__(self, imagen_path:str, posicion: tuple[int, int]):
        """Inicializa solicitando ruta de imagen y posicion de donde colocar

        Args:
            imagen_path (str): URL
            posicion (tuple): [int,int]
        """
        self.imagen = pygame.image.load(imagen_path).convert_alpha()
        self.rect = self.imagen.get_rect(center=posicion)
        self.posicion = posicion

    def dibujar(self, ventana):
        """Coloca la imagen sobre la superficie que se le asigna como argumento
        """          
        ventana.blit(self.imagen, self.rect)

    def voltear_imagen(self, posicion: tuple[int, int]):
        """ voltea la imagen como espejo

        Args:
            posicion (tuple): coordenadas de eje x, y
        """
        self.imagen = pygame.transform.flip(self.imagen, True, False)
        self.rect = self.imagen.get_rect(center=posicion)
        
    def escalar_imagen(self, posicion:tuple, ancho:int, alto:int):
        """Reescala la imagen con nuevo tamaño

        Args:
            posicion (tupla): coordenadas de eje x, y
            ancho (_int): ancho de imagen
            alto (int): alto de imagen
        """

        self.imagen = pygame.transform.scale(self.imagen, (ancho,alto))
        self.rect = self.imagen.get_rect(center=posicion)
  
    def cambiar_imagen(self, imagen_path: str, ventana, posicion: tuple, ancho: int, alto: int):
        """Cambia la imagen asignada al iniciar la clase y la reemplaza por otra ubicada en el url que se le pasa
        como argumento

        Args:
            imagen_path (str): URL imagen
            ventana (surface): ventana
            posicion (tuple): coordenadas en eje x, y 
            ancho (int): ancho de imagen
            alto (int): alto de imagen
        """

        self.imagen = pygame.image.load(imagen_path).convert_alpha()
        self.escalar_imagen(posicion, ancho, alto)
        self.dibujar(ventana)