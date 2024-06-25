import json
def cargar_archivo_json (path: str):

    with open(path, "r", encoding= 'utf-8' ) as archivo:
        data = json.load(archivo)

    return data

