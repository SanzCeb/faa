from abc import ABCMeta,abstractmethod
import math
import random

class Particion():
  
  indicesTrain=[]
  indicesTest=[]
  
  def __init__(self,indicesTrain, indicesTest):
    self.indicesTrain= indicesTrain
    self.indicesTest= indicesTest

#####################################################################################################

class EstrategiaParticionado(object):
  
  # Clase abstracta
  __metaclass__ = ABCMeta

  # Atributos: deben rellenarse adecuadamente para cada estrategia concreta
  nombreEstrategia="null"
  numeroParticiones=0
  particiones=[]

  def __init__(self, numeroParticiones,nombreEstrategia):
    self.nombreEstrategia = nombreEstrategia
    self.numeroParticiones = numeroParticiones

  @abstractmethod
  # TODO: esta funcion deben ser implementadas en cada estrategia concreta  
  def creaParticiones(self,datos,seed=None):
    pass
  

#####################################################################################################

class ValidacionSimple(EstrategiaParticionado):
  
  porcentajeTest = 0

  
  def __init__(self,numeroParticiones, porcentajeTest):
    EstrategiaParticionado.__init__(self,numeroParticiones,"Validacion Simple")
    self.porcentajeTest = porcentajeTest
    
  def __crea_particion(self,datos):
    """ Metodo que crea la particion simple elegiendo los datos para test
    aleatoriamente y filtrando como datos de entrenamiento los datos que no 
    han sido elegidos"""
    numDatos = len(datos.datos)
    numDatosTest = math.floor(self.porcentajeTest * numDatos)
    indices = range(numDatos)
    indicesTest = random.sample(indices,numDatosTest)
    indicesTrain = [x for x in indices if x not in indicesTest]
    return Particion(indicesTrain,indicesTest)
  
  def creaParticiones(self,datos,seed=None):
    self.particiones = [self.__crea_particion(datos) for i in range(self.numeroParticiones)]
    return self.particiones
      
      
#####################################################################################################      
class ValidacionCruzada(EstrategiaParticionado):
  
  
  def __init__ (self, numeroParticiones):
    EstrategiaParticionado.__init__(self,numeroParticiones,"Validacion Cruzada")
  # Crea particiones segun el metodo de validacion cruzada.
  # El conjunto de entrenamiento se crea con las nfolds-1 particiones
  # y el de test con la particion restante
  # Esta funcion devuelve una lista de particiones (clase Particion)
  # TODO: implementar
  def __crear_particion(self,datos):
    pass
  def creaParticiones(self,datos,seed=None):   
    random.seed(seed)
    pass
    
    
