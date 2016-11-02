from Clasificador import Clasificador
import numpy as np
import random
import math
from operator import mul,sub

def producto_escalar(w,x):
    return sum(map(mul,w,x))
def calcular_sigmoidal (a):
    return expit(a)
def generar_vector(d):
    return np.array([ random.uniform(-1,1) for i in range(d) ])
class ClasificadorRegresionLogistica(Clasificador):
    w = np.array([])
    n = 0.0 #cte aprendizaje
    num_epocas = 0

    def __init__(self,num_epocas, n):
        super(ClasificadorRegresionLogistica, self).__init__()
        self.num_epocas = num_epocas
        self.n = n
    def __generar_vector_nuevo(self,dato,sigmoidal,clase):
        factor = self.n * (sigmoidal - clase)
        return self.w - np.array(list(map(lambda x : x * factor, dato)))
    def entrenamiento(self, datosTrain, atributosDiscretos, diccionario):
        self.w = generar_vector(len(atributosDiscretos))
        for epoca in range(self.num_epocas):
            for dato in datosTrain:
                pe = producto_escalar(self.w,dato[:-1])
                sigmoidal = calcular_sigmoidal(pe)
                self.w = self.__generar_vector_nuevo(dato,
                                                     sigmoidal,
                                                     dato[-1])
        return self.w
    def __clasifica_dato(self,dato_test):
        return int(calcular_sigmoidal(producto_escalar(self.w,dato_test)) > 0.5)
    def clasifica (self, datosTest, atributosDiscretos, diccionario):
        return list(map(self.__clasifica_dato, datosTest))
