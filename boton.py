import pygame

def pintar_boton(ventana, boton, texto_boton, fuente):

    if boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(ventana, (18,79,134), boton, 0)
    else:
        pygame.draw.rect(ventana, (28,99,162), boton, 0)
    
    texto = fuente.render(texto_boton, True, (255,255,255))
    
    ventana.blit(texto, (boton.x + (boton.width-texto.get_width())/2, boton.y + (boton.height-texto.get_height())/2))