import pygame

class Boton:
    def __init__(self, ventana, x, y, ancho, alto, color_normal, color_hover, color_click, texto, fuente):
        self.ventana = ventana
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
        print(self.switch_rojo)

    def dibujar(self, color_texto):
        pygame.draw.rect(self.ventana, self.color_actual, self.rect)
        texto_superficie = self.fuente.render(self.texto, True, color_texto)
        self.ventana.blit(texto_superficie, (
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

    def agregar_imagen_boton(self, path, ancho, alto, x,y):
       
        boton_superficie = pygame.image.load(path).convert_alpha()
        boton_superficie = pygame.transform.scale(boton_superficie, (ancho, alto))
        self.rect = boton_superficie.get_rect(topleft= (x,y))
        self.ventana.blit(boton_superficie, (x,y))

    def escribir_sobre_imagen(self, color_texto):

        texto_superficie = self.fuente.render(self.texto, True, color_texto)
        self.ventana.blit(texto_superficie, (
            self.rect.x + (self.rect.width - texto_superficie.get_width()) // 2, #ALINEA EL TEXTO EN EJE HORIZONTAL
            self.rect.y + (self.rect.height - texto_superficie.get_height()) // 2)) #ALINEA EL TEXTO EN EJE VERTICAL      

    def es_click(self):
        return self.click
    
    def manejar_boton(self, switch_boton: bool, path_imagen):
            
            if switch_boton:

                self.agregar_imagen_boton(path_imagen, self.rect.width, self.rect.height, self.rect.x, self.rect.y)

                self.escribir_sobre_imagen((0,0,0))

    
    def manejar_switch_boton(self, evento, respuesta):
                      
        if self.texto == respuesta:                    
            self.switch_default = not self.switch_default
            self.switch_verde = not self.switch_verde
            print("COOORRECTOOOOOOO")
                
        else:                               
            self.switch_default = not self.switch_default
            self.switch_rojo = not self.switch_rojo
            print("BURROOOOOOOO")

    # def manejar_switch_boton2(self, evento, respuesta):
                      
    #     if self.texto == respuesta:                    
    #         self.switch_default = not self.switch_default
    #         self.switch_verde = not self.switch_verde
    #         print("COOORRECTOOOOOOO")
                
    #     else:                               
    #         self.switch_default = not self.switch_default
    #         self.switch_rojo = not self.switch_rojo
    #         print("BURROOOOOOOO")