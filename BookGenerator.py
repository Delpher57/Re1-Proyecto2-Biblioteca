from dataclasses import dataclass
import random
import Data
import urllib.request


#generamos los arrays 
def generar_arrays():
    """[generamos los arrays con las palabras que ocupamos]

    Returns:
        [array]: [listas de las palabras para generar titulos y autores]
    """    

    palabras = './listado-general.txt'

    nombres = './nombres-propios-es.txt'

    apellidos = './apellidos-es.txt'

    uniones = './uniones.txt'

    listado = [palabras,nombres,apellidos,uniones]

    diccionario = {"palabras": [], "nombres": [], "apellidos": [], "uniones": []}


    max = len(listado)
    for i in range(0,max):
        archivo = open(listado[i], 'r', encoding="utf8")
        txt = archivo.read()
        words = txt.splitlines()
        listado[i] = words

    
    diccionario["palabras"] = listado[0]
    diccionario["nombres"] = listado[1]
    diccionario["apellidos"] = listado[2]
    diccionario["uniones"] = listado[3]
    
    return diccionario


def generar_libros(cantidad = 1):
    """[generamos libros aleatorios,  cooooombre, autor y fotografia]

    Args:
        cantidad (int, optional): [cantidad de libros por generar]. Defaults to 1.

    Returns:
        [array]: [array de objetos libro]
    """  
    diccionario = generar_arrays()

    libros = []

    for i in range(0,cantidad):
        nombre = (random.choice(random.choice([diccionario["palabras"], diccionario["nombres"],diccionario["palabras"]])) 
                    + " " + random.choice(diccionario["uniones"])
                    + " " + random.choice(random.choice([diccionario["palabras"], diccionario["nombres"],diccionario["apellidos"]])))
        
        nombre = nombre.title()        

        autor = (random.choice(diccionario["nombres"])
                    + " " + random.choice(diccionario["apellidos"]))

        webUrl = urllib.request.urlopen('https://picsum.photos/200/300')
        webUrl = webUrl.geturl()

        libro = Data.Libro(i,nombre,autor,webUrl)
        libros += [libro]

    return libros
        


