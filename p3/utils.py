import numpy as np
import random
from unittest import TestCase
from datetime import datetime

def generar_bits (num):
    """Genera un numpy array con bits aleatorios"""
    return np.random.rand(num).round()

def entero_aleatorio(a,b):
    """Devuelve un numero entero aleatorio dentro del 
    intervalo [a,b]"""
    random.seed(datetime.now())
    return random.randint(a,b)

def numero_aleatorio(a,b):
    """Devuelve un numero flotante aleatorio dentro del 
    intervalo [a,b]"""
    random.seed(datetime.now())
    return random.uniform(a,b)

def crear_esquema(diccionarios):
    """metodo que devuelve la longitud de cada alelo del cromosoma
    a partir de la lista de diccionarios"""
    esquema = []
    for dicc in diccionarios:
        num_alelos = len(dicc.keys())
        if num_alelos:
            esquema.append(num_alelos)
    return esquema

<<<<<<< .working
def generar_codigos(length):
    """Funcion para generar el conjuntos de posibles codigos de un atributo
    en funcion del tamaño de su conjunto"""
    return np.identity(length)

||||||| .merge-left.r90
def generar_codigos(length):
    """Funcion para generar el conjuntos de posibles codigos de un atributo
    en funcion del tamaño de su conjunto"""
    return np.identity(3)

=======
>>>>>>> .merge-right.r92
class UtilsTests (TestCase):
        def crear_esquema_test(self):
            diccionarios = [{'a':0,'b':3,'c':1},{'z':2, 'w':5, 'r': 10,'o':8}, {'x': 0, 'y': '1'}]
            self.assertEqual(crear_esquema(diccionarios), [3,4,2])
            diccionarios = [{}]
            self.assertEqual(crear_esquema(diccionarios), [])
            diccionarios = [{'hola':1, 'adios':0},{'haciendo':2,'un test': 2}]
            self.assertEqual(crear_esquema(diccionarios), [2,2])
