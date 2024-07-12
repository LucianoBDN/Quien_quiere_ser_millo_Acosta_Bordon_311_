def cargar_high_score(lista_puntuaciones:list):
    """inicializa la matriz con 5 filas y 2 columnas
    luego itera cargando en la matris los datos pasados de una lista
    y retorna la matriz cargada

    Args:
        lista_puntuaciones (list): lista de puntuaciones

    Returns:
        _type_: list[list]
    """

    matriz = [[0]* 2 for _ in range(5)] 

    filas = len(matriz)
    columnas = len(matriz[0])

    for i in range(filas):
        vuelta = 0

        for j in range(columnas):

            if vuelta == 0:
                matriz[i][j] = lista_puntuaciones[i][j]
            else:
                matriz[i][j] = lista_puntuaciones[i][j]
            vuelta +=1
        
    return matriz



def bubble_sort(lista:list[list]):
    """_summary_
    Ordena la matriz en funcion del segundo elemento de cada sublista
    Args:
        lista (list[list]): matriz a ordenar

    Returns:
        _type_: matriz ordenada por el segundo elemento de casa sublista
    """

    for i in range(len(lista)):
        for j in range(0, len(lista) -1):
            if lista[j][1] < lista[j+1][1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista



def cargar_csv_highscore(lista_highscore:list[list], path: str):
    """abre un archivo csv para escritura, completa la carga de todos los elementos de la lista
    y crea un archivo en un path especifico

    Args:
        lista_highscore (list[list]): lista a ingresar en archivo
    """
    with open(path, "w",encoding= 'utf-8') as archivo:    
        for puntuacion in lista_highscore:
            
            linea = f"{puntuacion[0]},{puntuacion[1]}\n"
            archivo.write(linea)



import re
def cargar_matriz_csv(path: str):
    """carga datos del path del archivo que se le pasa como parametro

    Returns:
        _type_: lista[list]
    """
    lista_puntuacion = []

    with open(path, "r",encoding= 'utf-8') as archivo:    
        for linea in archivo:
            auxiliar = re.split(",|\n", linea)

            puntuacion_jugador = [auxiliar[0],int(auxiliar[1])]

            lista_puntuacion.append(puntuacion_jugador)
    
    return lista_puntuacion




def agregar_puntuaciones(lista_puntuaciones:list[list], nueva_puntuacion: list):
    """agrega nuevas puntuaciones a la lista

    Args:
        lista_puntuaciones (list[list]): lista con todas las puntuaciones
        nueva_puntuacion (list): nombre jugador y puntuacion

    Returns:
        _type_: _description_
    """

    lista_puntuaciones.append(nueva_puntuacion)

    return lista_puntuaciones



def agregar_jugador_highscore(nombre: str, putuacion: int, lista_score:list[list], path: str, ):
    """Agrega los datos del jugador y la puntuacion a la lista de highscore de top 5 jugadores
    utilizando funciones creadas

    Args:
        nombre (str):nombre del jugador
        putuacion (int): puntuacion del jugador
        lista_score (list[list]): lista de jugadores
        path (str): ruta donde se carga la matriz de jugadores
    """


    nueva_puntuacion = [nombre, putuacion]

    lista_score.append(nueva_puntuacion)


    lista_ordernada = bubble_sort(lista_score)


    matriz = cargar_high_score(lista_ordernada)

    cargar_csv_highscore(matriz, path)