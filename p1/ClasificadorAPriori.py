from Clasificador import Clasificador

class ClasificadorAPriori(Clasificador):
  
  mayoritaria=0
  # TODO: implementar
  def entrenamiento(self,datostrain,atributosDiscretos=None,diccionario=None):
    # Obtener la clase mayoritaria de los datos
    columna_clase = [ dato[-1] for dato in datostrain ]
    frecuencias = list(map(columna_clase.count, diccionario[-1].values()))
    self.mayoritaria = frecuencias.index(max(frecuencias))
    
    
  # TODO: implementar
  def clasifica(self,datostest,atributosDiscretos=None,diccionario=None):
    return [ self.mayoritaria for dato in datostest ]
