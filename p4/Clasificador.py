from abc import ABCMeta,abstractmethod
import numpy as np

class Clasificador(object):
  # Clase abstracta
  __metaclass__ = ABCMeta

  # Metodos abstractos que se implementan en casa clasificador concreto
  @abstractmethod
  # TODO: esta funcion deben ser implementadas en cada clasificador concreto
  # datosTrain: matriz numpy con los datos de entrenamiento
  # atributosDiscretos: array bool con la indicatriz de los atributos nominales
  # diccionario: array de diccionarios de la estructura Datos utilizados para la codificacion
  # de variables discretas
  def entrenamiento(self,datosTrain,atributosDiscretos,diccionario):
    pass


  # TODO: esta funcion deben ser implementadas en cada clasificador concreto
  # devuelve un numpy array con las predicciones
  def clasifica(self,datosTest,atributosDiscretos,diccionario):
    scores = self.score(datosTest,atributosDiscretos, diccionario)
    return np.argmax(scores, axis = 1)

  def score (self, datosTest, atributosDiscretos, diccionario):
    scores = np.zeros((len(datosTest), len(diccionario[-1])))
    preds = map(int, self.clasifica(datosTest,atributosDiscretos, diccionario))
    scores[range(datosTest.shape[0]), preds] = 1.0 
    return scores 
  
  def error(self,datos,pred):
    """Se cuenta tanto el numero de errores como el total de 
    datos clasificados, para calcular la tasa de error"""
    errores = 0
    total = 0
    for (x,y) in zip(datos,pred):
      if (x - y).any():
        errores += 1
      total += 1
    return 1 if total == 0 else errores / total
    

  def validacion(self,particionado,dataset,clasificador,seed=None):
    """Funcion que realiza una clasificacion utilizando una estrategia determinada
    por cada particion creada por el objeto particionado"""
    def __calculaError ( particion ):
      datos_train = dataset.extraeDatosTrain(particion)
      clasificador.entrenamiento( datos_train,
                                  dataset.nominalAtributos,
                                  dataset.diccionarios )
      datos_test = dataset.extraeDatosTest ( particion )
      prediccion = clasificador.clasifica ( datos_test,
                                            dataset.nominalAtributos,
                                            dataset.diccionarios )
      print("Particion clasificada")
      return self.error ( datos_test[:,-1], prediccion )
    particiones = particionado.creaParticiones(dataset)
    return list(map(__calculaError, particiones))

