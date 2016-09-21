import numpy as np

class Datos(object):
  
  supervisado=True
  TiposDeAtributos=('Continuo','Nominal')
  tipoAtributos=[]
  nombreAtributos=[]
  nominalAtributos=[]
  datos=np.array(())
  # Lista de diccionarios. Uno por cada atributo.
  diccionarios=[]
 
  # TODO: procesar el fichero para asignar correctamente las variables supervisado, tipoAtributos, nombreAtributos,nominalAtributos, datos y diccionarios
  def __init__(self, nombreFichero,sup):
    
  # TODO: hacer en las proximas practicas
  def extraeDatosTrain(idx):
    pass
  
  def extraeDatosTest(idx):
    pass



  