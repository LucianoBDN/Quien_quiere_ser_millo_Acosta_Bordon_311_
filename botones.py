import pygame

class Boton:
    def __init__(self, ventana, nombre: str, x: int, y: int, ancho: int, alto: int, color_normal: tuple, color_hover: tuple, color_click: tuple, texto: str, fuente: str):
        """Inicializa la clase boton con sus atributos

        Args:         
            self.ventana (surface): pantalla en la que vamos a mostrar el botón
            self.nombre (str): nombre del botón
            self.x (int): posicion x para la ubicación del boton
            self.y (int): posicion y para la ubicación del boton
            self.ancho (int): valor para el ancho del botón
            self.alto (int): valor para el alto del botón
            self.color_normal (tuple): color default del botón
            self.color_hover (tuple): color del botón al pasar el mouse por arriba
            self.color_click (tuple): color del botón al clickearlo
            self.texto (str): texto que lleva dentro el botón
            self.fuente (str): fuente que utilizará el texto
        """
        self.ventana = ventana
        self.nombre = nombre
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.color_click = color_click
        self.texto = texto
        self.fuente = fuente
        self.color_actual = self.color_normal
        self.click = False
        self.switch_default = True
        self.switch_verde = False
        self.switch_rojo = False


    def dibujar(self, color_texto):
        """Muestra al botón en pantalla

        Args:
            color_texto (tuple): color del texto del botón
        """
        pygame.draw.rect(self.ventana, self.color_actual, self.rect)
        texto_superficie = self.fuente.render(self.texto, True, color_texto)
        self.ventana.blit(texto_superficie, (
            self.rect.x + (self.rect.width - texto_superficie.get_width()) // 2,
            self.rect.y + (self.rect.height - texto_superficie.get_height()) // 2))

    def manejar_evento(self, lista_eventos:list):
        """Se encarga de cambiar los colores del botón según la posición del mouse

        Args:
            evento (event): evento que ocurre al realizar determinada acción
        """
        for evento in lista_eventos:
            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if self.rect.collidepoint(evento.pos):
                    self.color_actual = self.color_click
                    self.click = True
            elif evento.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(evento.pos):
                    self.click = False
            elif evento.type == pygame.MOUSEMOTION:
                if self.rect.collidepoint(evento.pos):
                    self.color_actual = self.color_hover
                else:
                    self.color_actual = self.color_normal

    def agregar_imagen_boton(self, path: str, ancho: int, alto: int, x: int, y: int):
        """Le agrega una imagen al botón

        Args:
            path (str): ruta de ubicación de la imagen
            ancho (int): ancho que le queremos dar a la imagen
            alto (int): alto que le queremos dar a la imagen
            x (int): posición en eje x para ubicar a la imagen
            y (int): posición en eje y para ubicar a la imagen
        """
       
        boton_superficie = pygame.image.load(path).convert_alpha()
        boton_superficie = pygame.transform.scale(boton_superficie, (ancho, alto))
        self.rect = boton_superficie.get_rect(topleft= (x,y))
        self.ventana.blit(boton_superficie, (x,y))

    def escribir_sobre_imagen(self, texto, color_texto: tuple):
        """Le agrega texto dentro del botón que tenga una imagen

        Args:
            color_texto (tuple): color del texto para el botón 
        """

        texto_superficie = self.fuente.render(texto, True, color_texto)
        self.ventana.blit(texto_superficie, (
            self.rect.x + (self.rect.width - texto_superficie.get_width()) // 2, #ALINEA EL TEXTO EN EJE HORIZONTAL
            self.rect.y + (self.rect.height - texto_superficie.get_height()) // 2)) #ALINEA EL TEXTO EN EJE VERTICAL      
    
    def manejar_boton(self, switch_boton: bool, path_imagen: str):
        """Pinta el botón de determinado color según el estado del interruptor

        Args:
            switch_boton (bool): interruptor 
            path_imagen (str): ruta de la imagen que mostrará
        """
        if switch_boton:

            self.agregar_imagen_boton(path_imagen, self.rect.width, self.rect.height, self.rect.x, self.rect.y)

            self.escribir_sobre_imagen((0,0,0))

    
    def reiniciar_switches(self):
        """Restablece todos los interruptores del botón a su estado por defecto cuando se inicializan
        """
                      
        self.switch_default = True
        self.switch_rojo = False
        self.switch_verde = False