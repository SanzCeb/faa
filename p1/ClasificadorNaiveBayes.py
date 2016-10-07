from Clasificador import Clasificador
import numpy as np

class ClasificadorNaiveBayes(Clasificador):

    entrenamiento = []
    a_prioris = []


    def __tabla_discreta (valores,hipotesis,
                          diccionario_atributo,
                          diccionario_hipotesis):

        tabla_entrenamiento = list(zip(valores,hipotesis))
        def __num_coincidencias ( atributo, hipotesis):
            return tabla_entrenamiento.count((atributo,hipotesis)) 

        for k_atributo in diccionario_atributo:
                yield k_atributo,
                {
                    k_hipotesis : __num_coincidencias (k_atributo, k_hipotesis)
                    for k_hipotesis in diccionario_hipotesis
                }

    def __tabla_continua(valores, diccionario):
        pass

    def entrenamiento(self,datos_train,atributosDiscretos,diccionario):
        datos_clase = list(datos_train.transpose()[-1])
        def __genera_tabla (valores, datoDiscreto,diccionario_atributo):
            if datoDiscreto:
                return __tabla_discreta(valores,
                                        datos_clase,
                                        diccionario_atributo.values(),
                                        diccionario[-1].values())
            else:
                return __tabla_continua(valores,diccionario)
            pass

        num_datos_train = len(datos_clase)
        self.a_prioris = [ datos_clase.count(dicc[key]) / num_datos_train
                           for dicc in diccionario
                           for key in dicc][:-1] ]
        self.entrenamiento = list(map(__genera_tabla,
                                      datos_clase,
                                      atributosDiscretos,
                                      diccionario))


    def __calcular_verosimilitud_discreta( frecuencias,
                                           atributo,
                                           hipotesis ):
        casos_favorables = frecuencias[atributo][hipotesis]
        casos_posibles = sum(frecuencias[valor_atributo].values())
        return casos_favorables / casos_posibles
    # Implementar formula gaussiana
    def __calcular_verosimilitud_continua:
        return 0


    def __clasifica_dato ( dato, atributosDiscretos, diccionario ):
        def __num_casos_a_posteriori ( hipotesis ):
            def  __calcula__verosimilitud(frecuencias,atributo,esDiscreto):
                if esDiscreto:
                   return  __calcular_verosimilitud_discreta(frecuencias,
                                                             atributo,
                                                             hipotesis)
                else:
                    return __calcular_verosimilitud_continua (frecuencias,
                                                              atributo,
                                                              hipotesis)
            verosimilitudes = map(__calcula_verosimilitud,
                                  entrenamiento,
                                  dato,
                                  atributosDiscretos)
            return reduce (lambda x,y: x * y ,
                           verosimilitudes) * a_priori[hipotesis]
        casos_favorables  = list(map( __num_casos_a_posteriori,
                                      diccionario[-1].values()))
        return casos_favorables.index(max(casos_favorables))
    def clasifica(self,datostest,atributosDiscretos,diccionario):
        return [ clasifica_dato (dato,atributosDiscretos,diccionario)
                 for dato in datostest ]

#        casos_favorables = list(map(__calcular_casos_favorables,
 #                                   diccionario[-1]))
  #      clase_mayoritaria = diccionario[casos_favorables.
   #                                          index(max(casos_favorables))]
                                                
