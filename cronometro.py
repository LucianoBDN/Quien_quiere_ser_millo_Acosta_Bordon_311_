import pygame

class Cronometro:
    def __init__(self, duracion_tiempo: int):
        """Inicializa la clase cronometro con sus atributos base

        Args:
            duracion_tiempo (int): cuánto durará el cronometro
        """
        self.duracion_tiempo = duracion_tiempo
        self.tiempo_final = 0
        self.tiempo_restante = duracion_tiempo
        self.iniciado = False

    def iniciar(self):
        """Inicia el cronometro
        """
        self.tiempo_final = pygame.time.get_ticks() / 1000 + self.duracion_tiempo
        self.iniciado = True

    def actualizar(self):
        """Actualiza en tiempo real cuántos segundos van del cronometro

        Returns:
            self.tiempo_restante (int): el tiempo que queda
        """
        
        if self.iniciado:
            tiempo_actual = pygame.time.get_ticks() / 1000
            self.tiempo_restante = int(self.tiempo_final - tiempo_actual)
            if self.tiempo_restante <= 0:
                self.tiempo_restante = 0
                self.iniciado = False
        
        return self.tiempo_restante
    
    def reiniciar(self):
        """Reinicia el cronometro
        """
        self.tiempo_final = 0
        self.tiempo_restante = self.duracion_tiempo
        self.iniciado = False
        