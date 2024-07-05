def cargar_high_score(lista_puntuaciones):

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



def bubble_sort(lista):

    for i in range(len(lista)):
        for j in range(0, len(lista) -1):
            if lista[j][1] < lista[j+1][1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista



def cargar_csv_highscore(lista_highscore):

    with open(r"datos/score.csv", "w",encoding= 'utf-8') as archivo:    
        for puntuacion in lista_highscore:
            linea = f"{puntuacion[0]},{puntuacion[1]}\n"
            archivo.write(linea)



import re
def cargar_matriz_csv():

    lista_puntuacion = []

    with open(r"datos/score.csv", "r",encoding= 'utf-8') as archivo:    
        for linea in archivo:
            auxiliar = re.split(",|\n", linea)

            puntuacion_jugador = [auxiliar[0],auxiliar[1]]

            lista_puntuacion.append(puntuacion_jugador)
    
    return lista_puntuacion





