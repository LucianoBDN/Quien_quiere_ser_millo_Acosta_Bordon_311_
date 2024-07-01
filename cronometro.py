import pygame

class Cronometro:
    def __init__(self, duracion_tiempo):
        self.duracion_tiempo = duracion_tiempo
        self.tiempo_final = 0
        self.tiempo_restante = duracion_tiempo
        self.iniciado = False

    def iniciar(self):
        self.tiempo_final = pygame.time.get_ticks() / 1000 + self.duracion_tiempo
        self.iniciado = True

    def actualizar(self):
        
        if self.iniciado:
            tiempo_actual = pygame.time.get_ticks() / 1000
            self.tiempo_restante = int(self.tiempo_final - tiempo_actual)
            if self.tiempo_restante <= 0:
                self.tiempo_restante = 0
                self.iniciado = False
        
        return self.tiempo_restante