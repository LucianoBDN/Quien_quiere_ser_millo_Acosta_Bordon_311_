import random


def nivel_pregunta(monto_jugador: int, lista_preguntas):

    pregunta_seleccionada = seleccionar_pregunta(lista_preguntas)

    while pregunta_seleccionada['monto_premio'] != monto_jugador:
         pregunta_seleccionada = seleccionar_pregunta(lista_preguntas)
            
    return pregunta_seleccionada

def seleccionar_pregunta(lista_preguntas: list):

    buscar_pregunta_por_id = random.randint(1, 25)

    for pregunta in lista_preguntas:
        if pregunta['id'] == buscar_pregunta_por_id:
            return pregunta['pregunta']
        


