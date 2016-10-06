import Clasificador

class ClasificadorAPriori(Clasificador):
  
  mayoritaria=0

  # TODO: implementar
  def entrenamiento(self,datostrain,atributosDiscretos=None,diccionario=None):
    # Obtener la clase mayoritaria de los datos
    columna_clase = [ dato[-1] for dato in datostrain ]
    mayoritaria = max ( map(columna_clase.count, diccionario['Class']) )
    
    
  # TODO: implementar
  def clasifica(self,datostest,atributosDiscretos=None,diccionario=None):
    return [ mayoritaria for dato in datostest ]
