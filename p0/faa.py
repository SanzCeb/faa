import numpy as np

 def leer_dato(fichero):
  """Lee una linea del fichero y divide la linea en tantos trozos como comas"""
  return fichero.readline().split('\n')[0].split(',')

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
    self.supervisado = sup
    dataFile = open(nombreFichero,'r')
    numDatos = int(dataFile.readline())
    self.nombreAtributos = leer_dato(dataFile)
    self.tipoAtributos = leer_dato(dataFile)
    self.datos = np.array([leer_dato(dataFile) for x in xrange(numDatos)])
    dataFile.close()
    

    
    
  # TODO: hacer en las proximas practicas
  def extraeDatosTrain(idx):
    pass
  
  def extraeDatosTest(idx):
    pass



  
