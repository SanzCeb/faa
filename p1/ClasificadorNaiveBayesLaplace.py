from ClasificadorNaiveBayes import ClasificadorNaiveBayes

class ClasificadorNaiveBayesLaplace (ClasificadorNaiveBayes):
    def __clasifica_dato (self,dato, atributosDiscretos, diccionario ):
        def __num_casos_a_posteriori ( hipotesis ):
            verosimilitudes = map(lambda frecuencias,atributo,esDiscreto:
                                  log(self.__calcula__verosimilitud (frecuencias,
                                                                     atributo,
                                                                     esDiscreto,
                                                                     hipotesis)),
                                  self.tablas_frecuencias,
                                  dato,
                                  atributosDiscretos)
            prob_a_priori = self.probs_a_priori[hipotesis]
            caso_favorable = sum(verosimilitudes,log(prob_a_priori))
            return caso_favorable

        casos_favorables  = list(map( __num_casos_a_posteriori,
                                      diccionario[-1].values()))

        return casos_favorables.index(max(casos_favorables))
    def __correccion_Laplace (self,tabla_frecuencia,esDiscreto):
            for k_atributo in tabla_frecuencia:
                if esDiscreto:
                    for k_hipotesis in tabla_frecuencia[k_atributo]:
                        nueva_tabla = tabla_frecuencia.copy()
                        nueva_tabla[k_atributo][k_hipotesis] += 1
                        return nueva_tabla
                else:
                    return tabla_frecuencia
                
    def entrenamiento (self,datos_train,atributosDiscretos,diccionario):
        super(ClasificadorNaiveBayesLaplace,
              self).entrenamiento(datos_train, atributosDiscretos, diccionario)
        self.tablas_frecuencias = list(map(self.__correccion_Laplace,
                                           self.tablas_frecuencias,
                                           atributosDiscretos))
    
