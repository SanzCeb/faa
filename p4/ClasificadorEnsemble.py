from Clasificador import Clasificador
from utils import elemento_mas_frecuente

class ClasificadorEnsemble(Clasificador):
    clasificadores = []
    
    def __init__(self, clasificadores):
        super(ClasificadorEnsemble,self).__init__()
        self.clasificadores = clasificadores

    
    def entrenamiento(self, datosTrain, atributosDiscretos, diccionario):

        for clasificador in self.clasificadores:
            clasificador.entrenamiento(datosTrain,
                                       atributosDiscretos,
                                       diccionario)

    def clasifica(self,datosTest,atributosDiscretos,diccionario):        
        def __clasifica(clasificador):
            return clasificador.clasifica(datosTest,
                                          atributosDiscretos,
                                          diccionario)
        clasificaciones = list(map(__clasifica, self.clasificadores))

        def clasificacion_iesima(i):
            return [clasificacion[i]
                    for clasificacion in clasificaciones]

        return [ elemento_mas_frecuente(clasificacion_iesima(pos_dato))
                 for pos_dato in range(len(datosTest))]
        
    
        
