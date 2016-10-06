import Clasificador
import numpy as np

class ClasificadorNaiveBayes(Clasificador):

    entrenamiento = []

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
        datos_train_traspuestos = datos_train.copy()
        datos_train_traspuestos.transpose()
        datos_clase = datos_train_traspuestos[-1]

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
        aprioris = [ datos_clase.count(diccionario[value]) / num_datos_train
                     for value in diccionario ][:-1]

    def clasifica(self,datostest,atributosDiscretos,diccionario):
        pass
                                                
