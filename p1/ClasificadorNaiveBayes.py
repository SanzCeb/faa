import Clasificador
import numpy as np 

class ClasificadorNaiveBayes(Clasificador):

    entrenamiento = []
  def __tabla_discreta (valores,hipotesis,diccionario_atributo,diccionario_hipotesis):
      pass
  def __tabla_continua (valores,diccionario):
      pass

  def entrenamiento(self,datos_train,atributosDiscretos,diccionario):
      datos_train_traspuestos = datos_train.copy().transpose()
      datos_clase = datos_train_traspuestos[-1]
      def __genera_tabla (valores, datoDiscreto,diccionario_atributo):
          if datoDiscreto: 
              return __tabla_discreta(valores,datos_clase,diccionario_atributo,diccionario[-1])
          else
              return __tabla_continua(valores,diccionario)
      entrenamiento = list(map(__genera_tabla,datos_train_traspuestos,atributosDiscretos,diccionario))
      num_datos_train = len(datos_clase)
      aprioris = [ datos_clase.count(diccionario[value]) / num_datos_train
                   for value in diccionario ][:-1]
      
  def clasifica(self,datostest,atributosDiscretos,diccionario):
    pass

    
  
