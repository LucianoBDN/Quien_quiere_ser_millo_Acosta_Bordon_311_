import pygame

class Imagen:

    def __init__(self, imagen_path: str, dimension: tuple[int,int], posicion: tuple[int,int]):
        """Inicia la clase imagen con sus atributos

        Args:
            self.imagen_path (str): ruta de la imagen
            self.dimension (tuple): dimensiones de la imagen que le asignamos a la imagen
            self.posicion (tuple): posición a colocar la imagen
        """
        self.imagen = pygame.image.load(imagen_path).convert_alpha()
        self.imagen_escalada = pygame.transform.scale(self.imagen, dimension)
        self.rectangulo = self.imagen_escalada.get_rect(center = posicion)

    def dibujar_imagen(self, ventana,):
        """Muestra el banco en pantalla

        Args:
            ventana (surface): pantalla en la cuál muestro el banco
        """
        ventana.blit(self.imagen_escalada, self.rectangulo)

    def escribir_imagen(self, ventana,fuente, texto, color_texto):
        """permite escribir un texto sobre a imagen, centra el texto y lo muestra en pantalla

        Args:
            ventana (surface): pantalla
            fuente (str): tipo de letra
            texto (str): texto que va sobre la imagen
            color_texto (tupla): color del texto
        """
        
        texto_superficie = fuente.render(texto, True, color_texto)
        ventana.blit(texto_superficie, (
            self.rectangulo.x + (self.rectangulo.width - texto_superficie.get_width()) // 2, #ALINEA EL TEXTO EN EJE HORIZONTAL
            self.rectangulo.y + (self.rectangulo.height - texto_superficie.get_height()) // 2)) #ALINEA EL TEXTO EN EJE VERTICAL      
    
