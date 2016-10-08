from Clasificador import Clasificador
import functools as fp
import operator as op
import numpy as np
import scipy.stats as stats
import math

class ClasificadorNaiveBayes(Clasificador):

    tabla_frecuencia = []
    probs_a_priori = []

    def __tabla_discreta (self,
                          columna_atributo,
                          hipotesis,
                          conjunto_atributo,
                          conjunto_hipotesis):
        """Funcion que realiza el cruce del conjunto de valores de un atributo
        con el conjunto de hipotesis."""
        tabla_entrenamiento = list(zip(columna_atributo,hipotesis))
        def __num_coincidencias ( atributo, hipotesis):
            return tabla_entrenamiento.count((atributo,
                                              hipotesis))

        for k_atributo in conjunto_atributo:
            frecuencias = { k_hipotesis :
                            __num_coincidencias (k_atributo, k_hipotesis)
                            for k_hipotesis in conjunto_hipotesis}
            yield k_atributo,frecuencias


    def __tabla_continua(self,
                         columna_atributo,
                         columna_clase,
                         conjunto_hipotesis):
        """Funcion que genera la funcion de un atributo continuo
        a partir de los datos de entrenamiento"""
        for k_hipotesis in conjunto_hipotesis:
            datos_clase = [ valor
                            for (valor,hipotesis) in
                            zip (columna_atributo,columna_clase)
                            if hipotesis == k_hipotesis ]
            gaussiana = stats.norm(np.mean(datos_clase),np.std(datos_clase))
            yield k_hipotesis, gaussiana.pdf




    def __calcular_verosimilitud_discreta(self,
                                          frecuencias,
                                          atributo,
                                          hipotesis ):
        """Calcula la verosimilitud de la hipotesis a partir
        del valor del atributo del dato que queremos clasificar
        y de las frecuencias recogidas durante el entrenamiento"""
        casos_favorables = frecuencias[atributo][hipotesis]
        casos_posibles = sum(frecuencias[atributo].values())
        return (casos_favorables / casos_posibles)

    def __calcular_verosimilitud_continua(self,
                                          frecuencias,
                                          atributo,
                                          hipotesis):
        return frecuencias[hipotesis](atributo)


    def  __calcula__verosimilitud(self,
                                  frecuencias,
                                  atributo,
                                  esDiscreto,
                                  hipotesis):
        """Funcion que comprueba si el atributo es discreto o no
        para decidir que funcion debe de calcular la verosimilitud"""
        if esDiscreto:
            return self.__calcular_verosimilitud_discreta(frecuencias,
                                                               atributo,
                                                               hipotesis)
        else:
            return self.__calcular_verosimilitud_continua (frecuencias,
                                                                atributo,
                                                                hipotesis)


    def __clasifica_dato (self,dato, atributosDiscretos, diccionario ):
        def __num_casos_a_posteriori ( hipotesis ):
            verosimilitudes = map(lambda frecuencias,atributo,esDiscreto:
                                  self.__calcula__verosimilitud (frecuencias,
                                                                 atributo,
                                                                 esDiscreto,
                                                                 hipotesis),
                                  self.tablas_frecuencias,
                                  dato,
                                  atributosDiscretos)
            prob_a_priori = self.probs_a_priori[hipotesis]
            return fp.reduce(op.mul,verosimilitudes) * prob_a_priori

        casos_favorables  = list(map( __num_casos_a_posteriori,
                                      diccionario[-1].values()))

        return casos_favorables.index(max(casos_favorables))


    def entrenamiento(self,datos_train,atributosDiscretos,diccionario):
        datos_traspuestos = datos_train.transpose()
        datos_atributos = datos_traspuestos[:-1]
        datos_clase = list(datos_traspuestos[-1])

        def __genera_tabla (valores, datoDiscreto,diccionario_atributo):
            if datoDiscreto:
                return dict(self.__tabla_discreta(valores,
                                                  datos_clase,
                                                  diccionario_atributo.values(),
                                                  diccionario[-1].values()))
            else:
                return dict(self.__tabla_continua(valores,
                                             datos_clase,
                                             diccionario[-1].values()))

        num_datos_train = len(datos_clase)
        self.probs_a_priori = [ datos_clase.count(dicc[key]) / num_datos_train
                                for dicc in diccionario
                                for key in dicc][:-1]

        self.tablas_frecuencias = list(map(__genera_tabla,
                                      datos_atributos,
                                      atributosDiscretos,
                                      diccionario))

    def clasifica(self,datostest,atributosDiscretos,diccionario):
        return [ self.__clasifica_dato (dato,atributosDiscretos,diccionario)
                 for dato in datostest ]


