from Clasificador import Clasificador 
import numpy as np
import math 

def normalizar_atributo(datos_atributo,esDiscreto,mean,std):
    if (esDiscreto):
        return datos_atributo
    else:
        return list(map(lambda x: (x - mean) / std, datos_atributo))
class ClasificadorKNN (Clasificador):
    datos = np.array([])
    means = []
    stdevs = []
    k = 0
    def __init__(self,k):
        super(ClasificadorKNN,self).__init__()
        self.k = k
            
    def entrenamiento(self, datosTrain, atributosDiscretos, diccionario):
        datos_traspuestos = datosTrain.transpose()
        self.means = list(map(np.mean,datos_traspuestos))
        self.stdevs = list(map(np.std,datos_traspuestos))
        datos_normalizados = map(normalizar_atributo,
                                 datos_traspuestos,
                                 atributosDiscretos,
                                 self.means,
                                 self.stdevs)
        self.datos = np.array(list(datos_normalizados)).transpose()
  
    def __clasifica_dato(self,dato, atributosDiscretos, diccionario):
        def __dist_euclides(dato_entrenamiento):
            def dist_eje (x,y,esDiscreto):
                return int (x != y) if esDiscreto else pow((x - y),2)
            return math.sqrt(sum(map(dist_eje,
                                     dato_entrenamiento,
                                     dato,
                                     atributosDiscretos)))         
        distancias = map(__dist_euclides,self.datos[:,:-1])
        distancias_min = sorted(zip(distancias,self.datos[:,-1]),key = lambda x: x[0])[:self.k]
        vecinos = list(map(lambda x : x[1], distancias_min))
        dominio_clase = list(diccionario[-1].values())
        frecuencias_clases = list(map(vecinos.count,dominio_clase))
        return dominio_clase[frecuencias_clases.index(max(frecuencias_clases))]
                    
    def clasifica (self, datosTest, atributosDiscretos, diccionario):
        datos_test_normalizados = np.array(list(map(normalizar_atributo,
                                                    datosTest.transpose(),
                                                    atributosDiscretos,
                                                    self.means,
                                                    self.stdevs))).transpose()                             
        return [ self.__clasifica_dato (dato,atributosDiscretos,diccionario)
                 for dato in datos_test_normalizados]

    
