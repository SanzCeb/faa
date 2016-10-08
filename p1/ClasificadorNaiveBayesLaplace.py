from ClasificadorNaiveBayes import ClasificadorNaiveBayes

class ClasificadorNaiveBayesLaplace (ClasificadorNaiveBayes):
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
    
