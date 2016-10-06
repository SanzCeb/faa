from Clasificador import Clasificador
import numpy as np

class ClasificadorNaiveBayes(Clasificador):

    entrenamiento = []
    a_prioris = []
    def __tabla_discreta (valores,hipotesis,
                          diccionario_atributo,
                          diccionario_hipotesis):

        for k_atributo in diccionario_atributo:
            for k_hipotesis in diccionario_hipotesis:
                yield k_atributo , list(zip(valores,
                                            hipotesis)).count((k_atributo,
                                                               k_hipotesis))

    def __tabla_continua(valores, diccionario):
        pass

    def entrenamiento(self,datos_train,atributosDiscretos,diccionario):
        datos_clase = list(datos_train.transpose()[-1])
        def __genera_tabla (valores, datoDiscreto,diccionario_atributo):
            if datoDiscreto: 
                return dict(__tabla_discreta(valores,
                                             datos_clase,
                                             diccionario_atributo,
                                             diccionario[-1]))
            else:
                return __tabla_continua(valores,diccionario)
            pass
        num_datos_train = len(datos_clase)
        self.a_prioris = [ datos_clase.count(dicc[key]) / num_datos_train
                           for dicc in diccionario
                           for key in dicc][:-1]

    def clasifica(self,datostest,atributosDiscretos,diccionario):
        pass
                                                
