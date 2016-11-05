from copy import deepcopy
from Clasificador import Clasificador
import numpy as np 

class ClasificadorMulticlase(Clasificador):

  def __init__(self,clasificadorbase):
    self.clasificadorbase=clasificadorbase
    self.clasificadores=[]
    
  
  def entrenamiento(self,datostrain,atributosDiscretos,diccionario):
    
  
    # se van diferentes labels en funcion de la estrategia multiclase
    n_classes=len(diccionario[-1])
    self.clasificadores=[]
    ovadiccionario=deepcopy(diccionario)
    ovadiccionario[-1]={'-':0, '+':1}
    
    
    for i in range(n_classes):
      new_y=np.zeros((datostrain.shape[0],1))
      new_y[datostrain[:,-1]==i,:]=1
      self.clasificadores.append(deepcopy(self.clasificadorbase))
      self.clasificadores[i].entrenamiento(np.append(datostrain[:,:-1],new_y,axis=1),atributosDiscretos,ovadiccionario)
      
      
      
      
      
  def clasifica(self,datostest,atributosDiscretos,diccionario):
    scores=np.zeros((datostest.shape[0],len(self.clasificadores)))
    ovadiccionario=deepcopy(diccionario)
    ovadiccionario[-1]={'-':0, '+':1}
    # evaluar el score para cada clasificador one-versus-all
    for i,c in enumerate(self.clasificadores):
      scores[:,i]=c.score(datostest,atributosDiscretos,ovadiccionario)[:,1]
      # se predice como aquella clase con mas confianza
      preds=np.argmax(scores,axis=1)
      return preds
