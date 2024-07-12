from botones import Boton
import pygame
from comodin import Comodin


#Carga la lista con los botones necesarios del juego

cargar_botones = lambda ventana: [


    Boton(ventana, "boton_jugar", 560, 300, 150, 50, (28, 99, 162), (18, 79, 134), (18, 79, 134), "Jugar", pygame.font.SysFont("Arial", 30)),
    Boton(ventana, "boton_score", 560, 400, 150, 50, (28, 99, 162), (18, 79, 134), (18, 79, 134), "Highscore", pygame.font.SysFont("Arial", 30)),
    Boton(ventana, "boton_salir", 560, 500, 150, 50, (28, 99, 162), (18, 79, 134), (18, 79, 134), "Salir", pygame.font.SysFont("Arial", 30)),
    Boton(ventana, "boton_a", 5, 370, 550, 200, (18, 79, 134), (18, 79, 134), (18, 79, 134), "", pygame.font.SysFont("Arial", 20, bold=True)),
    Boton(ventana, "boton_b", 505, 370, 550, 200, (18, 79, 134), (18, 79, 134), (18, 79, 134), "", pygame.font.SysFont("Arial", 20, bold=True)),
    Boton(ventana, "boton_c", 5, 530, 550, 200, (18, 79, 134), (18, 79, 134), (18, 79, 134), "", pygame.font.SysFont("Arial", 20, bold=True)),
    Boton(ventana, "boton_d", 505, 530, 550, 200, (18, 79, 134), (18, 79, 134), (18, 79, 134), "", pygame.font.SysFont("Arial", 20, bold=True)),
    Boton(ventana, "boton_continuar", 870, 270, 150, 50, (28, 99, 162), (18, 79, 134), (18, 79, 134), "Continuar", pygame.font.SysFont("Arial", 18)),
    Boton(ventana, "boton_retirarse", 870, 330, 150, 50, (28, 99, 162), (18, 79, 134), (18, 79, 134), "Retirarse", pygame.font.SysFont("Arial", 18)),
    Boton(ventana, "boton_volver", 870, 500, 200, 50, (28, 99, 162), (18, 79, 134), (18, 79, 134), "Volver al menú principal", pygame.font.SysFont("Arial", 18)),
    Boton(ventana, "boton_publico", 1000, 100, 50, 50, (0, 0, 0), (0, 0, 0), (0, 0, 0), "", pygame.font.SysFont("Arial", 20, bold=True)),
    Boton(ventana, "boton_llamada", 1100, 100, 50, 50, (0, 0, 0), (0, 0, 0), (0, 0, 0), "", pygame.font.SysFont("Arial", 20, bold=True)),
    Boton(ventana, "boton_cincuenta", 1200, 100, 50, 50, (0, 0, 0), (0, 0, 0), (0, 0, 0), "", pygame.font.SysFont("Arial", 20, bold=True))
]


##Carga las banderas que utilizamos en el juego

cargar_switches = lambda: {
    'bucle_principal': True,
    'menu_principal': True,
    'jugando': False,
    'pausa': False,
    'comodin_publico': False,
    'cincuenta_cincuenta': False,
    'comodin_llamada': False,
    'resultado_respuesta': None,
    'pantalla_score': False,
    'retirarse': False,
    'escribir': True
}

## carga los comodines que usamos en el juego
cargar_comodines = lambda: [
    Comodin("comodin_publico"),
    Comodin("comodin_llamada"),
    Comodin("comodin_cincuenta")
]