import pygame
from texto import *

def pintar_boton(ventana, boton, color_boton_estatico, color_boton_seleccionado, texto_boton, color_texto, fuente):

    if boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(ventana, color_boton_seleccionado, boton, 0)
    else:
        pygame.draw.rect(ventana, color_boton_estatico, boton, 0)

    texto = fuente.render(texto_boton, True, color_texto)

    ventana.blit(texto, (boton.x + (boton.width-texto.get_width())/2, boton.y + (boton.height-texto.get_height())/2))

        # def manejar_evento(self,evento,ventana, color, fuente,color_texto, texto:str):
        
        # input_rect = pygame.Rect(600,360,200,70)
        
        # bandera_escribir = True

       
        # if evento.type == pygame.KEYDOWN:
            
        #     if bandera_escribir:
                
        #         if evento.key == pygame.K_BACKSPACE:
        #             texto = texto[:-1]   
        #         elif evento.key == pygame.K_RETURN:
        #             self.nombre = texto
        #             bandera_escribir = False
        #         else:
        #             texto += evento.unicode
                    


        # pygame.draw.rect(ventana, color, input_rect, 2)
        # escribir_texto(ventana, texto,fuente,color,input_rect.x + 50 ,input_rect.y + 25)
              
        # return texto