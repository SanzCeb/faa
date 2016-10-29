import Clasificador 
import numpy as np
import math 

def normalizar_atributo(datos_atributo,esDiscreto):
    if (esDiscreto):
        return datos_atributo
    else:
        mean = np.mean(datos_atributo)
        var = np.var(datos_atributo)
        return list(map(lambda x: (x - mean) / var, datos_atributo))
class ClasificadorKNN (Clasificador):
    datos = np.array([])
    k = 0
    def __init__(self,k):
        super(ClasificadorKNN,self).__init__()
        self.k = k
            
    def entrenamiento(self, datosTrain, atributosDiscretos, diccionario):
        datos_traspuestos = datosTrain.transpose()
        datos_normalizados = map(normalizar_atributo,
                                 datos_traspuestos,
                                 atributosDiscretos)
        self.datos = np.array(list(datos_normalizados)).transpose()

    def __clasifica_dato(self,dato, atributosDiscretos, diccionario):
        def __dist_euclides(dato_entrenamiento):
            def dist_eje (x,y,esDiscreto):
                return int(x != y) if esDiscreto else (x - y) ** 2
            return math.sqrt(sum(map(dist_eje,
                                     dato_entrenamiento,
                                     dato,
                                     atributosDiscretos)))
                
        distancias = map(__dist_euclides,self.datos)
        distancias_min = sorted(distancias)[:self.k]
        frecuencias_clases = list(map(distancias_min.count,diccionario[-1]))
        return frecuencias_clases.index(max(frecuencias_clases))
                    
    def clasifica (self, datosTest, atributosDiscretos, diccionario):
        return [ self.__clasifica_dato (dato,atributosDiscretos,diccionario)
                 for dato in datosTest ]
