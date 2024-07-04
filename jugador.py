import pygame
from texto import *
class Jugador:
    def __init__(self):
        self.nombre = ""
        self.score = None
        self.vidas = 1
        self.nivel = 1
    

    def input_jugador(self,evento,ventana, color, fuente,color_texto, texto:str):
        
        input_rect = pygame.Rect(70,70,200,70)
        
        bandera_escribir = True

       
        if evento.type == pygame.KEYDOWN:
            if bandera_escribir:
                if evento.key == pygame.K_BACKSPACE:
                    texto = texto[:-1]   
                elif evento.key == pygame.K_RETURN:
                    self.nombre = texto
                else:
                    texto += evento.unicode
                    

        pygame.draw.rect(ventana, color, input_rect, 2)
        texto_superficie = fuente.render(texto, True, color_texto)
        ventana.blit(texto_superficie, (input_rect.x +5, input_rect.y +10))
              
        return texto
    

    def aumentar_nivel(self, boton, respuesta):

        if boton.texto == respuesta:                    
            boton.switch_default = False
            boton.switch_verde = True
            self.nivel += 1
            print("COOORRECTOOOOOOO")
            respuesta_correcta = True
                
        else:                               
            boton.switch_default = False
            boton.switch_rojo = True
            self.vidas = 0
            print("BURROOOOOOOO")
            respuesta_correcta = False

        return respuesta_correcta

    



    