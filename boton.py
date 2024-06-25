import pygame

def pintar_boton(ventana, boton, color_boton_estatico, color_boton_seleccionado, texto_boton, color_texto, fuente):

    if boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(ventana, color_boton_seleccionado, boton, 0)
    else:
        pygame.draw.rect(ventana, color_boton_estatico, boton, 0)

    texto = fuente.render(texto_boton, True, color_texto)

    ventana.blit(texto, (boton.x + (boton.width-texto.get_width())/2, boton.y + (boton.height-texto.get_height())/2))