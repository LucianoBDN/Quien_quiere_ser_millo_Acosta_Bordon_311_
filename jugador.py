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
    

    def aumentar_nivel_y_monto(self):

        self.nivel += 1

        match (self.nivel):
            
            case 1: self.score = 100
            case 2: self.score = 200
            case 3: self.score = 300
            case 4: self.score = 500
            case 5: self.score = 1000
            case 6: self.score = 2000
            case 7: self.score = 4000
            case 8: self.score = 8000
            case 9: self.score = 16000
            case 10: self.score = 32000
            case 11: self.score = 64000
            case 12: self.score = 125000
            case 13: self.score = 250000
            case 14: self.score = 500000
            case 15: self.score = 1000000

    



    