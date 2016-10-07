from Clasificador import Clasificador
import functools as fp
import operator as op
import numpy as np


class ClasificadorNaiveBayes(Clasificador):

    entrenamiento = []
    a_prioris = []

    def __tabla_discreta (self,
                          valores,
                          hipotesis,
                          diccionario_atributo,
                          diccionario_hipotesis):
        tabla_entrenamiento = list(zip(valores,hipotesis))
        def __num_coincidencias ( atributo, hipotesis):
            return tabla_entrenamiento.count((atributo,
                                              hipotesis))

        for k_atributo in diccionario_atributo:
            dicc = { k_hipotesis : __num_coincidencias (k_atributo, k_hipotesis)
                     for k_hipotesis in diccionario_hipotesis}
            yield k_atributo,dicc

    def __tabla_continua(self,valores, diccionario):
        pass

    def entrenamiento(self,datos_train,atributosDiscretos,diccionario):
        datos_traspuestos = datos_train.transpose()
        datos_atributos = datos_traspuestos[:-1]
        datos_clase = list(datos_traspuestos[-1])
        def genera_tabla (valores, datoDiscreto,diccionario_atributo):
            if datoDiscreto:
                return dict(self.__tabla_discreta(valores,
                                                  datos_clase,
                                                  diccionario_atributo.values(),
                                                  diccionario[-1].values()))
            else:
                return self.__tabla_continua(valores,diccionario)
            pass

        num_datos_train = len(datos_clase)
        self.a_prioris = [ datos_clase.count(dicc[key]) / num_datos_train
                           for dicc in diccionario
                           for key in dicc][:-1]
        self.entrenamiento = list(map(genera_tabla,
                                      datos_atributos,
                                      atributosDiscretos,
                                      diccionario))


    def __calcular_verosimilitud_discreta(self,
                                          frecuencias,
                                          atributo,
                                          hipotesis ):
        casos_favorables = frecuencias[atributo][hipotesis]
        casos_posibles = sum(frecuencias[atributo].values())
        return casos_favorables / casos_posibles
    # Implementar formula gaussiana
    def __calcular_verosimilitud_continua(self,
                                          frecuencias,
                                          atributo,
                                          hipotesis):
        return 0

    def  __calcula__verosimilitud(self,
                                  frecuencias,
                                  atributo,
                                  esDiscreto,
                                  hipotesis):
        if esDiscreto:
            return  self.__calcular_verosimilitud_discreta(frecuencias,
                                                           atributo,
                                                           hipotesis)
        else:
            return self.__calcular_verosimilitud_continua (frecuencias,
                                                           atributo,
                                                           hipotesis)

    def __clasifica_dato (self,dato, atributosDiscretos, diccionario ):
        def __num_casos_a_posteriori ( hipotesis ):
            verosimilitudes = map(lambda x,y,z:
                                  self.__calcula__verosimilitud (x,y,z,
                                                                 hipotesis),
                                  self.entrenamiento,
                                  dato,
                                  atributosDiscretos)
            return fp.reduce(op.mul,verosimilitudes) * self.a_prioris[hipotesis]
        casos_favorables  = list(map( __num_casos_a_posteriori,
                                      diccionario[-1].values()))
        return casos_favorables.index(max(casos_favorables))
    def clasifica(self,datostest,atributosDiscretos,diccionario):
        return [ self.__clasifica_dato (dato,atributosDiscretos,diccionario)
                 for dato in datostest ]

#        casos_favorables = list(map(__calcular_casos_favorables,
 #                                   diccionario[-1]))
  #      clase_mayoritaria = diccionario[casos_favorables.
   #                                          index(max(casos_favorables))]
