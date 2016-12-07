import numpy as np
import random
from unittest import TestCase


def generar_bits (num):
    """Genera un numpy array con bits aleatorios"""
    return np.random.rand(num).round()

def entero_aleatorio(a,b):
    """Devuelve un numero entero aleatorio dentro del 
    intervalo [a,b]"""
    return random.randint(a,b)

def numero_aleatorio(a,b):
    """Devuelve un numero flotante aleatorio dentro del 
    intervalo [a,b]"""
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

def generar_codigos(length):
    """Funcion para generar el conjuntos de posibles codigos de un atributo
    en funcion del tamaño de su conjunto"""
    return np.identity(length)

def generar_conclusion(length):
    """Funcion para generar una clausula en la que un solo predicado sea cierto"""
    conclusion = np.zeros(length)
    conclusion[entero_aleatorio(0,length -1)] = 1
    return conclusion

def elemento_mas_frecuente(values):
    """Funcion que devuelvue el elemento mas repetido de la lista variable de argumentos"""
    return sorted(set(values), key = values.count)[-1]

class UtilsTests (TestCase):
        def crear_esquema_test(self):
            diccionarios = [{'a':0,'b':3,'c':1},{'z':2, 'w':5, 'r': 10,'o':8}, {'x': 0, 'y': '1'}]
            self.assertEqual(crear_esquema(diccionarios), [3,4,2])
            diccionarios = [{}]
            self.assertEqual(crear_esquema(diccionarios), [])
            diccionarios = [{'hola':1, 'adios':0},{'haciendo':2,'un test': 2}]
            self.assertEqual(crear_esquema(diccionarios), [2,2])
        def generar_codigos(self):
            codigos = list(generar_codigos(3))

            self.assertFalse((codigos[0] - np.array([1,0,0])).any())
            self.assertFalse((codigos[1] - np.array([0,1,0])).any())
            self.assertFalse((codigos[2] - np.array([0,0,1])).any())

        def generar_conclusion_test(self):

            for i in range(100):
                conclusion = generar_conclusion(entero_aleatorio(1,100))
                self.assertEqual(sum(conclusion),1)
            
        def elemento_mas_frecuente_test(self):
            self.assertEqual(elemento_mas_frecuente([1,2,3,4,1]), 1)
            
            
