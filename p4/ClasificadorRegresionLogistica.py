import numpy as np
import random
import math
from operator import mul,neg

from EstrategiaParticionado import ValidacionCruzada
from datos import Datos
from ClasificadorMulticlase import ClasificadorMulticlase
from sklearn.multiclass import OneVsRestClassifier
from Clasificador import Clasificador

from scipy.special import expit
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn import datasets
from numpy.linalg import norm

def sigmoidal (a):
    if a >= 700:
        return 1
    elif a <= -700:
        return 0
    else:
        return 1 / (1 + math.exp(-a))

def crear_vector_w(d):
    return np.array([ random.uniform(-0.5,0.5) for i in range(d) ])

def crear_vector_datos(dato):
    return np.insert(dato,0,1)

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
        self.w = crear_vector_w(len(atributosDiscretos))
        for epoca in range(self.num_epocas):
            for dato in datosTrain:
                vector_datos = crear_vector_datos(dato[:-1])
                pe = np.dot( self.w,vector_datos)
                sigmoidal_res = sigmoidal(pe)
                self.w = self.__generar_vector_nuevo(vector_datos,
                                                     sigmoidal_res,
                                                     dato[-1])
        return self.w
    def __calcular_confianza(self,vector_dato_test):
        return np.dot(self.w,vector_dato_test) / norm(self.w)

    def __verosimilitud(self,vector_dato_test):
        return sigmoidal(np.dot(self.w,vector_dato_test))

    def __clasifica_dato(self,dato_test):
        return int(self.__verosimilitud(dato_test) > 0.5)

    def clasifica (self, datosTest, atributosDiscretos, diccionario):
        vectores_datos_test = map(crear_vector_datos,datosTest)
        return map(self.__clasifica_dato, vectores_datos_test)

    def __vector_confianza(self, datosTest):
        vectores_datos_test = map(crear_vector_datos,datosTest)
        return map(self.__calcular_confianza, vectores_datos_test)

    def score (self, datosTest, atributosDiscretos, diccionario):
        scores = np.zeros((datosTest.shape[0], 2))
        confianzas = self.__vector_confianza(datosTest)
        for (i,confianza) in enumerate(confianzas):
            scores[i,1] = confianza
        return scores

