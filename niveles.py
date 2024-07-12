import random
from texto import *


def seleccionar_pregunta(nivel_jugador: int, preguntas: list[dict]) -> dict:
    """generera numeros ramdon de preguntas para compararlas con el id 
    y valida qe el nivel de la pregunta random sea el mismo que el nivel del jugador
    si no es asi selecciona otro id de pregunta hasta que se cumpla el requisito

    Args:
        nivel_jugador (int): _description_
        preguntas (list[dict]): _description_

    Returns:
        dict: retorna el diccionario de la pregunta
    """

    nivel_pregunta_random = 0
    
    while nivel_pregunta_random != nivel_jugador:
    
        id_pregunta_random = random.randint(1, 75)

        for pregunta in preguntas:

            if id_pregunta_random == pregunta['id']:

                nivel_pregunta_random = pregunta['nivel']

                pregunta_final = pregunta

    return pregunta_final


def manejar_niveles(boton, pregunta, diccionario_switches, sonido_respuesta_mal, sonido_respuesta_bien) -> bool:
    """comprueba si el texto de la respuesta es igual texto que recibe el boton
    si lo es cambia el switch_verde a True y switch_default a False
    si no cambia el switch_rojo a True y switch_default a False

    Args:
        boton (_type_): elemento CLASS
        respuesta (str): texto 

    Returns:
        bool: True o False
    """

    if boton.texto == pregunta.respuesta_correcta:                
        boton.switch_default = False
        boton.switch_verde = True
        sonido_respuesta_bien.play()
        diccionario_switches['resultado_respuesta'] = True
        diccionario_switches['pausa'] = True
       
    else:                               
        boton.switch_default = False
        boton.switch_rojo = True
        sonido_respuesta_mal.play()
        diccionario_switches['resultado_respuesta'] = False
        diccionario_switches['jugando'] = False
       


    return diccionario_switches
