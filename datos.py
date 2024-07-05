import json
def cargar_archivo_json (path: str):
    """Carga un archivo con datos

    Args:
        path (str): ruta del archivo

    Returns:
        data: la información dentro del archivo
    """

    with open(path, "r", encoding= 'utf-8' ) as archivo:
        data = json.load(archivo)

    return data

