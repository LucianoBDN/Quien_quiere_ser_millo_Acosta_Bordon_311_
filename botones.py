import pygame

class Boton:
    def __init__(self, x, y, ancho, alto, color_normal, color_hover, color_click, texto, fuente):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.color_normal = color_normal
        self.color_hover = color_hover
        self.color_click = color_click
        self.texto = texto
        self.fuente = fuente
        self.color_actual = self.color_normal
        self.click = False

    def dibujar(self, pantalla, color_texto):
        pygame.draw.rect(pantalla, self.color_actual, self.rect)
        texto_superficie = self.fuente.render(self.texto, True, color_texto)
        pantalla.blit(texto_superficie, (
            self.rect.x + (self.rect.width - texto_superficie.get_width()) // 2,
            self.rect.y + (self.rect.height - texto_superficie.get_height()) // 2))

    def manejar_evento(self, evento):
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

    def agregar_imgagen_boton(self, ventana, path, ancho, alto, x,y):
       
        boton_superficie = pygame.image.load(path).convert_alpha()
        boton_superficie = pygame.transform.scale(boton_superficie, (ancho, alto))
        self.rect = boton_superficie.get_rect(topleft= (x,y))
        ventana.blit(boton_superficie, (x,y))


    def es_click(self):
        return self.click