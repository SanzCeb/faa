from abc import ABCMeta,abstractmethod
import math
import random

class Particion():
  
  indicesTrain=[]
  indicesTest=[]
  
  def __init__(self,indicesTrain, indicesTest):
    self.indicesTrain= indicesTrain
    self.indicesTest= indicesTest


class EstrategiaParticionado(object):
  
  __metaclass__ = ABCMeta


  nombreEstrategia="null"
  numeroParticiones=0
  particiones=[]

  def __init__(self, numeroParticiones,nombreEstrategia):
    self.nombreEstrategia = nombreEstrategia
    self.numeroParticiones = numeroParticiones

  @abstractmethod
  def creaParticiones(self,datos,seed=None):
    pass
  

#####################################################################################################

class ValidacionSimple(EstrategiaParticionado):
  
  porcentajeTest = 0

  """Clase que realiza el particionado tradicional"""
  def __init__(self,numeroParticiones, porcentajeTest):
    EstrategiaParticionado.__init__(self,numeroParticiones,"Validacion Simple")
    self.porcentajeTest = porcentajeTest
    
  def __crea_particion(self,datos):
    """ Metodo que crea la particion simple elegiendo los datos para test
    aleatoriamente y filtrando como datos de entrenamiento los datos que no 
    han sido elegidos"""
    numDatos = len(datos.datos)
    numDatosTest = math.floor(self.porcentajeTest * numDatos)
    indices = set(range(numDatos))
    indicesTest = set(random.sample(indices,numDatosTest))
    indicesTrain = indices.difference(indicesTest)
    return Particion(list(indicesTrain),list(indicesTest))

  def creaParticiones(self,datos,seed=None):
    self.particiones = [self.__crea_particion(datos) for i in range(self.numeroParticiones)]
    return self.particiones
  
      
#####################################################################################################      
class ValidacionCruzada(EstrategiaParticionado):
  def __init__ (self,k):
    EstrategiaParticionado.__init__(self,k,"Validacion Cruzada")
    
  def __split_list (self,sequence):
    """Parte la lista en k folds y devuelve una lista de folds"""
    folds = []
    longitud_fold = len(sequence) // self.numeroParticiones
    seek = 0
    for i in range(self.numeroParticiones - 1):
      last = seek + longitud_fold
      folds.append(sequence[seek : last])
      seek = last
    folds.append(sequence[seek:])
    return folds
  def __generar_rango_permutado(self,datos):
    indices = list(range(len(datos)))
    random.shuffle(indices)
    return indices
  def creaParticiones(self,datos,seed=None):
    """Parte la lista de indices en k folds
    para luego crear las k particiones
    permutando los distintos folds como train 
    y como test"""
    indices = self.__generar_rango_permutado(datos.datos)
    folds = map(set,self.__split_list(indices))
    indices_set = set(indices) 
    self.particiones = [Particion(list(indices_set.difference(fold)),
                                  list(fold))
                        for fold in folds]
    return self.particiones
  
    
